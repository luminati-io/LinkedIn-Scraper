import requests
import json
import time
from datetime import datetime


class LinkedInPostDiscovery:
    def __init__(self, api_token):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }
        self.dataset_id = "gd_lyy3tktm25m4avu764"

    def discover_posts(self, profile_urls):
        try:
            start_time = datetime.now()
            print(
                f"\nStarting discovery for {len(profile_urls)} profiles at {start_time.strftime('%H:%M:%S')}"
            )

            collection_response = self._trigger_discovery(profile_urls)
            if not collection_response or "snapshot_id" not in collection_response:
                raise Exception("Failed to initiate discovery")
            snapshot_id = collection_response["snapshot_id"]
            print("[OK] Discovery initiated")

            print("\nCollecting data:")
            while True:
                status = self._check_status(snapshot_id)
                current_time = datetime.now()
                elapsed = (current_time - start_time).seconds

                if status == "ready":
                    print(
                        f"\n[{current_time.strftime('%H:%M:%S')}] Discovery completed after {elapsed} seconds"
                    )
                    post_data = self._get_data(snapshot_id)
                    if post_data:
                        self._save_data(post_data)
                        break
                    else:
                        raise Exception(
                            "Failed to retrieve data after discovery completion"
                        )
                elif status in ["failed", "error"]:
                    raise Exception(f"Discovery failed with status: {status}")
                print(
                    f"[{current_time.strftime('%H:%M:%S')}] Status: {status} ({elapsed}s elapsed)",
                    end="\r",
                )
                time.sleep(5)
            return True
        except Exception as e:
            print(f"\nERROR: {str(e)}")
            return None

    def _trigger_discovery(self, profile_urls):
        try:
            print("Connecting to API...")
            response = requests.post(
                "https://api.brightdata.com/datasets/v3/trigger",
                headers=self.headers,
                params={
                    "dataset_id": self.dataset_id,
                    "type": "discover_new",
                    "discover_by": "profile_url",
                },
                json=profile_urls,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to trigger discovery: {str(e)}")
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
        except requests.exceptions.RequestException:
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
        except requests.exceptions.RequestException:
            return None

    def _save_data(self, data, filename="posts_by_profile.json"):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving data: {str(e)}")


def main():
    api_token = "<YOUR_API_TOKEN>"
    discoverer = LinkedInPostDiscovery(api_token)

    profiles = [
        {
            "url": "https://www.linkedin.com/in/luca-rossi-0aa497bb",
            "start_date": "2024-10-01T00:00:00.000Z",
            "end_date": "2024-10-09T00:00:00.000Z",
        },
        {
            "url": "https://www.linkedin.com/in/srijith-gomattam-401059214",
            "start_date": "2024-09-01T00:00:00.000Z",
            "end_date": "2024-10-01T00:00:00.000Z",
        },
        {
            "url": "https://www.linkedin.com/in/anna-clarke-0a342513",
            "start_date": "2024-10-01T00:00:00.000Z",
        },
    ]

    discoverer.discover_posts(profiles)


if __name__ == "__main__":
    main()