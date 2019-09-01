#FROM python:3.6.8-slim
#RUN apk --update add bash nano
#COPY ./requirements.txt /var/www/requirements.txt
#RUN pip install -r /var/www/requirements.txt

FROM python:3.6-alpine

RUN adduser -D chezasms

WORKDIR /home/chezasms

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY app.py settings.py start.sh ./
RUN chmod +x start.sh

ENV FLASK_APP app.py

RUN chown -R chezasms:chezasms ./

USER chezasms

EXPOSE 5000
ENTRYPOINT ["./start.sh"]







