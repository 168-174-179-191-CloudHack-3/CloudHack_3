
FROM python:3.8-alpine
WORKDIR /app
ENV FLASK_APP=app.py

COPY ./app /app
#COPY ./app/requirements.txt /app/requirements.txt

RUN apk add --update \
&& pip install --upgrade pip  \
&& pip install -r requirements.txt \
&& rm -rf /var/cache/apk/*
# Syntax: COPY <src-path> <destination-path>

EXPOSE 5050
CMD ["python", "/app/app.py"]
