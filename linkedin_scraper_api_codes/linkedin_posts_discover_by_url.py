import requests
import json
import time
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

API_URL = "https://api.brightdata.com/datasets/v3"
DATASET_ID = "gd_lyy3tktm25m4avu764"
DISCOVER_TYPE = "discover_new"
DISCOVER_BY = "url"
STATUS_READY = "ready"
STATUS_FAILED = "failed"
STATUS_ERROR = "error"
DEFAULT_FILENAME = "discovered_posts_by_url.json"


class LinkedInArticleDiscovery:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }

    def discover_articles(self, author_urls: List[Dict[str, Any]]) -> bool:
        """
        Discover articles for a list of author URLs.
        """
        start_time = datetime.now()
        logging.info(
            f"Starting discovery for {len(author_urls)} authors at {start_time.strftime('%H:%M:%S')}"
        )

        collection_response = self._trigger_discovery(author_urls)
        if not collection_response or "snapshot_id" not in collection_response:
            logging.error("Failed to initiate discovery")
            return False
        snapshot_id = collection_response["snapshot_id"]
        logging.info("Discovery initiated")

        logging.info("Collecting data:")
        while True:
            status = self._check_status(snapshot_id)
            current_time = datetime.now()
            elapsed = (current_time - start_time).seconds

            if status == STATUS_READY:
                logging.info(f"Discovery completed after {elapsed} seconds")
                article_data = self._get_data(snapshot_id)
                if article_data:
                    self._save_data(article_data)
                    return True
            elif status in [STATUS_FAILED, STATUS_ERROR]:
                logging.error(f"Discovery failed with status: {status}")
                return False
            print(f"\rStatus: {status} ({elapsed}s elapsed)", end="")
            time.sleep(5)

    def _trigger_discovery(
        self, author_urls: List[Dict[str, Any]]
    ) -> Optional[Dict[str, Any]]:
        """
        Trigger the discovery process.
        """
        try:
            logging.info("Connecting to API...")
            response = requests.post(
                f"{API_URL}/trigger",
                headers=self.headers,
                params={
                    "dataset_id": DATASET_ID,
                    "type": DISCOVER_TYPE,
                    "discover_by": DISCOVER_BY,
                },
                json=author_urls,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to trigger discovery: {str(e)}")
            return None

    def _check_status(self, snapshot_id: str) -> str:
        """
        Check the status of the discovery process.
        """
        try:
            response = requests.get(
                f"{API_URL}/progress/{snapshot_id}",
                headers=self.headers,
                timeout=30,
            )
            response.raise_for_status()
            return response.json().get("status", STATUS_ERROR)
        except requests.exceptions.RequestException:
            return STATUS_ERROR

    def _get_data(self, snapshot_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve the discovered data.
        """
        try:
            response = requests.get(
                f"{API_URL}/snapshot/{snapshot_id}",
                headers=self.headers,
                params={"format": "json"},
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

    def _save_data(
        self, data: Dict[str, Any], filename: str = DEFAULT_FILENAME
    ) -> None:
        """
        Save the discovered data to a file.
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logging.info(f"Data saved to {filename}")
        except Exception as e:
            logging.error(f"Error saving data: {str(e)}")


def main() -> None:
    api_token = "<YOUR_API_TOKEN>"
    discoverer = LinkedInArticleDiscovery(api_token)

    authors = [
        {
            "url": "https://www.linkedin.com/today/author/cristianbrunori?trk=public_post_follow-articles",
            "limit": 50,
        },
        {
            "url": "https://www.linkedin.com/today/author/stevenouri?trk=public_post_follow-articles"
        },
    ]

    discoverer.discover_articles(authors)


if __name__ == "__main__":
    main()