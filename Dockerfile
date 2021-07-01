FROM python:3.8-slim-buster as python

FROM python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=nobody . /usr/src/app
WORKDIR /usr/src/app
USER nobody
RUN mkdir log
RUN python manage.py collectstatic --no-input

# ssh
RUN apk add openssh \
     && echo "root:Docker!" | chpasswd 
COPY sshd_config /etc/ssh/

EXPOSE 8000 2222
