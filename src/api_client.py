import requests

class CountriesAPIClient:
    def __init__(self, base_url="https://restcountries.com"):
        self.base_url = base_url

    def get_all_countries(self):
        """Fetches data for all countries."""
        response = requests.get(f"{self.base_url}/v3.1/currency/zar")
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()