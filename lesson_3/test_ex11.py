import requests


class TestCookie:
    def test_cookie(self):
        cookie = {"HomeWork": "hw_value"}
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        assert dict(response.cookies) == cookie, "Cookie is different from the expected one"
