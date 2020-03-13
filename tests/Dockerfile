FROM python:3.8-slim

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        make \
        git \
        curl \
        vim \
        # other packages needed for pyenv to build python versions
        # (could have used https://github.com/pyenv/pyenv/wiki/common-build-problems
        # but used instead https://github.com/docker-library/python/blob/21d2ab0a50100ebdaf32f4bbb214bf21f857d1da/3.8/buster/slim/Dockerfile
        # as `python3-openssl` package would install py37 by default)
        dpkg-dev \
        gcc \
        libbluetooth-dev \
        libbz2-dev \
        libc6-dev \
        libexpat1-dev \
        libffi-dev \
        libgdbm-dev \
        liblzma-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        tk-dev \
        uuid-dev \
        wget \
        xz-utils \
        zlib1g-dev \
        && \
    apt-get clean && \
    pip install cookiecutter
