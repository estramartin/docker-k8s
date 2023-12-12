FROM python:3.10.6

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
