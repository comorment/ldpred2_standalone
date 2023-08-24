#!/bin/sh
#SBATCH --job-name=$JOBNAME
#SBATCH --account=$ACCOUNT
#SBATCH --open-mode=truncate
#SBATCH --output=${JOBNAME}.out
#SBATCH --error=${JOBNAME}.err
#SBATCH --time=$WALLTIME
#SBATCH --cpus-per-task=$CPUS_PER_TASK
#SBATCH --mem-per-cpu=$MEM_PER_CPU

module load $SINGULARITY_MODULE

export ROOTDIR="$(dirname ${PWD})"
export SINGULARITY_BIND="$ROOTDIR/reference:/REF:ro"  # mount reference directory as /REF
export SIF=${ROOTDIR}/containers
export R="singularity exec --home=$PWD:/home --cleanenv $SIF/ldpred2.sif R"
export RSCRIPT="singularity exec --home=$PWD:/home --cleanenv $SIF/ldpred2.sif Rscript"

# Run some commands
$R --version  # print version
$RSCRIPT --version  # print version
