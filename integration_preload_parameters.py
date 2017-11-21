GLOBAL_PRELOAD_PARAMETERS = {
# heat template parameter values common to all heat template continaing these parameters
     "defaults" : {
        'key_name' : 'vfw_key${uuid}',
        "pub_key" : "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAqqnA9BAiMLtjOPSYBfhzLu4CiBolWoskDg4KVwhTJVTTeB6CqrQNcadlGXxOHhCYuNCKkUmIVF4WTOisVOJ75Z1c4OMoZLL85xVPKSIeH63kgVugwgPYQu55NbbWX+rsbUha3LnElDhNviMM3iTPbD5nnhKixNERAJMTLKXvZZZGqxW94bREknYPQTT2qrk3YRqwldncopp6Nkgv3AnSJz2gc9tjxnWF0poTQnQm/3D6hiJICrzKfAV0EaPN0KdtYjPhKrYoy6Qb/tKOVaaqsvwfKBJGrT9LfcA7D7M/yj292RT1XN63hI84WC383LsaPJ6eWdDTE6zUP1eGTWCoOw== rsa-key-20161026",
        "repo_url_blob" : "https://nexus.onap.org/content/repositories/raw",
        "repo_url_artifacts" : "https://nexus.onap.org/content/groups/staging",
        "demo_artifacts_version" : "${GLOBAL_INJECTED_ARTIFACTS_VERSION}",
        "onap_private_net_id" : "${GLOBAL_INJECTED_NETWORK}",
        "onap_private_subnet_id" : "${GLOBAL_INJECTED_NETWORK}",
        "onap_private_net_cidr" : "10.0.0.0/8",
        "dcae_collector_ip" : "10.0.4.102",
        "dcae_collector_port" : "8080",
        "public_net_id" : "${GLOBAL_INJECTED_PUBLIC_NET_ID}",
        "cloud_env" : "${GLOBAL_INJECTED_CLOUD_ENV}",
   	    "install_script_version" : "${GLOBAL_INJECTED_SCRIPT_VERSION}",
    },

###
# heat template parameter values for heat template instances created during Vnf-Orchestration test cases
###
    "Vnf-Orchestration" : {
        "vfw_preload.template": {
            "unprotected_private_net_id" : "vofwl01_unprotected${hostid}",
            "unprotected_private_net_cidr" : "192.168.10.0/24",
            "protected_private_net_id" : "vofwl01_protected${hostid}",
            "protected_private_net_cidr" : "192.168.20.0/24",
            "vfw_private_ip_0" : "192.168.10.100",
            "vfw_private_ip_1" : "192.168.20.100",
            "vfw_private_ip_2" : "10.0.${ecompnet}.1",
            "vpg_private_ip_0" : "192.168.10.200",
            "vpg_private_ip_1" : "10.0.${ecompnet}.2",
            "vsn_private_ip_0" : "192.168.20.250",
            "vsn_private_ip_1" : "10.0.${ecompnet}.3",
            'vfw_name_0':'vofwl01fwl${hostid}',
            'vpg_name_0':'vofwl01pgn${hostid}',
            "vfw_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "vfw_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            'vsn_name_0':'vofwl01snk${hostid}'
        },
        "vlb_preload.template" : {
            "vlb_private_net_id" : "volb01_private${hostid}",
            "vlb_private_net_cidr" : "192.168.30.0/24",
            "vlb_private_ip_0" : "192.168.30.100",
            "vlb_private_ip_1" : "10.0.${ecompnet}.4",
            "vdns_private_ip_0" : "192.168.30.110",
            "vdns_private_ip_1" : "10.0.${ecompnet}.5",
            'vlb_name_0':'vovlblb${hostid}',
            'vdns_name_0':'vovlbdns${hostid}',
    	    "vlb_private_net_cidr" : "192.168.10.0/24",
            "vlb_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "vlb_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
  			"pktgen_private_net_cidr" : "192.168.9.0/24"

        },
        "dnsscaling_preload.template" : {
            "vlb_private_net_id" : "volb01_private${hostid}",
            "vlb_private_ip_0" : "192.168.30.100",
            "vlb_private_ip_1" : "10.0.${ecompnet}.4",
            "vdns_private_ip_0" : "192.168.30.222",
            "vdns_private_ip_1" : "10.0.${ecompnet}.6",
            'scaling_vdns_name_0':'vovlbscaling${hostid}',
    	    "vlb_private_net_cidr" : "192.168.10.0/24"
        },
        "vims_preload.template" : {
            "bono_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "sprout_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "homer_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "homestead_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "ralf_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "ellis_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "dns_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "bono_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "sprout_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "homer_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "homestead_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "ralf_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "ellis_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "dns_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "repo_url" : "http://repo.cw-ngv.com/stable",
            "zone" : "me.cw-ngv.com",
            "dn_range_start" : "2425550000",
            "dn_range_length" : "10000",
            "dnssec_key" : "9FPdYTWhk5+LbhrqtTPQKw=="

        },
        "vvg_preload.template" : {
        }
    },
# heat template parameter values for heat template instances created during Closed-Loop test cases
    "Closed-Loop" : {
		"vfw_preload.template": {
            "unprotected_private_net_id" : "clfwl01_unprotected${hostid}",
            "unprotected_private_net_cidr" : "192.168.110.0/24",
            "protected_private_net_id" : "clfwl01_protected${hostid}",
            "protected_private_net_cidr" : "192.168.120.0/24",
            "vfw_private_ip_0" : "192.168.110.100",
            "vfw_private_ip_1" : "192.168.120.100",
            "vfw_private_ip_2" : "10.0.${ecompnet}.11",
            "vpg_private_ip_0" : "192.168.110.200",
            "vpg_private_ip_1" : "10.0.${ecompnet}.12",
            "vsn_private_ip_0" : "192.168.120.250",
            "vsn_private_ip_1" : "10.0.${ecompnet}.13",
            'vfw_name_0':'clfwl01fwl${hostid}',
            'vpg_name_0':'clfwl01pgn${hostid}',
            "vfw_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "vfw_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            'vsn_name_0':'clfwl01snk${hostid}'
        },
        "vlb_preload.template" : {
            "vlb_private_net_id" : "cllb01_private${hostid}",
            "vlb_private_net_cidr" : "192.168.130.0/24",
            "vlb_private_ip_0" : "192.168.130.100",
            "vlb_private_ip_1" : "10.0.${ecompnet}.14",
            "vdns_private_ip_0" : "192.168.130.110",
            "vdns_private_ip_1" : "10.0.${ecompnet}.15",
            'vlb_name_0':'clvlblb${hostid}',
            'vdns_name_0':'clvlbdns${hostid}',
    	    "vlb_private_net_cidr" : "192.168.10.0/24",
  			"pktgen_private_net_cidr" : "192.168.9.0/24",
            "vlb_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "vlb_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}"
        },
        "dnsscaling_preload.template" : {
            "vlb_private_net_id" : "cllb01_private${hostid}",
            "vlb_private_ip_0" : "192.168.130.100",
            "vlb_private_ip_1" : "10.0.${ecompnet}.14",
            "vdns_private_ip_0" : "192.168.130.222",
            "vdns_private_ip_1" : "10.0.${ecompnet}.16",
            'scaling_vdns_name_0':'clvlbscaling${hostid}',
    	    "vlb_private_net_cidr" : "192.168.10.0/24"
        },
        "vims_preload.template" : {
            "bono_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "sprout_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "homer_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "homestead_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "ralf_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "ellis_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "dns_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "bono_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "sprout_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "homer_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "homestead_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "ralf_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "ellis_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "dns_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "repo_url" : "http://repo.cw-ngv.com/stable",
            "zone" : "me.cw-ngv.com",
            "dn_range_start" : "2425550000",
            "dn_range_length" : "10000",
            "dnssec_key" : "9FPdYTWhk5+LbhrqtTPQKw=="
        },
        "vvg_preload.template" : {
        }
    },
 # heat template parameter values for heat template instances created for hands on demo test case
   "Demo" : {
        "vfw_preload.template": {
            "unprotected_private_net_id" : "demofwl_unprotected",
            "unprotected_private_net_cidr" : "192.168.110.0/24",
            "protected_private_net_id" : "demofwl_protected",
            "protected_private_net_cidr" : "192.168.120.0/24",
            "vfw_private_ip_0" : "192.168.110.100",
            "vfw_private_ip_1" : "192.168.120.100",
            "vfw_private_ip_2" : "10.0.${ecompnet}.11",
            "vpg_private_ip_0" : "192.168.110.200",
            "vpg_private_ip_1" : "10.0.${ecompnet}.12",
            "vsn_private_ip_0" : "192.168.120.250",
            "vsn_private_ip_1" : "10.0.${ecompnet}.13",
            'vfw_name_0':'demofwl01fwl',
            'vpg_name_0':'demofwl01pgn',
            "vfw_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "vfw_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            'vsn_name_0':'demofwl01snk'
        },
        "vlb_preload.template" : {
            "vlb_private_net_id" : "demolb_private",
            "vlb_private_net_cidr" : "192.168.130.0/24",
            "vlb_private_ip_0" : "192.168.130.100",
            "vlb_private_ip_1" : "10.0.${ecompnet}.14",
            "vdns_private_ip_0" : "192.168.130.110",
            "vdns_private_ip_1" : "10.0.${ecompnet}.15",
            'vlb_name_0':'demovlblb',
            'vdns_name_0':'demovlbdns',
    	    "vlb_private_net_cidr" : "192.168.10.0/24",
            "vlb_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "vlb_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
  			"pktgen_private_net_cidr" : "192.168.9.0/24"
        },
        "dnsscaling_preload.template" : {
            "vlb_private_net_id" : "demolb_private",
            "vlb_private_ip_0" : "192.168.130.100",
            "vlb_private_ip_1" : "10.0.${ecompnet}.14",
            "vdns_private_ip_0" : "192.168.130.222",
            "vdns_private_ip_1" : "10.0.${ecompnet}.16",
            'scaling_vdns_name_0':'demovlbscaling',
    	    "vlb_private_net_cidr" : "192.168.10.0/24"
        },
        "vims_preload.template" : {
            "bono_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "sprout_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "homer_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "homestead_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "ralf_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "ellis_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "dns_image_name" : "${GLOBAL_INJECTED_VM_IMAGE_NAME}",
            "bono_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "sprout_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "homer_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "homestead_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "ralf_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "ellis_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "dns_flavor_name" : "${GLOBAL_INJECTED_VM_FLAVOR}",
            "repo_url" : "http://repo.cw-ngv.com/stable",
            "zone" : "me.cw-ngv.com",
            "dn_range_start" : "2425550000",
            "dn_range_length" : "10000",
            "dnssec_key" : "9FPdYTWhk5+LbhrqtTPQKw=="
        },
        "vvg_preload.template" : {
        }
    }
}

