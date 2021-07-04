import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
redirect_count = len(response.history)

print(f"Count of redirections is {redirect_count}")
print(f"Last url is {response.url}")
