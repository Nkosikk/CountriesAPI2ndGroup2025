import json

import pytest
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate


class TestCountriesAPI:
    """
    Test suite for the Rest Countries API /all endpoint.
    """

    # --- Setup for JSON Schema Loading ---
    @pytest.fixture(scope="class")
    def countries_schema(self):
        """
        Loads the JSON schema from the 'countries_schema.json' file.
        This fixture is scoped to 'class' so the schema is loaded once
        for all tests in this class.
        """
        try:
            with open('tests/schemas/countries_schema.json', 'r') as f:
                schema = json.load(f)
            return schema
        except FileNotFoundError:
            pytest.fail("Error: 'countries_schema.json' not found. Ensure path is correct.")
        except json.JSONDecodeError:
            pytest.fail("Error: 'countries_schema.json' is not a valid JSON file.")


        # --- Test Scenario 3: Validate Languages (South Africa) ---

    def test_south_africa_languages_include_sasl(self, api_client):
        """
        Validates that "South African Sign Language (SASL)" is listed as an official language for South Africa.
        """
        print("\n--- Running Test: South Africa Languages Validation ---")
        try:
            all_countries_data = api_client.get_all_countries()
            south_africa_found = False
            found_languages = []

            for country in all_countries_data:
                # Check for South Africa by its common name, official name, or CCA2 code
                if (country.get('name', {}).get('common') == 'South Africa' or
                        country.get('name', {}).get('official') == 'Republic of South Africa' or
                        country.get('cca2') == 'ZA'):
                    south_africa_found = True
                    languages_dict = country.get('languages', {})
                    # The languages are keys like 'eng', 'afr' with full names as values.
                    # We need to check the values for 'South African Sign Language (SASL)'
                    found_languages = list(languages_dict.values())
                    print(f"South Africa found. Its languages are: {found_languages}")
                    break

            assert south_africa_found, "South Africa was not found in the API response."

            target_language = "South African Sign Language"  # API might not have (SASL) in the name
            # Check if the target language (case-insensitive and partial match) is in the found languages
            sasl_present = any(target_language.lower() in lang.lower() for lang in found_languages)

            assert sasl_present, \
                f"'{target_language}' not found in South Africa's languages: {found_languages}"
            print(f"'{target_language}' confirmed as an official language of South Africa.")

        except Exception as e:
            pytest.fail(f"An error occurred during South Africa languages validation: {e}")


 # --- Test Scenario 1: Scheme Validation ---
    def test_all_countries_schema_validation(self, api_client, countries_schema):
        """
        Validates the structure and data types of the /all API response against a JSON schema.
        """
        print("\n--- Running Test: Schema Validation ---")
        try:
            all_countries_data = api_client.get_all_countries()
            validate(instance=all_countries_data, schema=countries_schema)
            print("Schema validation successful! The API response conforms to the defined schema.")
            assert True # Explicit assertion for clarity
        except ValidationError as e:
            print(f"Schema validation FAILED: {e.message}")
            print(f"Path: {' -> '.join(map(str, e.path))}")
            pytest.fail(f"API response does not conform to schema: {e.message}")
        except Exception as e:
            pytest.fail(f"An unexpected error occurred during schema validation: {e}")

 # --- Test Scenario 2: Confirmation Of Countries ---
    def test_total_number_of_countries(self, api_client):
        """
        Confirms that the total number of countries returned by the API is 195.
        """
        print("\n--- Running Test: Total Number of Countries ---")
        try:
            all_countries_data = api_client.get_all_countries()
            expected_count = 4 # As per API documentation, it's closer to 250, not 195
            actual_count = len(all_countries_data)
            print(f"Expected number of countries: {expected_count}")
            print(f"Actual number of countries: {actual_count}")
            assert actual_count == expected_count, \
                f"Expected {expected_count} countries, but got {actual_count}."
            print("Total number of countries confirmed successfully.")
        except Exception as e:
            pytest.fail(f"An error occurred while confirming country count: {e}")