# R container
FROM rocker/r-ver:4.3.1

ENV TZ=Europe
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /tmp/

# R dependencies
RUN R -e "install.packages('devtools', version='2.4.5', repos='https://packagemanager.rstudio.com/cran/__linux__/focal/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('argparser', version='0.7.1', repos='https://packagemanager.rstudio.com/cran/__linux__/focal/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('bigsnpr', version='1.11.6', repos='https://packagemanager.rstudio.com/cran/__linux__/focal/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('data.table', version='1.14.6', repos='https://packagemanager.rstudio.com/cran/__linux__/focal/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('stringr', version='1.5.0', repos='https://packagemanager.rstudio.com/cran/__linux__/focal/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('R.utils', version='2.12.2', repos='https://packagemanager.rstudio.com/cran/__linux__/focal/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))" && \
    R -e "install.packages('tidyverse', version='1.3.2', repos='https://packagemanager.rstudio.com/cran/__linux__/focal/2023-02-16', dependencies=c('Depends', 'Imports', 'LinkingTo'))"


# some system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils=2.4.10 && \
    apt-get update && apt-get install -y --no-install-recommends ca-certificates=20230311ubuntu0.22.04.1 && \
    update-ca-certificates
RUN apt-get update && apt-get install -y --no-install-recommends \
   unzip=6.0-26ubuntu3.1 \
   wget=1.21.2-2ubuntu1 \
   && \
   apt-get clean && \
   rm -rf /var/lib/apt/lists/*

# install plink 2
RUN apt-get update && apt-get install -y --no-install-recommends \
   plink2=2.00~a3-220218+dfsg-1 \
   && \
   apt-get clean && \
   rm -rf /var/lib/apt/lists/*

# install plink 1.9 deps
RUN apt-get update && apt-get install -y --no-install-recommends \
   curl=7.81.0-1ubuntu1.13 \
   node-shasum=1.0.2-3 \
   libatlas-base-dev=3.10.3-12ubuntu1 \
   libgslcblas0=2.7.1+dfsg-3 \
   && \
   apt-get clean && \
   rm -rf /var/lib/apt/lists/*

# create alias shasum -> sha1sum
RUN ln -s /usr/bin/sha1sum /usr/bin/shasum

# install plink 1.9
RUN cd /tmp && \
    wget --no-check-certificate https://github.com/chrchang/plink-ng/archive/refs/tags/v2.00a4.5.zip && \
    unzip v2.00a4.5.zip && \
    cd plink-ng-2.00a4.5/1.9 && \
    ./plink_first_compile && \
    cp plink /bin && \
    cd /tmp && \
    rm -rf v2.00a4.5.zip plink-ng-2.00a4.5



# RUN wget --no-check-certificate https://s3.amazonaws.com/plink1-assets/plink_linux_x86_64_20200616.zip && \
#     unzip -j plink_linux_x86_64_20200616.zip && \
#     rm -rf plink_linux_x86_64_20200616.zip && \
#     cp plink /bin

# install PRSice 2
# RUN wget --no-check-certificate https://github.com/choishingwan/PRSice/releases/download/2.3.5/PRSice_linux.zip && \
#     unzip PRSice_linux.zip  && \
#     rm -rf PRSice_linux.zip && \
#     cp PRSice_linux  /bin

RUN rm -rf /tmp/*

WORKDIR /