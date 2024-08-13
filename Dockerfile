FROM ubuntu:22.04
LABEL maintainer="Yesha Vyas <yeshavyas27@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata

RUN apt-get update && apt-get install -y python3.10 python3-pip tzdata

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN date

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install -r /app/requirements.txt

RUN echo "In the middle of the build"

COPY . /app