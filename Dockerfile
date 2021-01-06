FROM debian:bullseye

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq

RUN apt-get install -y --no-install-recommends \
    wget python3-pip make

RUN pip3 install Sphinx==3.4.2

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




