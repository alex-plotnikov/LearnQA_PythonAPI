import random
import requests

TEST_URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"

http_request_types = ["GET", "POST", "PUT", "DELETE"]

# Any request without parameter
request_method = random.choice(http_request_types)
random_response = requests.request(method=request_method, url=f"{TEST_URL}")
print(f"Request method is: {request_method}")
print(f"Text is the following: {random_response.text}")
print(f"Status code is: {random_response.status_code}")

# Request out of list
head_response = requests.head(f"{TEST_URL}")
print(f"Text is the following: {head_response.text}")
print(f"Status code is: {head_response.status_code}")


# Correct request with parameter
for request_method in http_request_types:
    payload = {"method": f"{request_method}"}
    if request_method == "GET":
        response = requests.request(method=request_method, url=f"{TEST_URL}", params=payload)
    else:
        response = requests.request(method=request_method, url=f"{TEST_URL}", data=payload)
    print(f"Request method is: {request_method}")
    print(f"Text is the following: {response.text}")
    print(f"Status code is: {response.status_code}")

# All possible variations
for request_method in http_request_types:
    for method_in_payload in http_request_types:
        payload = {"method": f"{method_in_payload}"}
        if request_method == "GET":
            response = requests.request(method=request_method, url=f"{TEST_URL}", params=payload)
        else:
            response = requests.request(method=request_method, url=f"{TEST_URL}", data=payload)
        print(f"Request method is: {request_method} and {method_in_payload}")
        print(f"Text is the following: {response.text}")
        print(f"Status code is: {response.status_code}")

