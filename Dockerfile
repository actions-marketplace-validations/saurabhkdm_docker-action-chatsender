FROM ubuntu:latest

COPY .  /.

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.7 \
    python3-pip \

RUN pip3 install json httplib2

ENTRYPOINT ["/entrypoint.sh"]
