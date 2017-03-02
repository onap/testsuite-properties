#!/bin/bash

#
# Execute tags built to support the hands on demo,
# init - Distributes models demoVFW and demoVLB, and creates customer "Demonstration"
# preload - Preloads the VNF <vnf_name> that was provided in the VID interface and
#           preloads the <module_name> that will be provided to VID when instantiating the VNF
#
# appc - Will configure APPC for the VFW <module_name> for a closed loop test
#

# Set the defaults
if [ $# -eq 0 ];then
	echo "Usage: demo.sh init"
	echo "       demo.sh preload <vnf_name> <module_name>"
	echo "       demo.sh appc <module_name>"
	exit
fi
##
## if more than 1 tag is supplied, the must be provided with -i or -e
##
while [ $# -gt 0 ]
do
	key="$1"

	case $key in
    	init)
    	TAG="InitDemo"
    	shift
    	;;
    	preload)
    	TAG="PreloadDemo"
    	shift
    	if [ $# -ne 2 ];then
			echo "Usage: demo.sh preload <vnf_name> <module_name>"
			exit
		fi
    	VARIABLES="$VARIABLES -v VNF_NAME:$1"
    	shift
    	VARIABLES="$VARIABLES -v MODULE_NAME:$1"
    	shift
    	;;
    	appc)
    	TAG="APPCMountPointDemo"
    	shift
    	if [ $# -ne 1 ];then
			echo "Usage: demo.sh appc <module_name>"
			exit
		fi
    	VARIABLES="$VARIABLES -v MODULE_NAME:$1"
    	shift
    	;;
    	*)
    	echo "Usage: demo.sh init"
    	echo "       demo.sh preload <vnf_name> <module_name>"
   	    echo "       demo.sh appc <module_name>"
    	exit
	esac
done

ETEHOME=/var/opt/OpenECOMP_ETE
VARIABLEFILES="-V /share/config/vm_properties.py -V /share/config/integration_robot_properties.py -V /share/config/integration_preload_parameters.py"
docker exec openecompete_container ${ETEHOME}/runTags.sh ${VARIABLEFILES} ${VARIABLES} -d /share/logs/demo/${TAG} -i ${TAG} --display 89 2> ${TAG}.out