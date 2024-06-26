# PRSice-2

This directory contains a copy of the [``PRSice.R``](https://github.com/choishingwan/PRSice/blob/2.3.5/PRSice.R) script taken from the PRSice [repository](https://github.com/choishingwan/PRSice/tree/2.3.5) for use with the software container provided here, as it contains the ``PRSice`` binary.

For details on PRSice, see its [documentation](https://choishingwan.github.io/PRSice/).

## Usage with ``ldpred2`` container

Minimal example using:

### Singularity

Invoking the ``PRSice`` binary:

```
$ export CONTAINER=<path/to/ldpred2_standalone>/containers/ldpred2.sif
$ export PRSICE="singularity run --home=${PWD}:/home ${CONTAINER} PRSice"
$ $PRSICE --version
2.3.5 (2021-09-20) 

$ PRSICE --help
usage: PRSice [options] <-b base_file> <-t target_file>

Base File:
    --a1                    Column header containing allele 1 (effective allele)
                            Default: A1
    --a2                    Column header containing allele 2 (non-effective allele)
                            Default: A2
...
```

Invoking the ``PRSice.R`` script: 
```
$ export CONTAINER=<path/to/ldpred2_standalone>/containers/ldpred2.sif
$ export RSCRIPT="singularity run --home=${PWD}:/home ${CONTAINER} Rscript"
$ export LS="singularity run --home=${PWD}:/home ${CONTAINER} ls"
$ $RSCRIPT PRSice.R --help
usage: Rscript PRSice.R [options] <-b base_file> <-t target_file> <--prsice prsice_location>

Required:

    --prsice                Location of the PRSice binary
    --dir                   Location to install ggplot. Only require if ggplot
                            is not installed
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

#### Building

The ``<path/to/ldpred2_standalone>/dockerfiles/ldpred2/Dockerfile`` can be built locally by issuing:

```
export CONTAINER=ldpred2
docker build -t $CONTAINER -f docker/dockerfiles/ldpred2/Dockerfile .
```
#### Using

It can be used by issuing with the ``PRSice`` binary as:

```
$ export CONTAINER=ldpred2
$ export PRSICE="docker run -it --mount type=bind,source=${PWD},target=${PWD} ${CONTAINER} PRSice"
$ $PRSICE --<arg1> --<arg2> ...
...
```

And similar with ``PRSice.R`` as:

```
$ export CONTAINER=ldpred2
$ export RSCRIPT="docker run -it --mount type=bind,source=${PWD},target=/home ${CONTAINER} Rscript"
$ $RSCRIPT $PWD/PRSice.R --no-install --<arg1> --<arg2> ...
```

Note that the ``--no-install`` option is set as the script may try and install additional R packages which should be included the container itself.

#### MacOS Notes

If running Docker on MacOS with a modern M1/M2 chip, include `--platform linux/amd64` with the `docker pull` and `docker run` commands (and similar) to execute the container for the correct architecture.
