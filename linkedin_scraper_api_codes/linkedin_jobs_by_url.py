import requests
import json
import time
from datetime import datetime
from typing import List, Dict, Optional, Any


class LinkedInJobsCollector:
    def __init__(self, api_token: str, dataset_id: str):
        """
        Initialize the LinkedInJobsCollector with API token and dataset ID.
        """
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }
        self.dataset_id = dataset_id

    def collect_jobs(
        self, job_urls: List[Dict[str, str]]
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Collect job data from LinkedIn using the provided job URLs.
        """
        try:
            start_time = time.time()
            print("\nCollecting data:")

            trigger_response = self._trigger_collection(job_urls)
            if not trigger_response or "snapshot_id" not in trigger_response:
                raise ValueError("Failed to initiate data collection")
            snapshot_id = trigger_response["snapshot_id"]
            jobs_data = None

            while True:
                status = self._check_status(snapshot_id)
                elapsed = int(time.time() - start_time)

                if status == "running":
                    print(
                        f"\r[{self._get_timestamp()}] Status: {status} ({elapsed}s elapsed)",
                        end="",
                        flush=True,
                    )
                    time.sleep(5)
                    continue
                elif status == "ready":
                    if jobs_data is None:
                        jobs_data = self._get_data(snapshot_id)
                        if jobs_data:
                            print(
                                f"\r[{self._get_timestamp()}] Collection completed after {elapsed} seconds\n"
                            )
                            self._save_data(jobs_data)
                            return jobs_data
                    break
                elif status in ["failed", "error"]:
                    raise RuntimeError(f"Collection failed with status: {status}")
                time.sleep(5)
        except (ValueError, RuntimeError, Exception) as e:
            print(f"Error during collection: {str(e)}")
            return None

    def _trigger_collection(
        self, job_urls: List[Dict[str, str]]
    ) -> Optional[Dict[str, Any]]:
        """
        Trigger the data collection process.
        """
        try:
            response = requests.post(
                "https://api.brightdata.com/datasets/v3/trigger",
                headers=self.headers,
                params={"dataset_id": self.dataset_id, "include_errors": "true"},
                json=job_urls,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error triggering collection: {str(e)}")
            return None

    def _check_status(self, snapshot_id: str) -> str:
        """
        Check the status of the data collection process.
        """
        try:
            response = requests.get(
                f"https://api.brightdata.com/datasets/v3/progress/{snapshot_id}",
                headers=self.headers,
                timeout=30,
            )
            response.raise_for_status()
            return response.json().get("status", "error")
        except requests.exceptions.RequestException:
            return "error"

    def _get_data(self, snapshot_id: str) -> Optional[List[Dict[str, Any]]]:
        """
        Retrieve the collected data.
        """
        try:
            response = requests.get(
                f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}",
                headers=self.headers,
                params={"format": "json"},
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving data: {str(e)}")
            return None

    def _save_data(
        self, data: List[Dict[str, Any]], filename: str = "linkedin_jobs_url.json"
    ) -> None:
        """
        Save the collected data to a JSON file.
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✓ Data saved to {filename}")
            print(f"✓ Collected {len(data)} job listings")
        except Exception as e:
            print(f"Error saving data: {str(e)}")

    def _get_timestamp(self) -> str:
        """
        Get the current timestamp.
        """
        return datetime.now().strftime("%H:%M:%S")


def main() -> None:
    api_token = "<YOUR_API_TOKEN>"
    dataset_id = "gd_lpfll7v5hcqtkxl6l"
    collector = LinkedInJobsCollector(api_token, dataset_id)

    job_searches = [
        {"url": "https://www.linkedin.com/jobs/view/4073552631"},
        {"url": "https://www.linkedin.com/jobs/view/4073729630"},
    ]

    collector.collect_jobs(job_searches)


if __name__ == "__main__":
    main()
