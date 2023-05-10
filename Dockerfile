FROM public.ecr.aws/debian/debian:bullseye

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq

RUN apt-get install -y --no-install-recommends \
    wget python3-pip make

RUN pip3 install Jinja2==3.0 Sphinx==3.4.2 myst-parser==0.15.1

WORKDIR /opt
