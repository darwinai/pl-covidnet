FROM alpine:latest as download

WORKDIR /tmp
ADD https://fnndsc.childrens.harvard.edu/COVID-Net/models/20200727/selected_models.tar.gz /tmp/models.tar.gz
RUN ["tar", "xf", "models.tar.gz"]

FROM docker.io/fnndsc/tensorflow:1.15.3

ENV DEBIAN_FRONTEND=noninteractive

# install python dependencies using apt
# for support on non-x86_64 architectures such as PowerPC
RUN apt-get update \
    && apt-get install -y python3-opencv \
    && rm -rf /var/lib/apt/lists/*

COPY --from=download /tmp/models /usr/local/lib/covidnet

WORKDIR /usr/local/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN pip install .

CMD ["covidnet", "--help"]
