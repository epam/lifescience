FROM debian:stretch

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq

RUN apt-get install -y --no-install-recommends \
    build-essential libfreetype6-dev libfontconfig1-dev cmake\
    curl ca-certificates libssl-dev git unzip zip
    

RUN apt-get install -y --no-install-recommends \
	python-sphinx

RUN apt-get install -y --no-install-recommends \
	wget

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


#RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \
#  rm -rf \
#    /var/lib/apt/lists/* \
#    /tmp/* \
#    /var/tmp/* \
#    mkdir /code


