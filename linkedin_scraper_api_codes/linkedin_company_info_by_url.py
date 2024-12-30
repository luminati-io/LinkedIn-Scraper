import requests
import json
import time
import logging
from datetime import datetime
from typing import List, Dict, Optional, Any


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class LinkedInCompanyInfo:
    API_BASE_URL = "https://api.brightdata.com/datasets/v3"
    DATASET_ID = "gd_l1vikfnt1wgvvqz95w"

    def __init__(self, api_token: str):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }

    def collect_company_info(
        self, company_urls: List[Dict[str, str]]
    ) -> Optional[bool]:
        start_time = datetime.now()
        logging.info(
            f"Starting collection for {len(company_urls)} companies at {start_time.strftime('%H:%M:%S')}"
        )

        collection_response = self._trigger_collection(company_urls)
        if not collection_response or "snapshot_id" not in collection_response:
            logging.error("Failed to initiate data collection")
            return None
        snapshot_id = collection_response["snapshot_id"]
        logging.info("Collection initiated")

        logging.info("Collecting data:")
        while True:
            status = self._check_status(snapshot_id)
            current_time = datetime.now()
            elapsed = (current_time - start_time).seconds

            if status == "ready":
                logging.info(f"Collection completed after {elapsed} seconds")
                company_data = self._fetch_data(snapshot_id)
                if company_data:
                    break
            elif status in ["failed", "error"]:
                logging.error(f"Collection failed with status: {status}")
                return None
            logging.info(f"Status: {status} ({elapsed}s elapsed)")
            time.sleep(5)
        self._save_data(company_data)
        return True

    def _trigger_collection(
        self, company_urls: List[Dict[str, str]]
    ) -> Optional[Dict[str, Any]]:
        try:
            logging.info("Connecting to API...")
            response = requests.post(
                f"{self.API_BASE_URL}/trigger",
                headers=self.headers,
                params={"dataset_id": self.DATASET_ID},
                json=company_urls,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to trigger collection: {str(e)}")
            return None

    def _check_status(self, snapshot_id: str) -> Optional[str]:
        try:
            response = requests.get(
                f"{self.API_BASE_URL}/progress/{snapshot_id}",
                headers=self.headers,
                timeout=30,
            )
            response.raise_for_status()
            return response.json().get("status")
        except requests.exceptions.RequestException:
            return "error"

    def _fetch_data(self, snapshot_id: str) -> Optional[List[Dict[str, Any]]]:
        try:
            response = requests.get(
                f"{self.API_BASE_URL}/snapshot/{snapshot_id}",
                headers=self.headers,
                params={"format": "json"},
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

    def _save_data(
        self, data: List[Dict[str, Any]], filename: str = "linkedin_company_info.json"
    ) -> None:
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logging.error(f"Error saving data: {str(e)}")


def main() -> None:
    api_token = "<YOUR_API_TOKEN>"
    collector = LinkedInCompanyInfo(api_token)

    companies = [
        {"url": "https://il.linkedin.com/company/ibm"},
        {"url": "https://www.linkedin.com/company/stalkit"},
        {
            "url": "https://www.linkedin.com/organization-guest/company/the-kraft-heinz-company"
        },
        {"url": "https://il.linkedin.com/company/bright-data"},
    ]

    collector.collect_company_info(companies)


if __name__ == "__main__":
    main()