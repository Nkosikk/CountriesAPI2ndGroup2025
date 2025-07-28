
import pytest

from src.api_client import CountriesAPIClient


@pytest.fixture(scope="module")
def api_client():
    """
       Provides a shared instance of the CountriesAPIClient for all tests in a module.
       The 'module' scope ensures the client is initialized once per test file.
       """
    return CountriesAPIClient()

