#!/bin/bash
apt-get update && apt-get install -y  --no-install-recommends \
    apt-utils=2.0.9 \
    ca-certificates=20211016ubuntu0.20.04.1 \
    curl=7.68.0-1ubuntu2.15 \
    && \
    update-ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
