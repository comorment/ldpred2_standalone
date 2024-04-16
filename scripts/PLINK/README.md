# PLINK

Invoking [``PLINK``](https://www.cog-genomics.org/plink/) from the ``ldpred2`` container, using either ``PLINK-1.9`` or ``PLINK-2.0`` in:

## Singularity

### PLINK-1.9

```
$ export CONTAINER=<path/to/ldpred2_standalone>/containers/ldpred2.sif
$ singularity run --home=$PWD:/home $CONTAINER plink --version
PLINK v1.90p 64-bit (13 Feb 2023)
```

### PLINK-2.0

```
$ export CONTAINER=<path/to/ldpred2_standalone>/containers/ldpred2.sif
$ singularity run --home=$PWD:/home $CONTAINER plink2 --version
PLINK v2.00a3 SSE4.2 (18 Feb 2022)
```

## Docker

### Pulling

The container can be pulled from the GitHub Container Registry by issuing:

```
$ docker pull ghcr.io/comorment/ldpred2:latest
```

For usage, the container can be tagged as
```
$ docker tag ghcr.io/comorment/ldpred2:latest ldpred2:latest
```

### Building

The ``<path/to/ldpred2_standalone>/dockerfiles/ldpred2/Dockerfile`` can be built locally by issuing:

```
export CONTAINER=ldpred2
docker build -t $CONTAINER -f docker/dockerfiles/ldpred2/Dockerfile .
```

### Using

it can be used by issuing:

```
$ export CONTAINER=ldpred2
$ docker run -it --mount type=bind,source=$PWD,target=/home $CONTAINER plink --version
PLINK v1.90p 64-bit (13 Feb 2023)
```

and similar for the ``plink2`` binary.

### MacOS Notes

If running Docker on MacOS with a modern M1/M2 chip, include `--platform linux/amd64` with the `docker pull` and `docker run` commands (and similar) to execute the container for the correct architecture.
