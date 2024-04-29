FROM ubuntu:22.04 as dependencies

RUN mkdir "/app"
WORKDIR /app
RUN apt-get update
RUN apt-get install -y python3-pip wget libgdiplus
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1-1ubuntu2.1~18.04.23_amd64.deb \
    && dpkg -i libssl1.1_1.1.1-1ubuntu2.1~18.04.23_amd64.deb
RUN apt autoremove \
    && apt clean


FROM dependencies as code
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

FROM code as test-runner
ENTRYPOINT ["/app/test.sh"]