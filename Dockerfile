FROM debian:buster

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq

RUN apt-get install -y --no-install-recommends \
    build-essential libfreetype6-dev libfontconfig1-dev cmake\
    curl ca-certificates libssl-dev git unzip zip wget

RUN apt-get install -y --no-install-recommends \
	python-pip python-setuptools


RUN pip install Sphinx==1.6.3


# Build indigo
RUN mkdir -p /opt/indigo

# Make build operation cache-smart (only if version is changed)
ADD ./indigo/HEAD /srv/
COPY ./indigo/download.sh /srv/
COPY ./indigo/build-python.sh /srv/

RUN cd /srv && \
    ./download.sh

RUN cd /srv && \
    ./build-python.sh

WORKDIR /opt




