# docker image rm pytest_check
# docker image ls

# docker build -t pytest_check .
# docker run --rm --mount type=bind,src=D:\my_codeworks\playGround6,target=/tests/ pytest_check python -m pytest -s --alluredir=test_results/ tests/

FROM python

WORKDIR /tests

COPY . .

RUN pip install -r requirements.txt

ENV ENVIRONMENT=test

CMD python -m pytest -s --alluredir=test_results/ /tests/