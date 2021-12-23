FROM python:3.9.5-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /django
RUN apk add --update --no-cache g++ gcc libxslt-dev && \
    apk add --no-cache openssl-dev libffi-dev && \
    apk add postgresql-dev gcc python3-dev musl-dev && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
