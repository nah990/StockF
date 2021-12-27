FROM python:3.9.5-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /django
RUN apk update \
    apk add --update --no-cache g++ gcc libxslt-dev && \
    apk add --no-cache openssl-dev libffi-dev && \
    apk add postgresql-dev gcc python3-dev musl-dev && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /django/entrypoint.sh
RUN chmod +x /django/entrypoint.sh

COPY . .
RUN python manage.py collectstatic --noinput
ENTRYPOINT ["/django/entrypoint.sh"]