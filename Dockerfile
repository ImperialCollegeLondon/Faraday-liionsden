FROM python:3.8-slim-buster as python

FROM python

# ssh
COPY install_ssh.sh .
RUN chmod u+x install_ssh.sh
RUN ./install_ssh.sh
COPY sshd_config /etc/ssh/

# django
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=nobody . /usr/src/app
WORKDIR /usr/src/app
USER nobody
RUN mkdir log
RUN python manage.py collectstatic --no-input

# 8000 for the web and 2222 for ssh
EXPOSE 8000 2222

# Initialization
COPY init.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/init.sh
ENTRYPOINT ["init.sh"]
