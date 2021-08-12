FROM python:3.9.5-slim-buster

# UPDATE/UPGRADE PACKAGES AND PIP
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install tzdata -y \
    && pip3 install --upgrade pip

# INSTALL REQUIREMENTS
COPY ./reqs/requirements.txt /
RUN pip3 install -r requirements.txt

# CREATE APP DIR
RUN mkdir app
