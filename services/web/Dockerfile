# pull base image
FROM python:3.8.1-slim-buster

# setting up working directory
WORKDIR /usr/src/app

# setting up environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
# copy project
COPY . /usr/src/app/
# run entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

