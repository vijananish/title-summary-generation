# default value (python:3.8)
ARG BASE_IMAGE=python:3.8
FROM ${BASE_IMAGE}
WORKDIR /src
COPY src/requirements.txt /src
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY src /src