# R container
FROM rocker/r-ver:4.3.3
RUN /rocker_scripts/setup_R.sh https://packagemanager.posit.co/cran/__linux__/jammy/2024-03-01

ENV TZ=Europe
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /tmp/

# some system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils=2.4.12 \
    ca-certificates=20230311ubuntu0.22.04.1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    update-ca-certificates

RUN apt-get update && apt-get install -y --no-install-recommends \
    bzip2=1.0.8-5build1 \
    cmake=3.22.1-1ubuntu1.22.04.2 \
    curl=7.81.0-1ubuntu1.16 \
    libatlas-base-dev=3.10.3-12ubuntu1 \
    libctl-dev=4.5.1-1 \
    libeigen3-dev=3.4.0-2ubuntu2 \
    libgcc-11-dev=11.4.0-1ubuntu1~22.04 \
    libgslcblas0=2.7.1+dfsg-3 \
    libicu-dev=70.1-2 \
    node-shasum=1.0.2-3 \
    patch=2.7.6-7build2 \
    unzip=6.0-26ubuntu3.2 \
    zlib1g-dev=1:1.2.11.dfsg-2ubuntu9.2 \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# R dependencies
RUN R -e "install.packages(c('devtools', 'argparser', 'bigsnpr', 'data.table', 'essentials', 'eulerr', 'IRkernel', 'optparse', 'stringr', 'R.utils', 'tidyverse'), dependencies=c('Depends', 'Imports', 'LinkingTo'))"

    
# install plink 1.9
RUN curl -sSL https://github.com/chrchang/plink-ng/archive/refs/tags/v2.00a4.5.zip -o v2.00a4.5.zip && \
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
RUN curl -sSL https://github.com/choishingwan/PRSice/archive/refs/tags/2.3.5.zip -o 2.3.5.zip && \
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

WORKDIR /tmp/miniforge
RUN curl -sSL "https://github.com/conda-forge/miniforge/releases/download/24.3.0-0/Miniforge3-24.3.0-0-$("uname")-$("uname -m").sh" -o /tmp/miniforge.sh \
    && mkdir /root/.conda \
    && bash /tmp/miniforge.sh -bfp /usr/local \
    && rm -rf /tmp/miniforge.sh \
    && export PATH=$PATH:/opt/conda/bin

RUN mamba install \
    python=3.11 \
    conda-pack==0.7.1 \
    numpy==1.26.4 \
    scipy==1.13.0 \
    numba==0.59.1 \
    pandas==2.2.2 \
    matplotlib-base==3.8.4 \
    seaborn==0.13.2 \
    notebook==7.1.3 \
    --yes && \
    mamba install icc_rt==2020.2 --channel numba --yes

# clean up
RUN mamba clean -a -y && \
        pip cache purge && \
    rm -rf /tmp/*

WORKDIR /
