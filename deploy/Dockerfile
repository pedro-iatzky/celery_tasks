FROM python:3.6

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:/app
ENV PORT=8080
