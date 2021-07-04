import requests
import time
import json

STATUS_NOT_READY = "Job is NOT ready"
STATUS_READY = "Job is ready"


def test_function(token=None):
    payloads = {"token": token}
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payloads)
    json_resp = json.loads(response.text)

    if not token:
        token = json_resp["token"]
        seconds = json_resp["seconds"]
        return token, seconds
    else:
        return json_resp["status"]


token, seconds = test_function()
status = test_function(token=token)
if status == STATUS_NOT_READY:
    print("Status before completeness is correct")
else:
    raise Exception("Incorrect status")
print(f"Sleep time is {seconds}")
time.sleep(seconds)
status = test_function(token=token)
if status == STATUS_READY:
    print("Status after completeness is correct")
else:
    raise Exception("Incorrect status")
