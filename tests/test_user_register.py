import pytest
import string
import random

from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):

    def test_crete_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

    def test_create_user_with_incorrect_email(self):
        incorrect_email = 'incorrect_email_example.com'
        data = self.prepare_registration_data(incorrect_email)
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        proper_content = "Invalid email format"
        assert response.content.decode("utf-8") == proper_content,\
            f"Unexpected response content {response.content}, should be {proper_content}"

    EXCLUDE_PARAMETERS = [
        "password",
        "username",
        "firstName",
        "lastName",
        "email"
    ]

    @pytest.mark.parametrize('condition', EXCLUDE_PARAMETERS)
    def test_negative_create_user_without_parameter(self, condition):
        data = self.prepare_registration_data()
        data.pop(condition)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == \
               f"The following required params are missed: {condition}", \
               f"Unexpected response content {response.content}"

    def test_negative_create_user_with_very_small_name(self):
        data = self.prepare_registration_data()
        data['firstName'] = 'S'

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == \
               f"The value of 'firstName' field is too short", \
               f"Unexpected response content {response.content}"

    def test_negative_create_user_with_very_large_name(self):
        data = self.prepare_registration_data()
        letters = string.ascii_letters
        long_name = ''.join(random.choice(letters) for i in range(251))
        data['firstName'] = long_name

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == \
               f"The value of 'firstName' field is too long", \
               f"Unexpected response content {response.content}"
