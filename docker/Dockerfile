FROM ubuntu

# Etiquette pour le mainteneur
LABEL maintainer="amadou.diadie04@gmail.com"

COPY . /Daamtu

RUN apt-get update
RUN apt-get install -y curl neofetch iputils-ping nano btop net-tools socat
RUN socat TCP6-LISTEN:8888,fork TCP4:127.0.0.1:9000 &

ENV TEST_KEY=
ENV SECOND_KEY=
COPY healthy .
COPY readme.sh .

CMD sleep 500000000
