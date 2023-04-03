from datetime import datetime
from requests import Response
#from lib.logger import Logger

class BaseCase:
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    # def teardown(self):
    #     Logger.get_instance().write_data_to_logfile()

    @staticmethod
    def get_cookie(response: Response, cookie_name):
        if cookie_name in response.cookies:
            return {cookie_name: response.cookies[cookie_name]}
        else:
            raise Exception(f"No cookie named {cookie_name}")

    @staticmethod
    def get_header(response: Response, headers_name):
        if headers_name in response.headers:
            return {headers_name: response.headers[headers_name]}
        else:
            raise Exception(f"No header named {headers_name}")

    def create_email(self, base: str, domain="test.com"):
        return f'{base}.{self.time}@{domain}'