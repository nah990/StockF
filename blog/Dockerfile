FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /blog
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .