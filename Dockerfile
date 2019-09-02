#FROM python:3.6.8-slim
#RUN apk --update add bash nano
#COPY ./requirements.txt /var/www/requirements.txt
#RUN pip install -r /var/www/requirements.txt

FROM python:3.6-alpine

RUN adduser -D chezasms

WORKDIR /home/chezasms

COPY requirements.txt requirements.txt

#RUN python -m venv venv
#RUN venv/bin/pip install -r requirements.txt
#RUN venv/bin/pip install gunicorn

COPY sibsco sibsco
COPY migrations migrations
COPY run.py settings.py start.sh ./

RUN pip install -r requirements.txt

#RUN chmod +x start.sh

#ENV FLASK_APP run.py

#RUN chown -R chezasms:chezasms ./

USER chezasms

EXPOSE 5000
#ENTRYPOINT ["./start.sh"]
CMD ["python", "run.py", "0.0.0.0:5000"]






