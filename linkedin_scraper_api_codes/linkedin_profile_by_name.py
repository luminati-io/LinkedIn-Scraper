import requests
import json
import time
from datetime import datetime
from typing import List, Dict, Optional, Any

DATASET_ID = "gd_l1viktl72bvl7bjuj0"
API_URL = "https://api.brightdata.com/datasets/v3"


class LinkedInProfileDiscovery:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }

    def discover_profiles(self, people: List[Dict[str, str]]) -> Optional[bool]:
        start_time = datetime.now()
        print(
            f"\nStarting discovery for {len(people)} profiles at {start_time.strftime('%H:%M:%S')}"
        )

        collection_response = self._trigger_discovery(people)
        if not collection_response or "snapshot_id" not in collection_response:
            print("Failed to initiate profile discovery")
            return None
        snapshot_id = collection_response["snapshot_id"]
        print("Discovery initiated")
        print("\nCollecting data:")

        while True:
            status = self._check_status(snapshot_id)
            elapsed = (datetime.now() - start_time).seconds

            print(f"\rStatus: {status} ({elapsed}s elapsed)", end="", flush=True)

            if status == "ready":
                print(f"\nDiscovery completed after {elapsed} seconds")
                profile_data = self._get_data(snapshot_id)
                if profile_data:
                    self._save_data(profile_data)
                    return True
                break
            elif status in ["failed", "error"]:
                print(f"\nDiscovery failed with status: {status}")
                return None
            time.sleep(5)

    def _trigger_discovery(
        self, people: List[Dict[str, str]]
    ) -> Optional[Dict[str, Any]]:
        try:
            print("Connecting to API...")
            response = requests.post(
                f"{API_URL}/trigger",
                headers=self.headers,
                params={
                    "dataset_id": DATASET_ID,
                    "type": "discover_new",
                    "discover_by": "name",
                },
                json=people,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to trigger discovery: {str(e)}")
            return None

    def _check_status(self, snapshot_id: str) -> str:
        try:
            response = requests.get(
                f"{API_URL}/progress/{snapshot_id}",
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
        self, data: Dict[str, Any], filename: str = "profiles_by_name.json"
    ) -> None:
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✓ Data saved to {filename}")
            print(f"✓ Discovered {len(data)} profiles")
        except Exception as e:
            print(f"Error saving data: {str(e)}")


def main() -> None:
    api_token = "<YOUR_API_TOKEN>"
    discoverer = LinkedInProfileDiscovery(api_token)

    people = [
        {"first_name": "James", "last_name": "Smith"},
        {"first_name": "Bill", "last_name": "Gates"},
    ]

    discoverer.discover_profiles(people)


if __name__ == "__main__":
    main()