FROM ubuntu:latest


RUN apt-get update && apt-get install -y \
    bash \
    procps \
    coreutils \
    util-linux \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /sh-container


COPY system-state.sh .


RUN chmod +x system-state.sh


CMD ["./system-state.sh"]

