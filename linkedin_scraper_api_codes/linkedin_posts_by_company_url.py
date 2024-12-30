import requests
import json
import time
import logging
import os
from datetime import datetime
from typing import List, Dict, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LinkedInPostsCollector:
    def __init__(self, api_token: str, dataset_id: str = "gd_lyy3tktm25m4avu764", sleep_interval: int = 5, timeout: int = 30):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }
        self.dataset_id = dataset_id
        self.sleep_interval = sleep_interval
        self.timeout = timeout

    def collect_posts(self, company_data: List[Dict[str, Any]]) -> Optional[List[Dict[str, Any]]]:
        try:
            start_time = time.time()
            logging.info("Collecting posts:")
            
            trigger_response = self._trigger_collection(company_data)
            if not trigger_response or 'snapshot_id' not in trigger_response:
                raise Exception("Failed to initiate data collection")
                
            snapshot_id = trigger_response['snapshot_id']
            posts_data = None

            while True:
                status = self._check_status(snapshot_id)
                elapsed = int(time.time() - start_time)
                
                if status == "running":
                    logging.info(f"Status: {status} ({elapsed}s elapsed)")
                    time.sleep(self.sleep_interval)
                    continue
                    
                elif status == "ready":
                    if posts_data is None:
                        posts_data = self._get_data(snapshot_id)
                        if posts_data:
                            logging.info(f"Collection completed after {elapsed} seconds")
                            self._save_data(posts_data)
                            return posts_data
                    break
                    
                elif status in ["failed", "error"]:
                    raise Exception(f"Collection failed with status: {status}")
                
                time.sleep(self.sleep_interval)

        except Exception as e:
            logging.error(f"Error during collection: {str(e)}")
            return None

    def _trigger_collection(self, company_data: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        try:
            response = requests.post(
                "https://api.brightdata.com/datasets/v3/trigger",
                headers=self.headers,
                params={
                    "dataset_id": self.dataset_id,
                    "type": "discover_new",
                    "discover_by": "company_url",
                    "include_errors": "true"
                },
                json=company_data,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error triggering collection: {str(e)}")
            return None

    def _check_status(self, snapshot_id: str) -> str:
        try:
            response = requests.get(
                f"https://api.brightdata.com/datasets/v3/progress/{snapshot_id}",
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json().get("status", "error")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error checking status: {str(e)}")
            return "error"

    def _get_data(self, snapshot_id: str) -> Optional[List[Dict[str, Any]]]:
        try:
            response = requests.get(
                f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}",
                headers=self.headers,
                params={"format": "json"},
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error retrieving data: {str(e)}")
            return None

    def _save_data(self, data: List[Dict[str, Any]], filename: str = "linkedin_posts_company_url.json") -> None:
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logging.info(f"Data saved to {filename}")
            logging.info(f"Collected {len(data)} posts")
        except Exception as e:
            logging.error(f"Error saving data: {str(e)}")

    def _get_timestamp(self) -> str:
        return datetime.now().strftime("%H:%M:%S")

def main() -> None:
    api_token = os.getenv("API_TOKEN")
    if not api_token:
        logging.error("API token not found. Please set the API_TOKEN environment variable.")
        return

    collector = LinkedInPostsCollector(api_token)

    companies = [
        {
            "url": "https://www.linkedin.com/company/lanieri",
        }
    ]

    collector.collect_posts(companies)

if __name__ == "__main__":
    main()