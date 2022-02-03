FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y gettext && \
 rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
ADD . /usr/src/app
RUN pip install -r req.txt