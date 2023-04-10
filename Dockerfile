FROM python:3.11-slim-buster

WORKDIR /

# Dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src/ src/
COPY builds/ builds/
COPY tests/ tests/