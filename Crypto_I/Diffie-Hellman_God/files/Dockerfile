FROM python:3.8-alpine

RUN apk update && apk upgrade && apk add socat

RUN mkdir /chal
WORKDIR /chal
COPY . /chal
RUN chmod 555 server.py

RUN adduser -D chalhost
USER chalhost

CMD socat TCP-LISTEN:1337,fork,reuseaddr EXEC:"./server.py"

