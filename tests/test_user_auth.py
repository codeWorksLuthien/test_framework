import pytest
from http import HTTPStatus
from lib.base_case import BaseCase
from lib.asserts import Asserts
from lib.my_requests import MyRequest as Request


class TestCreateUser(BaseCase):
    auth_sid = "auth_sid"
    x_csrf_token = "x-csrf-token"

    def test_auth_positive(self):
        data = {
            "email": "ivanov@mail.com",
            "password": "123456"
        }

        response = Request.post("/user/login", data)
        Asserts.assert_status_code(response, HTTPStatus.OK)
        Asserts.assert_response_has_cookie(response, self.auth_sid)
        Asserts.assert_response_has_headers(response, self.x_csrf_token)


    @pytest.mark.parametrize("test_mail, test_pass", [
        ("ivanov@mail.com", "123"),
        ("ivanov@mail.com", ""),
        ("", "123"),
        ("", ""),
        ("ivanovmail.com", "123"),
    ])
    def test_auth_negative(self, test_mail, test_pass):
        data = {
            "email": test_mail,
            "password": test_pass
        }

        response = Request.post("/user/login", data)
        Asserts.assert_status_code(response, HTTPStatus.BAD_REQUEST)
        Asserts.assert_response_text(response, "Invalid username/password supplied")
        Asserts.assert_response_has_no_cookie(response, self.auth_sid)
        Asserts.assert_response_has_no_headers(response, self.x_csrf_token)