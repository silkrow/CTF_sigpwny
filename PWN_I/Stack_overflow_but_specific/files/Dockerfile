# You can probably ignore this file! We just put it here for completeness.
# Just take a look at challenge.c.

FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat gcc python
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/pwn
WORKDIR /usr/src/pwn
RUN cd /usr/src/pwn/

COPY flag.txt .
RUN chmod 444 flag.txt
RUN adduser pwn
COPY challenge.c .
RUN gcc -std=c99 -o challenge challenge.c -O0 -fno-stack-protector -g -Wno-deprecated-declarations
RUN chmod 111 challenge
RUN rm challenge.c
USER pwn
CMD socat -T60 TCP-LISTEN:1337,fork,reuseaddr EXEC:"./challenge"
