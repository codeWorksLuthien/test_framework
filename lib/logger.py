from datetime import datetime
import allure
import os
import logging
from requests import Response


class Logger:
    instance = None
    logger = None
    log_file_path = "requests_log.log"
    data = ""
    #current time formatted like y.m.d h:m:s
    curr_time = datetime.now().strftime("%Y.%m.%d %H:%M:%S")


    def __init__(self):
        if os.path.exists(self.log_file_path):
            os.remove(self.log_file_path)

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler(self.log_file_path)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance


    @allure.step("{method} request to {url}")
    def add_request(self, url: str, data: dict, headers: dict, cookies: dict, method: str):
        data_to_add = f"\n=================\n"
        data_to_add += f"___________________ REQUEST ___________________\n" \
                       f"{self.curr_time} Request method:  {method}\n" \
                       f"{self.curr_time} Request URL:     {url}\n" \
                       f"{self.curr_time} Request data:    {data}\n" \
                       f"{self.curr_time} Request headers: {headers}\n" \
                       f"{self.curr_time} Request cookies: {cookies}\n" \
                       f"=================\n"

        self.data += data_to_add
        self.logger.info(data_to_add)


    def add_response(self, response: Response):
        headers_as_dict = dict(response.headers)
        cookies_as_dict = dict(response.cookies)

        data_to_add = f"\n=================\n"
        data_to_add += f"___________________ RESPONSE ___________________\n" \
                       f"{self.curr_time} Response code:    {response.status_code}\n" \
                       f"{self.curr_time} Response text:    {response.text}\n" \
                       f"{self.curr_time} Response headers: {headers_as_dict}\n" \
                       f"{self.curr_time} Response cookies: {cookies_as_dict}\n" \
                       f"=================\n"

        self.data += data_to_add
        self.logger.info(data_to_add)


    def clear_data(self):
        self.data = ""


    def write_data_to_logfile(self):
        with open(self.log_file_path, 'a', encoding='utf-8') as log_file:
            log_file.write(f"TEST STARTS\n"
                           f"{self.data}\n"
                           f"TEST ENDS\n\n")
            self.clear_data()