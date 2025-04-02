FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app /app/app

ENV FLASK_APP=app
CMD [ "flask", "run", "--host=0.0.0.0" ]
