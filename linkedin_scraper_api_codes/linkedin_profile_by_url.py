import requests
import json
import time
from datetime import datetime
from typing import List, Dict, Optional, Any


class LinkedInProfileInfo:
    def __init__(self, api_token: str, dataset_id: str = "gd_l1viktl72bvl7bjuj0"):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }
        self.dataset_id = dataset_id

    def collect_profile_info(
        self, profile_urls: List[Dict[str, str]]
    ) -> Optional[bool]:
        try:
            start_time = datetime.now()
            print(
                f"\nStarting collection for {len(profile_urls)} profiles at {start_time.strftime('%H:%M:%S')}"
            )

            collection_response = self._trigger_collection(profile_urls)
            if not collection_response or "snapshot_id" not in collection_response:
                raise ValueError("Failed to initiate data collection")
            snapshot_id = collection_response["snapshot_id"]
            print("\nCollecting data:")

            while True:
                status = self._check_status(snapshot_id)
                elapsed = (datetime.now() - start_time).seconds

                print(f"\rStatus: {status} ({elapsed}s elapsed)", end="", flush=True)

                if status == "ready":
                    print(f"\nCollection completed after {elapsed} seconds")
                    profile_data = self._get_data(snapshot_id)
                    if profile_data:
                        self._save_data(profile_data)
                        print(f"✓ Collected {len(profile_data)} profiles")
                        return True
                    break
                elif status in ["failed", "error"]:
                    print(f"\nCollection failed with status: {status}")
                    return None
                time.sleep(5)
        except Exception as e:
            print(f"\nERROR: {str(e)}")
            return None

    def _trigger_collection(
        self, profile_urls: List[Dict[str, str]]
    ) -> Optional[Dict[str, Any]]:
        try:
            print("Connecting to API...")
            response = requests.post(
                "https://api.brightdata.com/datasets/v3/trigger",
                headers=self.headers,
                params={"dataset_id": self.dataset_id},
                json=profile_urls,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to trigger collection: {str(e)}")
            return None

    def _check_status(self, snapshot_id: str) -> str:
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

    def _get_data(self, snapshot_id: str) -> Optional[Dict[str, Any]]:
        try:
            response = requests.get(
                f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}",
                headers=self.headers,
                params={"format": "json"},
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

    def _save_data(
        self, data: Dict[str, Any], filename: str = "profiles_by_url.json"
    ) -> None:
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✓ Data saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {str(e)}")


def main():
    api_token = "<YOUR_API_TOKEN>"
    collector = LinkedInProfileInfo(api_token)

    profiles = [
        {"url": "https://www.linkedin.com/in/williamhgates"},
        {"url": "https://www.linkedin.com/in/rbranson/"},
        {"url": "https://www.linkedin.com/in/justinwelsh/"},
        {"url": "https://www.linkedin.com/in/simonsinek/"},
    ]

    collector.collect_profile_info(profiles)


if __name__ == "__main__":
    main()