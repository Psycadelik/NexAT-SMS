FROM python:3.6.8-slim
RUN apk --update add bash nano
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt