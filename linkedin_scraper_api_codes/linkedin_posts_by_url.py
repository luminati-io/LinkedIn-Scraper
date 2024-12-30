import requests
import json
import time
from datetime import datetime


class LinkedInPostCollector:
    def __init__(self, api_token):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }
        self.dataset_id = "gd_lyy3tktm25m4avu764"

    def collect_posts(self, post_urls):
        start_time = datetime.now()
        print(
            f"\nStarting collection for {len(post_urls)} posts at {start_time.strftime('%H:%M:%S')}"
        )

        collection_response = self._trigger_collection(post_urls)
        if not collection_response or "snapshot_id" not in collection_response:
            print("Failed to initiate collection")
            return None
        snapshot_id = collection_response["snapshot_id"]
        print("[OK] Collection initiated")

        print("\nCollecting data:")
        while True:
            status = self._check_status(snapshot_id)
            current_time = datetime.now()
            elapsed = (current_time - start_time).seconds

            if status == "ready":
                print(
                    f"\n[{current_time.strftime('%H:%M:%S')}] Collection completed after {elapsed} seconds"
                )
                post_data = self._get_data(snapshot_id)
                if post_data:
                    self._save_data(post_data)
                    return True
            elif status in ["failed", "error"]:
                print(f"Collection failed with status: {status}")
                return None
            print(
                f"[{current_time.strftime('%H:%M:%S')}] Status: {status} ({elapsed}s elapsed)",
                end="\r",
            )
            time.sleep(5)

    def _trigger_collection(self, post_urls):
        print("Connecting to API...")
        try:
            response = requests.post(
                "https://api.brightdata.com/datasets/v3/trigger",
                headers=self.headers,
                params={"dataset_id": self.dataset_id},
                json=post_urls,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to trigger collection: {str(e)}")
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

    def _save_data(self, data, filename="linkedin_posts_url.json"):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving data: {str(e)}")


def main():
    api_token = "<YOUR_API_TOKEN>"
    collector = LinkedInPostCollector(api_token)

    posts = [
        {
            "url": "https://www.linkedin.com/pulse/ab-test-optimisation-earlier-decisions-new-readout-de-b%C3%A9naz%C3%A9?trk=public_profile_article_view"
        },
        {
            "url": "https://www.linkedin.com/posts/orlenchner_scrapecon-activity-7180537307521769472-oSYN?trk=public_profile"
        },
        {
            "url": "https://www.linkedin.com/posts/karin-dodis_web-data-collection-for-businesses-bright-activity-7176601589682434049-Aakz?trk=public_profile"
        },
        {
            "url": "https://www.linkedin.com/pulse/getting-value-out-sunburst-guillaume-de-b%C3%A9naz%C3%A9?trk=public_profile_article_view"
        },
    ]

    collector.collect_posts(posts)


if __name__ == "__main__":
    main()