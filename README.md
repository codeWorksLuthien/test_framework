# python-api-automation

written in
### Python 3, py.test


## Installation

1. Download [Python 3.9](https://www.python.org/downloads/)
2. Install Python from the downloaded package.
3. Clone the project, navigate to project directory from your terminal, run:
```pip3 install -r requirements.txt```

## Running the tests
To start all the final tests from a terminal, inside the project, run ```python3 -m pytest --alluredir=test_results/ framework_example/tests```

## Report
To generate the report, run ```allure serve test_results```

