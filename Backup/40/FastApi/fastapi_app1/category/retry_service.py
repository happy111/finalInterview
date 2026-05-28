import requests
from tenacity import retry, wait_fixed, stop_after_attempt

class RetryService:

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def call_api(self, url):
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            raise Exception("External API failed")
        return response.json()



import time
import requests
from category.logger import logger
from category.exceptions import ExternalAPIFailedException

def retry_request(url: str, method="GET", retries=3, delay=2):
    """Retry external API call"""

    for attempt in range(1, retries + 1):
        try:
            logger.info(f"Retry Attempt {attempt} for URL: {url}")
            response = requests.request(method, url, timeout=5)

            if response.status_code == 200:
                return response.json()

            logger.warning(
                f"Attempt {attempt} failed with status {response.status_code}"
            )

        except Exception as e:
            logger.error(f"Retry attempt {attempt} failed due to: {e}")

        time.sleep(delay)

    # After max retries → fail
    raise ExternalAPIFailedException()
