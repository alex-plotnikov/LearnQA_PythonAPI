from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserDelete(BaseCase):

    def test_delete_static_user(self):
        # Login
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # Delete
        response2 = MyRequests.delete(
            f"/user/{2}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_status_code(response2, 400)
        assert response2.content.decode("utf-8") == \
               f"Please, do not delete test users with ID 1, 2, 3, 4 or 5.", \
               f"Unexpected response content {response2.content}"

    def test_delete_just_created_user(self):
        #Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Delete
        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_status_code(response3, 200)

        # Login again
        login_data = {
            'email': email,
            'password': password
        }
        response4 = MyRequests.post("/user/login", data=login_data)

        Assertions.assert_status_code(response4, 400)
        assert response4.content.decode("utf-8") == \
               f"Invalid username/password supplied", \
               f"Unexpected response content {response2.content}"

    def test_delete_user_auth_as_another_user(self):
        # Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Delete
        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_status_code(response3, 400)
        assert response3.content.decode("utf-8") == \
               f"Please, do not delete test users with ID 1, 2, 3, 4 or 5.", \
               f"Unexpected response content {response3.content}"
