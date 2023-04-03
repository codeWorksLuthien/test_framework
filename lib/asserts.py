import allure
import json
from requests import Response


class Asserts:
    @staticmethod
    def assert_equals(value1, value2, message: str = ""):
        assert value1 == value2, f"{value1} is not equal to {value2}. {message}"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, f"Status code is not {expected_status_code}," \
                                                             f"it's {response.status_code}"

    @staticmethod
    def assert_json_has_key(response: Response, key: str):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert key in response_as_dict, f'No such key: "{key}" in Response. JSON text is "{response.text}'

    @staticmethod
    def assert_response_has_headers(response: Response, header):
        assert header in response.headers, f'Expected header: "{header}" in Response'

    @staticmethod
    def assert_response_has_no_headers(response: Response, header):
        assert header not in response.headers, f'Expected no header named "{header}"'

    @staticmethod
    def assert_response_has_cookie(response: Response, name):
        cookies = response.cookies
        assert name in cookies, f"There's no cookie named {name}." \
                                f"Cookie list: {Asserts._make_cookie_readable(cookies)}"

    @staticmethod
    def assert_response_has_no_cookie(response: Response, name):
        cookies = response.cookies
        assert name not in cookies, f"Expected no cookie named {name}." \
                                f"Cookie list: {Asserts._make_cookie_readable(cookies)}"

    @staticmethod
    def _make_cookie_readable(cookie_jar):
        cookie_dict = cookie_jar.get_dict()
        res = ['%s=%s' % (key, value) for (key, value) in cookie_dict.items()]
        return ';'.join(res)

    @staticmethod
    def assert_response_text(response: Response, expected_text: str = ""):
        assert response.text == expected_text, f"Expected text: {expected_text}," \
                                               f"but got {response.text}"