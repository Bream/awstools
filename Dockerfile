FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y python3 python3-boto python3-pip libssl-dev

RUN pip3 install moto

ADD . /auto-shutdown

WORKDIR /auto-shutdown
CMD [ "python3", "auto-shutdown.py" ]
