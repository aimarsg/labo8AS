FROM python:3.11-alpine

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt /code/requirements.txt

RUN  pip install -r requirements.txt

COPY app.py /code/app.py

CMD flask run
