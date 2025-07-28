

class TestCountriesAPI:


    def test_get_countries(self, client):
        response = client.get("/countries")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    def test_get_country_by_code(self, client):
        response = client.get("/countries/US")
        assert response.status_code == 200
        assert response.json()["code"] == "US"

    def test_get_country_by_invalid_code(self, client):
        response = client.get("/countries/INVALID")
        assert response.status_code == 404