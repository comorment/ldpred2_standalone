# LDpred2 standalone

Software container build(s) and utilities for computing polygenic scores (PGS), based on our main development repository [CoMorMent/Containers](https://github.com/comorment/containers)

## Obtaining these files

To use these files and codes, [clone](https://github.com/comorment/ldpred2_standalone) this repository by pressing that green [![Code](https://img.shields.io/badge/Code-green.svg)](https://github.com/comorment/ldpred2_standalone) button above and follow the instructions.

This repository also uses [git LFS](https://git-lfs.com) for large, non-code files.
After cloning the repository, initialize git LFS locally by issuing in the terminal:

```
cd </path/to/>ldpred2_standalone
git lfs install
git pull
```

## Build status

[![License](http://img.shields.io/:license-GPLv3+-green.svg)](http://www.gnu.org/licenses/gpl-3.0.html)
[![Documentation Status](https://readthedocs.org/projects/container-template/badge/?version=latest)](https://container-template.readthedocs.io/en/latest/?badge=latest)
[![Flake8 lint](https://github.com/comorment/ldpred2_standalone/actions/workflows/python.yml/badge.svg)](https://github.com/comorment/ldpred2_standalone/actions/workflows/python.yml)
[![Dockerfile lint](https://github.com/comorment/ldpred2_standalone/actions/workflows/docker.yml/badge.svg)](https://github.com/comorment/ldpred2_standalone/actions/workflows/docker.yml)

## Description of available containers

* ``ldpred2.sif`` - a minimal Singularity container with R based on [rocker/r-ver](https://rocker-project.org/images/versioned/r-ver.html), [PLINK](https://www.cog-genomics.org/plink/) version 1.9 and 2.0, and [PRSice-2](https://choishingwan.github.io/PRSice/), and R dependencies for running PGS using [LDpred2](https://privefl.github.io/bigsnpr/articles/LDpred2.html).


## Using



## Software versions

Below is the list of tools included in the different Dockerfile(s) and installer bash scripts for each container.
Please keep up to date (and update the main `<ldpred2_standalone>/README.md` when pushing new container builds):
  
### ldpred2_standalone.sif
  
| OS/tool               | Version/Git tag               | License           | Source
| --------------------- | ----------------------------- | ----------------- | -------------
| Ubuntu                | 22.04 (LTS)                   | [Creative Commons CC-BY-SA version 3.0 UK licence](https://ubuntu.com/legal/intellectual-property-policy) | [Ubuntu.com](https://ubuntu.com) |
| Rocker/r-ver          | 3.2.1                         | [GPL](https://github.com/rocker-org/rocker-versioned2/blob/master/LICENSE) | [rocker-project.org](https://rocker-project.org)
| R                     | 4.3.1 (2023-06-16)            | [GPL-*](https://www.r-project.org/Licenses/) | [r-project.org](https://www.r-project.org) |
| PLINK-1.9             | [v2.00a4.5](https://github.com/chrchang/plink-ng/releases/tag/v2.00a4.5)  | [GPL-3](https://github.com/chrchang/plink-ng/blob/master/1.9/LICENSE) | [https://www.cog-genomics.org/plink/](https://www.cog-genomics.org/plink/) |
| PLINK-2.0             | 2.00~a3-220218+dfsg-1         | [GPL-3](https://github.com/chrchang/plink-ng/blob/master/2.0/COPYING) | [https://www.cog-genomics.org/plink/](https://www.cog-genomics.org/plink/) |

## Building/rebuilding containers

For instructions on how to build or rebuild containers using [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) refer to [`<ldpred2_standalone>/docker/README.md`](https://github.com/comorment/ldpred2_standalone/blob/main/docker/README.md).

## Build the documentation

Within this repository, the html-documentation can be built from source files put here using [Sphinx](https://www.sphinx-doc.org/en/master/index.html). 
To do so, install Sphinx and some additional packages in python using [Conda](https://docs.conda.io/en/latest/) by issuing:

```
cd <ldpred2_standalone>/docs/source
conda env create -f environment.yml  # creates environment "sphinx"
conda activate sphinx  # activates environment "sphinx
make html  # builds html documentation into _build/html/ subdirectory
```

The built documentation can be viewed locally in a web browser by opening the file 
`<ldpred2_standalone>/docs/source/_build/html/index.html`

The documentation may also be hosted online on [readthedocs.org](https://readthedocs.org).

## SLURM jobscript example

A basic job script example for running a Singularity container in an HPC setting with the [SLURM](https://slurm.schedmd.com) job scheduler is provided in the file [singularity_slurm_job.sh](https://github.com/comorment/ldpred2_standalone/blob/main/scripts/singularity_slurm_job.sh), and should be modified as needed.
It expects a few environment variables, and can be submitted as

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
