FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

RUN apt-get update \
    && apt-get install \
        python3 \
        python3-pip \
        git \
        -y -qq

RUN pip3 install torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/cu118
