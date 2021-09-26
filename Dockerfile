FROM debian:bullseye

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq

RUN apt-get install -y --no-install-recommends \
    wget python3-pip make

RUN pip3 install Sphinx==3.4.2 myst-parser==0.15.1

WORKDIR /opt
