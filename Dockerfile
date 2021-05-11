FROM python:3.8-slim-buster as python

FROM python
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic --no-input