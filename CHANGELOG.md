# Changelog
All notable changes to the container-template project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- additions goes here

### Updated

- updated LDpred2 R scripts (SHA: d882dd9cbefd457d1f14f2e7d8ed91fdabd08937 of github.com/comorment/containers)
- use `testthat` for checking R package installation
- Updated Dockerfile compiling PLINK-2.0 inplace

### Fixed

- `plink2` binary now works on Macs w. M1/M2 CPUs

### Removed

- removals goes here

## [1.0.0rc0] - 2023-08-24

### Added

- ``ldpred2.sif`` Singularity container and scripts
