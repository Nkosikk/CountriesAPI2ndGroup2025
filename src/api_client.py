import requests

class CountriesAPIClient:
    def __init__(self, base_url="https://restcountries.com/v3.1"):
        self.base_url = base_url

    def get_all_countries(self):
        """Fetches data for all countries."""
        response = requests.get(f"{self.base_url}/all")
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()