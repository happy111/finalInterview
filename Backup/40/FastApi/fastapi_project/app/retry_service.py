import requests
from tenacity import retry, wait_fixed, stop_after_attempt

class RetryService:

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def call_api(self, url):
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            raise Exception("External API failed")
        return response.json()
