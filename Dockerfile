FROM debian:buster

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq

RUN apt-get install -y --no-install-recommends \
    wget python-pip make

RUN pip install Sphinx==1.6.3

# Build indigo
RUN mkdir -p /opt/indigo

# Make build operation cache-smart (only if version is changed)
COPY ./indigo/HEAD /srv/
COPY ./indigo/download.sh /srv/

RUN cd /srv && \
    ./download.sh && \
    rm /srv/HEAD && \
    rm /srv/download.sh

WORKDIR /opt




