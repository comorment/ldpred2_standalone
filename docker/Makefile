all: ldpred2_standalone.sif  # additional .sif files may be listed here for corresponding dockerfiles

%.sif: dockerfiles/%/Dockerfile
	docker build -t $* -f dockerfiles/$*/Dockerfile . && \
	scripts/convert_docker_image_to_singularity.sh $* && \
	scripts/move_singularity_file.sh $*

# Example commands executed by this make file
# 
# Run "make ldpred2_standalone.sif" will trigger this:
# docker build -t ldpred2_standalone -f dockerfiles/ldpred2_standalone/Dockerfile . && \  # build docker container
#     scripts/convert_docker_image_to_singularity.sh ldpred2_standalone && \         # produces ldpred2_standalone.sif
#     scripts/move_singularity_file.sh ldpred2_standalone        # moves ldpred2_standalone.sif to ../containers/.
#  
# Run "make all" will build all singularity containers in this project
