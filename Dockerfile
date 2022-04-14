FROM python:3.8-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN command apt-get update && apt-get upgrade -y
RUN apt-get install libpq-dev python-dev gcc -y

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /py_ml
COPY . /py_ml

RUN chmod +x ./tools/run_stuff.sh
