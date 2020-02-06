FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y software-properties-common --no-install-recommends
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get install -y python3.8 python3-pip python3-setuptools --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["./start.sh"]