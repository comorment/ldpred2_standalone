# encoding: utf-8

"""
Test module for ``ldpred2_standalone.sif`` singularity build
or ``ldpred2_standalone`` dockerfile build

In case ``singularity`` is unavailable, the test function(s) should fall
back to ``docker``.
"""

import os
import socket
import subprocess


# port used by tests
sock = socket.socket()
sock.bind(('', 0))
port = sock.getsockname()[1]

# Check that (1) singularity exist, and (2) if not, check for docker.
# If neither are found, tests will not run.
try:
    pth = os.path.join('containers', 'ldpred2_standalone.sif')
    out = subprocess.run('singularity')
    cwd = os.getcwd()
    PREFIX = f'singularity run {pth}'
    PREFIX_MOUNT = PREFIX_MOUNT = f'singularity run --no-home --bind {cwd} {pth}'
    # PREFIX_MOUNT = PREFIX_MOUNT = f'singularity run --home={cwd}:/home/ {pth}'
except FileNotFoundError:
    try:
        out = subprocess.run('docker')
        pwd = os.getcwd()
        PREFIX = f'docker run -p {port}:{port} ldpred2_standalone'
        PREFIX_MOUNT = (
            f'docker run -p {port}:{port} ' +
            f'--mount type=bind,source={pwd},target={pwd} ldpred2_standalone')
    except FileNotFoundError as e:
        raise FileNotFoundError(
            'Neither `singularity` nor `docker` found in PATH.' +
            'Can not run tests!') from e


def test_assert():
    """dummy test that should pass"""
    assert True


def test_ldpred2_standalone_R():
    call = f'{PREFIX} R --version'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0


def test_ldpred2_standalone_Rscript():
    call = f'{PREFIX} Rscript --version'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0


def test_ldpred2_standalone_R_packages():
    pwd = os.getcwd()
    call = f'{PREFIX_MOUNT} Rscript tests/extras/r.R'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0


def test_ldpred2_standalone_bin_prsice():
    call = f'{PREFIX} PRSice --version'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0


def test_ldpred2_standalone_bin_plink():
    call = f'{PREFIX} plink --version'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0


def test_ldpred2_standalone_bin_plink2():
    call = f'{PREFIX} plink2 --version'
    out = subprocess.run(call.split(' '))
    assert out.returncode == 0

