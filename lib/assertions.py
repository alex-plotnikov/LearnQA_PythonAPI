import json

from requests import Response


class Assertions:

    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is on in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is on in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is on in JSON format. Response text is '{response.text}'"

        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_no_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is on in JSON format. Response text is '{response.text}'"

        for name in names:
            assert name not in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_no_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is on in JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. " \
                                             f"But it's present"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}, Actual: {response.status_code}"
