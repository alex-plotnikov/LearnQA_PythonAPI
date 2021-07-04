import requests


class TestHeaders:
    def test_headers(self):
        expected_header = "Some secret value"
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        assert "x-secret-homework-header" in response.headers, "Needed header is not in headers list"
        assert response.headers["x-secret-homework-header"] == expected_header,\
            "Headers is different from the expected one"
