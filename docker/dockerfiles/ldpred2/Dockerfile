# R container
FROM rocker/r-ver:4.3.1

ENV TZ=Europe
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /tmp/

# some system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils=2.4.10 \
    ca-certificates=20230311ubuntu0.22.04.1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    update-ca-certificates

RUN apt-get update && apt-get install -y --no-install-recommends \
    cmake=3.22.1-1ubuntu1.22.04.1 \
    curl=7.81.0-1ubuntu1.13 \
    libatlas-base-dev=3.10.3-12ubuntu1 \
    libctl-dev=4.5.1-1 \
    libeigen3-dev=3.4.0-2ubuntu2 \
    libgslcblas0=2.7.1+dfsg-3 \
    libicu-dev=70.1-2 \
    node-shasum=1.0.2-3 \
    patch=2.7.6-7build2 \
    unzip=6.0-26ubuntu3.1 \
    wget=1.21.2-2ubuntu1 \
    zlib1g-dev=1:1.2.11.dfsg-2ubuntu9.2 \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# R dependencies
RUN R -e "install.packages('devtools', version='2.4.5', repos='https://packagemanager.posit.co/cran/__linux__/jammy/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('argparser', version='0.7.1', repos='https://packagemanager.posit.co/cran/__linux__/jammy/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('bigsnpr', version='1.11.6', repos='https://packagemanager.posit.co/cran/__linux__/jammy/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('data.table', version='1.14.6', repos='https://packagemanager.posit.co/cran/__linux__/jammy/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('optparse', version='1.7.3', repos='https://packagemanager.posit.co/cran/__linux__/jammy/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('stringr', version='1.5.0', repos='https://packagemanager.posit.co/cran/__linux__/jammy/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('R.utils', version='2.12.2', repos='https://packagemanager.posit.co/cran/__linux__/jammy/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('tidyverse', version='1.3.2', repos='https://packagemanager.posit.co/cran/__linux__/jammy/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))"
        
# install plink 1.9
RUN wget -q --no-check-certificate https://github.com/chrchang/plink-ng/archive/refs/tags/v2.00a4.5.zip && \
    unzip v2.00a4.5.zip

WORKDIR /tmp/plink-ng-2.00a4.5/1.9
RUN ./plink_first_compile && \
    cp plink /bin/

# install plink 2
WORKDIR /tmp/plink-ng-2.00a4.5/2.0
RUN make -j && \
    cp "${PWD}"/bin/* /bin/

# clean up
WORKDIR /tmp
RUN rm -rf v2.00a4.5.zip plink-ng-2.00a4.5

# install PRSice-2
COPY patches/*.diff /tmp/patches/
RUN wget -q --no-check-certificate https://github.com/choishingwan/PRSice/archive/refs/tags/2.3.5.zip && \
    unzip 2.3.5.zip

WORKDIR /tmp/PRSice-2.3.5
RUN patch inc/misc.hpp < /tmp/patches/prsice_patch_1.diff && \
    patch inc/storage.hpp < /tmp/patches/prsice_patch_2.diff && \
    patch inc/genotype.hpp < /tmp/patches/prsice_patch_3.diff && \
    patch inc/fastlm.hpp < /tmp/patches/prsice_patch_4.diff && \
    patch inc/family.hpp < /tmp/patches/prsice_patch_5.diff && \
    patch inc/glm.hpp < /tmp/patches/prsice_patch_6.diff && \
    patch inc/regression.hpp < /tmp/patches/prsice_patch_7.diff && \
    patch inc/prsice.hpp < /tmp/patches/prsice_patch_8.diff && \
    mkdir build

WORKDIR /tmp/PRSice-2.3.5/build
RUN cmake ../ && \
    make -j && \
    cp ../bin/PRSice /bin/
    
WORKDIR /tmp 
RUN rm -rf 2.3.5.zip PRSice-2.3.5

# clean up
RUN rm -rf /tmp/*

WORKDIR /