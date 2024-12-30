from dataclasses import dataclass
from typing import List, Optional
import requests
from bs4 import BeautifulSoup
import time
import random
import json
from urllib.parse import quote
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


@dataclass
class JobData:
    title: str
    company: str
    location: str
    job_link: str
    posted_date: str


class ScraperConfig:
    BASE_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
    JOBS_PER_PAGE = 25
    MIN_DELAY = 2
    MAX_DELAY = 5
    RATE_LIMIT_DELAY = 30
    RATE_LIMIT_THRESHOLD = 10

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Cache-Control": "no-cache",
    }


class LinkedInJobsScraper:
    def __init__(self):
        self.session = self._setup_session()

    def _setup_session(self) -> requests.Session:
        session = requests.Session()
        retries = Retry(
            total=5, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504]
        )
        session.mount("https://", HTTPAdapter(max_retries=retries))
        return session

    def _build_search_url(self, keywords: str, location: str, start: int = 0) -> str:
        params = {
            "keywords": keywords,
            "location": location,
            "start": start,
        }
        return f"{ScraperConfig.BASE_URL}?{'&'.join(f'{k}={quote(str(v))}' for k, v in params.items())}"

    def _clean_job_url(self, url: str) -> str:
        return url.split("?")[0] if "?" in url else url

    def _extract_job_data(self, job_card: BeautifulSoup) -> Optional[JobData]:
        try:
            title = job_card.find("h3", class_="base-search-card__title").text.strip()
            company = job_card.find(
                "h4", class_="base-search-card__subtitle"
            ).text.strip()
            location = job_card.find(
                "span", class_="job-search-card__location"
            ).text.strip()
            job_link = self._clean_job_url(
                job_card.find("a", class_="base-card__full-link")["href"]
            )
            posted_date = job_card.find("time", class_="job-search-card__listdate")
            posted_date = posted_date.text.strip() if posted_date else "N/A"

            return JobData(
                title=title,
                company=company,
                location=location,
                job_link=job_link,
                posted_date=posted_date,
            )
        except Exception as e:
            print(f"Failed to extract job data: {str(e)}")
            return None

    def _fetch_job_page(self, url: str) -> BeautifulSoup:
        try:
            response = self.session.get(url, headers=ScraperConfig.HEADERS)
            if response.status_code != 200:
                raise RuntimeError(
                    f"Failed to fetch data: Status code {response.status_code}"
                )
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            raise RuntimeError(f"Request failed: {str(e)}")

    def scrape_jobs(
        self, keywords: str, location: str, max_jobs: int = 100
    ) -> List[JobData]:
        all_jobs = []
        start = 0

        while len(all_jobs) < max_jobs:
            try:
                url = self._build_search_url(keywords, location, start)
                soup = self._fetch_job_page(url)
                job_cards = soup.find_all("div", class_="base-card")

                if not job_cards:
                    break
                for card in job_cards:
                    job_data = self._extract_job_data(card)
                    if job_data:
                        all_jobs.append(job_data)
                        if len(all_jobs) >= max_jobs:
                            break
                print(f"Scraped {len(all_jobs)} jobs...")
                start += ScraperConfig.JOBS_PER_PAGE
                time.sleep(
                    random.uniform(ScraperConfig.MIN_DELAY, ScraperConfig.MAX_DELAY)
                )
            except Exception as e:
                print(f"Scraping error: {str(e)}")
                break
        return all_jobs[:max_jobs]

    def save_results(
        self, jobs: List[JobData], filename: str = "linkedin_jobs.json"
    ) -> None:
        if not jobs:
            return
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([vars(job) for job in jobs], f, indent=2, ensure_ascii=False)
        print(f"Saved {len(jobs)} jobs to {filename}")


def main():
    params = {"keywords": "AI/ML Engineer", "location": "London", "max_jobs": 100}

    scraper = LinkedInJobsScraper()
    jobs = scraper.scrape_jobs(**params)
    scraper.save_results(jobs)


if __name__ == "__main__":
    main()