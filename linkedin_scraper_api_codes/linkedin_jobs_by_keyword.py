import requests
import json
import time
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class LinkedInJobsDiscovery:
    def __init__(self, api_token):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }
        self.dataset_id = "gd_lpfll7v5hcqtkxl6l"

    def discover_jobs(self, search_criteria):
        try:
            start_time = time.time()
            logging.info("Discovering jobs")

            trigger_response = self._trigger_collection(search_criteria)
            if not trigger_response or "snapshot_id" not in trigger_response:
                raise Exception("Failed to initiate job discovery")
            snapshot_id = trigger_response["snapshot_id"]
            jobs_data = None

            while True:
                status = self._check_status(snapshot_id)
                elapsed = int(time.time() - start_time)

                if status == "running":
                    logging.info(f"Status: {status} ({elapsed}s elapsed)")
                    time.sleep(5)
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
                    raise Exception(f"Discovery failed with status: {status}")
                time.sleep(5)
        except Exception as e:
            logging.error(f"Error during job discovery: {str(e)}")
            return None

    def _trigger_collection(self, search_criteria):
        try:
            response = requests.post(
                "https://api.brightdata.com/datasets/v3/trigger",
                headers=self.headers,
                params={
                    "dataset_id": self.dataset_id,
                    "type": "discover_new",
                    "discover_by": "keyword",
                    "include_errors": "true",
                },
                json=search_criteria,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error triggering discovery: {str(e)}")
            return None

    def _check_status(self, snapshot_id):
        try:
            response = requests.get(
                f"https://api.brightdata.com/datasets/v3/progress/{snapshot_id}",
                headers=self.headers,
                timeout=30,
            )
            response.raise_for_status()
            return response.json().get("status")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error checking status: {str(e)}")
            return "error"

    def _get_data(self, snapshot_id):
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
            logging.error(f"Error retrieving data: {str(e)}")
            return None

    def _save_data(self, data, filename="linkedin_jobs_keyword.json"):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logging.info(f"Data saved to {filename}")
            logging.info(f"Discovered {len(data)} jobs")
        except Exception as e:
            logging.error(f"Error saving data: {str(e)}")

    def _get_timestamp(self):
        return datetime.now().strftime("%H:%M:%S")


def main():
    api_token = "<YOUR_API_TOKEN>"
    discoverer = LinkedInJobsDiscovery(api_token)

    search_criteria = [
        {
            "location": "New York",
            "keyword": "data analyst",
            "country": "US",
            "time_range": "Any time",
            "job_type": "Part-time",
            "experience_level": "Entry level",
            "remote": "Remote",
            "company": "",
        },
    ]

    discoverer.discover_jobs(search_criteria)


if __name__ == "__main__":
    main()
