
def test_if_south_africa_has_sasl():
    response = requests.get("https://restcountries.com/v3.1/name/south%20africa")
    assert response.status_code == 200

    country = response.json()[0]
    languages = country.get("languages", {})
    language_values = list(languages.values())

    print(f"\n📘 South Africa's languages: {language_values}")

    sasl_found = any("sign" in lang.lower() or "sasl" in lang.lower() for lang in language_values)
    assert sasl_found, "South African Sign Language (SASL) not found in language list"