FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=main.py
ENV FLASK_DEBUG=1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

