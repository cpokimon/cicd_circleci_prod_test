FROM python:3.6

WORKDIR /usr/app

COPY ./service/requirements.txt .

RUN pip install -r requirements.txt

COPY ./service .