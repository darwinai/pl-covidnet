FROM python:alpine as download

# Download the relevant machine learning models whose results will be used as input
# For example, for COVID-NET, download COVIDNet-CXR4-B from https://github.com/lindawangg/COVID-Net/blob/master/docs/models.md
WORKDIR /tmp/models/COVIDNet-CXR4-B
RUN pip install gdown \
  && gdown "https://drive.google.com/uc?id=1257TPH1o_kUl4YHnRg3tdy471tA5dE3v" \
  && gdown "https://drive.google.com/uc?id=1RhRM_9lczaOnhBJh_TrCryRzne-YYuH4" \
  && gdown "https://drive.google.com/uc?id=1lDR-CYciDpSlvZcoBxi3TFKWBNkZLJ4t" \
  && gdown "https://drive.google.com/uc?id=1hgeHuFaT4_o7g_CVIcGyKxh-ur9dwiQM"

WORKDIR /tmp/models/COVIDNet-SEV-GEO
RUN pip install gdown \
  && gdown "https://drive.google.com/uc?id=1vmr5gADYVokAYz-6kGQ-INb_r0weoWWD" \
  && gdown "https://drive.google.com/uc?id=18zSwSRybX2Zy5jm0E4alBuGGvHAuuvXd" \
  && gdown "https://drive.google.com/uc?id=10aL3s_TLRSCxZ0E2OUIjy9rLa-fTOtUj" \
  && gdown "https://drive.google.com/uc?id=1Sbp4NetlGzEM0VwxkZ1Lq-0fjprdjdCR"

WORKDIR /tmp/models/COVIDNet-SEV-OPC
RUN pip install gdown \
  && gdown "https://drive.google.com/uc?id=11Ju0YeIitzS2GgXJ4U5J3M87tF683-sM" \
  && gdown "https://drive.google.com/uc?id=1m0dXmUueCx4v9PbZhanmbt0ECe63tMKA" \
  && gdown "https://drive.google.com/uc?id=1oaILEyuMcHWQS68l4hrMPyWgosnqfAu0" \
  && gdown "https://drive.google.com/uc?id=1m5eJwhuFccZwyGl8T4DRfq8x3rgkqCEC"

FROM docker.io/fnndsc/tensorflow:1.15.3

LABEL org.opencontainers.image.authors="DarwinAI <support@darwinai.com>"

ENV DEBIAN_FRONTEND=noninteractive

COPY ["apt-requirements.txt", "requirements.txt", "./"]

RUN apt-get update \
  && xargs -d '\n' -a apt-requirements.txt apt-get install -y \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && rm -rf /var/lib/apt/lists/* \
  && rm -f requirements.txt apt-requirements.txt

COPY --from=download /tmp/models /usr/local/lib/covidnet

WORKDIR /usr/local/src
COPY . .
RUN pip install .

CMD ["covidnet", "--help"]
