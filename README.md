# ldpred2_standalone project

README info goes here. Modify for your own project's needs.

# Important! - post initial setup steps

After setting up project from the template, add files, commit and push the changes after running the setup script (`scripts/init.py`):

```
git add <file1> <file2> ...
git commit -a -m "initial setup"
git push
```

The remaining codes may then be added to and be modified further to suit the requirements of the `<ldpred2_standalone>` project. 

# Important! - Set up Git LFS

Container files may get large and one should never add large binary files (.sif, .zip, .tar.gz, .mat, .dat, etc.) in [git](https://git-scm.com) repositories directly, mainly files that can be parsed as raw text files (code files, etc.).
[**Git Large File Storage** (LFS)](https://git-lfs.github.com) should be used instead.
Before adding new files to this project after initialization (running `python scripts/init.py`), go through step 1-3 on the Git LFS [homepage](https://git-lfs.github.com).
Revise the `<ldpred2_standalone>/.gitattributes` file as necessary. Some common file formats has been added already.

## Build status

[![License](http://img.shields.io/:license-GPLv3+-green.svg)](http://www.gnu.org/licenses/gpl-3.0.html)
[![Documentation Status](https://readthedocs.org/projects/container-template/badge/?version=latest)](https://container-template.readthedocs.io/en/latest/?badge=latest)
[![Flake8 lint](https://github.com/comorment/ldpred2_standalone/actions/workflows/python.yml/badge.svg)](https://github.com/comorment/ldpred2_standalone/actions/workflows/python.yml)
[![Dockerfile lint](https://github.com/comorment/ldpred2_standalone/actions/workflows/docker.yml/badge.svg)](https://github.com/comorment/ldpred2_standalone/actions/workflows/docker.yml)

## Description of available containers

* ``ldpred2_standalone`` - a hello-world introductory container setup

## Software versions

Below is the list of tools included in the different Dockerfile(s) and installer bash scripts for each container.
Please keep up to date (and update the main `<ldpred2_standalone>/README.md` when pushing new container builds):
  
### ldpred2_standalone.sif
  
| OS/tool             | Version               | License           | Source
| ------------------- | --------------------- | ----------------- | -------------
| ubuntu              | 20.04                 | [Creative Commons CC-BY-SA version 3.0 UK licence](https://ubuntu.com/legal/intellectual-property-policy) | [Ubuntu.com](https://ubuntu.com)
| python              | 3.8.10                | [PSF](https://docs.python.org/3.10/license.html) | [Python.org](https://www.python.org)

## Building/rebuilding containers

For instructions on how to build or rebuild containers using [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) refer to [`<ldpred2_standalone>/src/README.md`](https://github.com/comorment/ldpred2_standalone/blob/main/src/README.md).

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
