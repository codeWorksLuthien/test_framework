import os

class Environment:
    TEST = 'test'
    PROD = 'prod'

    URLS = {
        TEST: 'https://playground.learnqa.ru/api',
        PROD: 'https://rc.playground.learnqa.du/api'
    }

    def __init__(self):
        self.name = self._get_environment_variable()

    @classmethod
    def _get_environment_variable(cls) -> str:
        try:
            return os.environ['ENVIRONMENT']
        except KeyError:
            return cls.TEST

    def base_url(self) -> str:
        return self.URLS[self.name]

ENV = Environment()