#!/bin/bash
version=22.11.1-4
curl -sSL https://github.com/conda-forge/miniforge/releases/download/$version/Mambaforge-$version-$(uname)-$(uname -m).sh -o /tmp/mambaforge.sh \
  && mkdir /root/.conda \
  && bash /tmp/mambaforge.sh -bfp /usr/local \
  && rm -rf /tmp/mambaforge.sh
