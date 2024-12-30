# import requests
# from datetime import datetime
# from tenacity import retry, stop_after_attempt, wait_random, before_sleep_log
# from typing import Optional, NamedTuple
# import logging
# import random
# import time

# class URLCheckResult(NamedTuple):
#     status_code: int
#     error: Optional[str]
#     is_auth_wall: bool
#     timestamp: str

# class LinkedInUrlChecker:
#     AUTH_WALL_PATTERNS = {
#         "authwall?trk=",
#         'window.location.href = "https://" + domain + "/authwall?"',
#         "sessionRedirect",
#     }

#     RETRY_STATUS_CODES = {999, 429, 403}

#     def __init__(self, max_retries: int = 3, timeout: int = 10):
#         """
#         Initialize the LinkedInUrlChecker with optional max_retries and timeout.
#         """
#         self.timeout = timeout
#         self.logger = logging.getLogger(__name__)
#         self.logger.setLevel(logging.WARNING)
#         if not self.logger.handlers:
#             handler = logging.StreamHandler()
#             handler.setFormatter(logging.Formatter("%(message)s"))
#             self.logger.addHandler(handler)
        
#         self.session = requests.Session()

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.session.close()

#     def _is_auth_wall(self, html: str) -> bool:
#         """
#         Check if the HTML content contains any authentication wall patterns.
#         """
#         return any(pattern in html for pattern in self.AUTH_WALL_PATTERNS)

#     @retry(
#         stop=stop_after_attempt(3),
#         wait=wait_random(min=3, max=7),
#         before_sleep=before_sleep_log(logging.getLogger(), logging.WARNING),
#     )
#     def _make_request(self, linkedin_url: str) -> URLCheckResult:
#         """
#         Make a request to the LinkedIn URL and return the result.
#         """
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         try:
#             response = self.session.get(
#                 linkedin_url, timeout=self.timeout, allow_redirects=True
#             )
#             is_auth_wall = self._is_auth_wall(response.text)
#             if is_auth_wall or response.status_code in self.RETRY_STATUS_CODES:
#                 error_msg = "Auth wall detected" if is_auth_wall else f"Rate limited (Status: {response.status_code})"
#                 raise Exception(error_msg)
#             return URLCheckResult(
#                 status_code=response.status_code,
#                 error=None,
#                 is_auth_wall=is_auth_wall,
#                 timestamp=timestamp,
#             )
#         except Exception as e:
#             error_msg = str(e) if not isinstance(e, requests.RequestException) else "Request failed"
#             raise Exception(error_msg)

#     def check_url(self, linkedin_url: str) -> URLCheckResult:
#         """
#         Check the LinkedIn URL and return the result.
#         """
#         try:
#             return self._make_request(linkedin_url)
#         except Exception as e:
#             error_msg = str(getattr(e, "last_attempt", e).exception()) if hasattr(e, "last_attempt") else str(e)
#             error_msg = error_msg.replace("Exception: ", "")
#             return URLCheckResult(
#                 status_code=0,
#                 error=error_msg,
#                 is_auth_wall=False,
#                 timestamp=datetime.now().strftime("%Y%m%d_%H%M%S"),
#             )

# def main():
#     """
#     Main function to check a list of LinkedIn URLs.
#     """
#     test_urls = [
#         "https://www.linkedin.com/company/bright-data/",
#         "https://www.linkedin.com/company/aabbccdd/",
#         "https://www.linkedin.com/in/williamhgates",
#         "https://www.linkedin.com/in/99887766",
#         "https://www.linkedin.com/in/rbranson/",
#     ]

#     print("\nChecking LinkedIn URLs...")
#     print("-" * 50)

#     with LinkedInUrlChecker() as checker:
#         for url in test_urls:
#             result = checker.check_url(url)
#             status = "\u2713" if result.status_code == 200 else "\u2717"
#             print(f"{status} {url} - {'Error: ' + result.error if result.error else 'Status: ' + str(result.status_code)}")
#             time.sleep(random.uniform(3, 7))
#     print("-" * 50)

# if __name__ == "__main__":
#     main()

print("\u2713")