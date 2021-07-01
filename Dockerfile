FROM python:3.8-slim-buster as python

FROM python
COPY requirements.txt .
COPY sshd_config /etc/ssh/

RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=nobody . /usr/src/app
WORKDIR /usr/src/app
USER nobody
RUN mkdir log
RUN python manage.py collectstatic --no-input

# ssh
ENV SSH_PASSWD "root:Docker!"
RUN apt-get update
RUN apt-get install -y --no-install-recommends dialog
RUN apt-get update
RUN apt-get install -y --no-install-recommends openssh-server
RUN echo "$SSH_PASSWD" | chpasswd 

EXPOSE 8000 2222
