# encoding: utf-8

"""
Test module for ``ldpred2.sif`` singularity build
or ``ldpred2`` dockerfile build

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
    pth = os.path.join('containers', 'ldpred2.sif')
    _ = subprocess.run('singularity', check=False)
    cwd = os.getcwd()
    PREFIX = f'singularity run {pth}'
    # PREFIX_MOUNT = PREFIX_MOUNT = f'singularity run --no-home --bind {cwd} {pth}'
    PREFIX_MOUNT = PREFIX_MOUNT = f'singularity run --home={cwd}:/home/ {pth}'
except FileNotFoundError:
    try:
        _ = subprocess.run('docker', check=False)
        cwd = os.getcwd()
        PREFIX = f'docker run -p {port}:{port} --platform=linux/amd64 ldpred2'
        PREFIX_MOUNT = (
            f'docker run -p {port}:{port} ' +
            f'--mount type=bind,source={cwd},target={cwd} --platform=linux/amd64 ldpred2')
    except FileNotFoundError as e:
        raise FileNotFoundError(
            'Neither `singularity` nor `docker` found in PATH.' +
            'Can not run tests!') from e


def test_assert():
    """dummy test that should pass"""
    assert True


def test_ldpred2_R():
    call = f'{PREFIX} R --version'
    out = subprocess.run(call.split(' '), check=True)
    assert out.returncode == 0


def test_ldpred2_Rscript():
    call = f'{PREFIX} Rscript --version'
    out = subprocess.run(call.split(' '), check=True)
    assert out.returncode == 0


def test_ldpred2_R_packages():
    if PREFIX.rfind('docker') >= 0:
        call = f'{PREFIX_MOUNT} Rscript {cwd}/tests/extras/r.R'
    else:
        call = f'{PREFIX_MOUNT} Rscript tests/extras/r.R'
    out = subprocess.run(call.split(' '), check=True)
    assert out.returncode == 0


def test_ldpred2_bin_prsice():
    call = f'{PREFIX} PRSice --version'
    out = subprocess.run(call.split(' '), check=True)
    assert out.returncode == 0


def test_ldpred2_bin_plink():
    call = f'{PREFIX} plink --version'
    out = subprocess.run(call.split(' '), check=True)
    assert out.returncode == 0


def test_ldpred2_bin_plink2():
    call = f'{PREFIX} plink2 --version'
    out = subprocess.run(call.split(' '), check=True)
    assert out.returncode == 0


def test_ldpred2_Rscript_LDpred2():
    if PREFIX.rfind('docker') >= 0:
        call = f'{PREFIX_MOUNT} Rscript {cwd}/scripts/LDpred2/ldpred2.R --help'
    else:
        call = f'{PREFIX_MOUNT} Rscript scripts/LDpred2/ldpred2.R --help'
    out = subprocess.run(call.split(' '), check=True)
    assert out.returncode == 0

def test_ldpred2_Rscript_PRSice():
    if PREFIX.rfind('docker') >= 0:
        call = f'{PREFIX_MOUNT} Rscript {cwd}/scripts/PRSice2/PRSice.R --help'
    else:
        call = f'{PREFIX_MOUNT} Rscript scripts/PRSice2/PRSice.R --help'
    out = subprocess.run(call.split(' '), check=True)
    assert out.returncode == 0
