# LDpred2 standalone

Software container build(s) and utilities for computing polygenic scores (PGS), based on our main development repository [CoMorMent/Containers](https://github.com/comorment/containers)

## Dependencies

To set up this project on the local machine, the following may be required:

* [git](https://git-scm.com)
* [git LFS](https://git-lfs.com)
* [Docker](https://www.docker.com). Recommended for MacOS users (with M1, M2, or newer chips)
* [Singularity](https://docs.sylabs.io) or [Apptainer](https://apptainer.org). Recommended for Linux users, or for MacOS users (with Intel chips), or for secure systems with no direct internet access.
* [ORAS CLI](https://oras.land). Recommended for Linux users, or for users wishing to download the Singularity container from the GitHub Container Registry
* [Python](https://python.org) version 3.11 or newer

There are multiple methods to install these dependencies, and the user should choose the one that best fits their system.
Please refer to the respective websites for installation instructions.

### Conda environment

For ease of use, a [Conda](https://docs.conda.io/en/latest/) environment file is provided in the [conda-environment.yml](https://github.com/comorment/ldpred2_standalone/blob/main/conda-environment.yml) in this repository.

To create a new Conda environment with the required dependencies, issue in the terminal:

```
conda env create -f conda-environment.yml
conda activate ldpred2_standalone
```

To obtain Conda, please refer to the [Conda installation instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

## Obtaining these files

To use these files and codes, [clone](https://github.com/comorment/ldpred2_standalone) this repository by pressing the green [![Code](https://img.shields.io/badge/Code-green.svg)](https://github.com/comorment/ldpred2_standalone) button above and follow the instructions.

For those who will not need the entire development history, a shallow clone may be performed by issuing:

```
git clone --depth 1 https://github.com/comorment/ldpred2_standalone.git
```

This repository may use [git LFS](https://git-lfs.com) for large, non-code files.
After cloning the repository, initialize git LFS locally by issuing in the terminal:

```
cd </path/to/>ldpred2_standalone
git lfs install
git pull
```

## Build status

[![License](http://img.shields.io/:license-GPLv3+-green.svg)](http://www.gnu.org/licenses/gpl-3.0.html)
[![Documentation Status](https://readthedocs.org/projects/ldpred2_standalone/badge/?version=latest)](https://ldpred2_standalone.readthedocs.io/en/latest/?badge=latest)
[![Flake8 lint](https://github.com/comorment/ldpred2_standalone/actions/workflows/python.yml/badge.svg)](https://github.com/comorment/ldpred2_standalone/actions/workflows/python.yml)
[![Dockerfile lint](https://github.com/comorment/ldpred2_standalone/actions/workflows/docker.yml/badge.svg)](https://github.com/comorment/ldpred2_standalone/actions/workflows/docker.yml)

## Description of available containers

* ``ldpred2.sif`` - a minimal Singularity container with R and RStudio based on [rocker/r-ver](https://rocker-project.org/images/versioned/r-ver.html), [Python](https://python.org) with some common numerics and plotting packages, [PLINK](https://www.cog-genomics.org/plink/) version 1.9 and 2.0, and [PRSice-2](https://choishingwan.github.io/PRSice/), and dependencies for running PGS using [LDpred2](https://privefl.github.io/bigsnpr/articles/LDpred2.html).

## Using

Please refer to the scripts and README files in the [scripts](https://github.com/comorment/ldpred2_standalone/tree/main/scripts/) directory for usage

## Software versions

This [table](https://github.com/comorment/ldpred2_standalone/tree/main/docker#ldpred2sif) contains the list of tools included in the different Dockerfile(s) and installer bash scripts for each container.
Please keep up to date when pushing new container builds:

## Pulling/Building/rebuilding containers

For instructions on how to build or rebuild containers using [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) or [Apptainer](https://apptainer.org) refer to [`<ldpred2_standalone>/docker/README.md`](https://github.com/comorment/ldpred2_standalone/blob/main/docker/README.md).

## Build the documentation

Within this repository, the html-documentation can be built from source files put here using [Sphinx](https://www.sphinx-doc.org/en/master/index.html). 
To do so, install Sphinx and some additional packages in Python using [Conda](https://docs.conda.io/en/latest/) by issuing:

```
cd <ldpred2_standalone>/docs/source
conda env create -f environment.yml  # creates environment "sphinx"
conda activate sphinx  # activates environment "sphinx
make html  # builds html documentation into _build/html/ subdirectory
```

The built documentation can be viewed locally in a web browser by opening the file
`<ldpred2_standalone>/docs/source/_build/html/index.html`

The documentation may also be hosted online on [readthedocs.org](https://readthedocs.org).

## SLURM job script example

A basic job script example for running a Singularity container in an HPC setting with the [SLURM](https://slurm.schedmd.com) job scheduler is provided in the file [singularity_slurm_job.sh](https://github.com/comorment/ldpred2_standalone/blob/main/scripts/singularity_slurm_job.sh), and should be modified as needed.
It expects a few environment variables and can be submitted as

```
export JOBNAME=ldpred2_standalone
export ACCOUNT=<project allocation account name>
export WALLTIME="00:05:00"  # expected run time HH:MM:SS format
export CPUS_PER_TASK=1  # number of CPU cores
export MEM_PER_CPU=2000MB  # RAM per CPU
export SINGULARITY_MODULE=singularity/3.7.1  # name of Singularity module and version

sbatch singularity_slurm_job.sh  # submit job
```
The output of the job will be written to the text files `ldpred2_standalone.out` (output) and `ldpred2_standalone.err` (errors).

## Feedback

If you face any issues, or if you need additional software, please let us know by creating a new [issue](https://github.com/comorment/ldpred2_standalone/issues/new).
