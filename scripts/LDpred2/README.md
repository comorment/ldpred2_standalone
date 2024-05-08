# LDpred2

This directory contains a copy of LDpred2 related scripts taken from our main [CoMorMent/Containers](https://github.com/comorment/containers) repository, 
in the [<containers>/scripts/pgs/LDpred2](https://github.com/comorment/containers/tree/main/scripts/pgs/LDpred2) directory. 
Usage of these scripts is documented throughout the corresponding README file as well as in the online [documentation](https://cosgap.readthedocs.io/en/latest/scripts/pgs/LDpred2/README.html).

Please note that some environment variables must be updated for Singularity compared to the above documentation, mainly:

```
export SIF=<path/to/ldpred2_standalone>/containers
export RSCRIPT="singularity exec --home=$PWD:/home $SIF/ldpred2.sif Rscript"
```

Also, note that this repository does not contain any reference datasets.
If needed, please obtain them as described in the official [documentation](https://cosgap.readthedocs.io/en/latest/scripts/pgs/LDpred2/README.html).

## Usage with ``ldpred2`` container

Some minimal examples invoking the R scripts provided here using either Apptainer/Singularity or Docker are shown below.
The latter is recommended for MacOS users with M1/M2 and newer chipsets.

### Apptainer/Singularity

Apptainer [https://apptainer.org](https://apptainer.org) is a tool to run Singularity containers with a simple command line interface.

#### Pulling

The container can be pulled from the GitHub Container Registry [ghcr.io](https://ghcr.io) on hosts with internet access by issuing:

```
$ apptainer pull ghcr.io/comorment/ldpred2:latest
```

or

```
$ singularity pull docker://ghcr.io/comorment/ldpred2:latest
```

or using the [ORAS CLI](https://oras.land)

```
$ oras pull ghcr.io/comorment/ldpred2_sif:latest
```

Either of the above will put the container in the current directory as `ldpred2.sif`.
The recommended file location is `<path/to/ldpred2_standalone>/containers/ldpred2.sif` for these examples.

#### Using

```
$ export CONTAINER=<path/to/ldpred2_standalone>/containers/ldpred2.sif
$ export RSCRIPT="singularity run --home=${PWD}:/home ${CONTAINER} Rscript"
$ $RSCRIPT ldpred2.R --help
usage: ldpred2.R [--] [--help] [--out-merge] [--geno-impute-zero]
       [--merge-by-rsid] [--opts OPTS] [--geno-file-rds GENO-FILE-RDS]
       [--sumstats SUMSTATS] [--out OUT] [--out-merge-ids
       OUT-MERGE-IDS] [--file-keep-snps FILE-KEEP-SNPS] [--ld-file
       LD-FILE] [--ld-meta-file LD-META-FILE] [--chr2use CHR2USE]
       [--col-chr COL-CHR] [--col-snp-id COL-SNP-ID] [--col-A1 COL-A1]
       [--col-A2 COL-A2] [--col-bp COL-BP] [--col-stat COL-STAT]
       [--col-stat-se COL-STAT-SE] [--col-pvalue COL-PVALUE] [--col-n
       COL-N] [--stat-type STAT-TYPE] [--effective-sample-size
       EFFECTIVE-SAMPLE-SIZE] [--n-cases N-CASES] [--n-controls
       N-CONTROLS] [--name-score NAME-SCORE] [--hyper-p-length
       HYPER-P-LENGTH] [--hyper-p-max HYPER-P-MAX] [--ldpred-mode
       LDPRED-MODE] [--cores CORES] [--set-seed SET-SEED]

Calculate polygenic scores using ldpred2

flags:
  -h, --help                   show this help message and exit
  --out-merge                  Merge output with existing file.
...
```

### Docker

#### Pulling

The container can be pulled from the GitHub Container Registry by issuing:

```
$ docker pull ghcr.io/comorment/ldpred2:latest
```

For usage, the container can be tagged as
```
$ docker tag ghcr.io/comorment/ldpred2:latest ldpred2:latest
```

Multiple tags may exist for the container, see the [GitHub Container Registry](https://ghcr.io/comorment/ldpred2) for more information.
The tags are generally the same as for the Docker containers.

#### Building

The ``<path/to/ldpred2_standalone>/dockerfiles/ldpred2/Dockerfile`` can been built locally by issuing:

```
export CONTAINER=ldpred2
docker build -t $CONTAINER -f docker/dockerfiles/ldpred2/Dockerfile .
```

#### Running

The container can be used by issuing:

```
$ export CONTAINER=ldpred2
$ export RSCRIPT="docker run -it --mount type=bind,source=${PWD},target=${PWD} ${CONTAINER} Rscript"
$ $RSCRIPT $PWD/ldpred2.R --help
usage: ldpred2.R [--] [--help] [--out-merge] [--geno-impute-zero]
...
```

#### MacOS Notes

If running Docker on MacOS with a modern M1/M2 chip, include `--platform linux/amd64` with the `docker pull` and `docker run` commands (and similar) to execute the container for the correct architecture.
