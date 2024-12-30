import requests
import json
import time
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional

# Configure logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

BRIGHTDATA_API_URL = "https://api.brightdata.com/datasets/v3"


class LinkedInJobsURLDiscovery:
    def __init__(
        self,
        api_token: str,
        dataset_id: str = "gd_lpfll7v5hcqtkxl6l",
        sleep_interval: int = 5,
        timeout: int = 30,
    ):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }
        self.dataset_id = dataset_id
        self.sleep_interval = sleep_interval
        self.timeout = timeout

    def discover_jobs(
        self, search_urls: List[Dict[str, str]]
    ) -> Optional[List[Dict[str, Any]]]:
        try:
            start_time = time.time()
            logging.info("Discovering jobs:")

            trigger_response = self._trigger_collection(search_urls)
            if not trigger_response or "snapshot_id" not in trigger_response:
                raise ValueError("Failed to initiate job discovery")
            snapshot_id = trigger_response["snapshot_id"]
            jobs_data = None

            while True:
                status = self._check_status(snapshot_id)
                elapsed = int(time.time() - start_time)

                if status == "running":
                    logging.info(f"Status: {status} ({elapsed}s elapsed)")
                    time.sleep(self.sleep_interval)
                    continue
                elif status == "ready":
                    if jobs_data is None:
                        jobs_data = self._get_data(snapshot_id)
                        if jobs_data:
                            logging.info(f"Discovery completed after {elapsed} seconds")
                            self._save_data(jobs_data)
                            return jobs_data
                    break
                elif status in ["failed", "error"]:
                    raise RuntimeError(f"Discovery failed with status: {status}")
                time.sleep(self.sleep_interval)
        except Exception as e:
            logging.error(f"Error during job discovery: {e}")
            return None

    def _trigger_collection(
        self, search_urls: List[Dict[str, str]]
    ) -> Optional[Dict[str, Any]]:
        try:
            response = requests.post(
                f"{BRIGHTDATA_API_URL}/trigger",
                headers=self.headers,
                params={
                    "dataset_id": self.dataset_id,
                    "type": "discover_new",
                    "discover_by": "url",
                    "include_errors": "true",
                },
                json=search_urls,
                timeout=self.timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error triggering discovery: {e}")
            return None

    def _check_status(self, snapshot_id: str) -> str:
        try:
            response = requests.get(
                f"{BRIGHTDATA_API_URL}/progress/{snapshot_id}",
                headers=self.headers,
                timeout=self.timeout,
            )
            response.raise_for_status()
            return response.json().get("status", "error")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error checking status: {e}")
            return "error"

    def _get_data(self, snapshot_id: str) -> Optional[List[Dict[str, Any]]]:
        try:
            response = requests.get(
                f"{BRIGHTDATA_API_URL}/snapshot/{snapshot_id}",
                headers=self.headers,
                params={"format": "json"},
                timeout=self.timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error retrieving data: {e}")
            return None

    def _save_data(
        self,
        data: List[Dict[str, Any]],
        filename: str = "linkedin_jobs_search_url.json",
    ) -> None:
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logging.info(f"Data saved to {filename}")
            logging.info(f"Discovered {len(data)} jobs")
        except IOError as e:
            logging.error(f"Error saving data: {e}")

    def _get_timestamp(self) -> str:
        return datetime.now().strftime("%H:%M:%S")


def main() -> None:
    api_token = "<YOUR_API_TOKEN>"
    discoverer = LinkedInJobsURLDiscovery(api_token)

    search_urls = [
        {
            "url": "https://www.linkedin.com/jobs/search?keywords=Software&location=Tel%20Aviv-Yafo&geoId=101570771&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&f_TPR=r3600"
        },
    ]

    discoverer.discover_jobs(search_urls)


if __name__ == "__main__":
    main()
