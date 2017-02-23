GLOBAL_PRELOAD_PARAMETERS = {
# heat template parameter values common to all heat template continaing these parameters
     "defaults" : { 
        'key_name' : 'vfw_key${uuid}',
        "pub_key" : "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAqqnA9BAiMLtjOPSYBfhzLu4CiBolWoskDg4KVwhTJVTTeB6CqrQNcadlGXxOHhCYuNCKkUmIVF4WTOisVOJ75Z1c4OMoZLL85xVPKSIeH63kgVugwgPYQu55NbbWX+rsbUha3LnElDhNviMM3iTPbD5nnhKixNERAJMTLKXvZZZGqxW94bREknYPQTT2qrk3YRqwldncopp6Nkgv3AnSJz2gc9tjxnWF0poTQnQm/3D6hiJICrzKfAV0EaPN0KdtYjPhKrYoy6Qb/tKOVaaqsvwfKBJGrT9LfcA7D7M/yj292RT1XN63hI84WC383LsaPJ6eWdDTE6zUP1eGTWCoOw== rsa-key-20161026",
        "repo_user" : "${nexus_username}",
        "repo_passwd" : "${nexus_password}",
        "ecomp_private_net_id" : "${network}",
        "ecomp_private_subnet_id" : "${network}",
        "ecomp_private_net_cidr" : "10.0.0.0/8",
        "dcae_collector_ip" : "10.0.4.102",
        "dcae_collector_port" : "8080",

    },
# heat template parameter values for heat template instances created during Vnf-Orchestration test cases
    "Vnf-Orchestration" : {                         
        "vfw_preload.template": { 
            "repo_url" : "${nexus_repo}/org.openecomp.demo/vfw/${artifacts_version}",
            "unprotected_private_net_id" : "vofwl01_unprotected",
            "unprotected_private_net_cidr" : "192.168.10.0/24",
            "protected_private_net_id" : "vofwl01_protected",
            "protected_private_net_cidr" : "192.168.20.0/24",
            "vfw_private_ip_0" : "192.168.10.100",
            "vfw_private_ip_1" : "192.168.20.100",
            "vfw_private_ip_2" : "10.1.${ecompnet}.1",
            "vpg_private_ip_0" : "192.168.10.200",
            "vpg_private_ip_1" : "10.1.${ecompnet}.2",
            "vsn_private_ip_0" : "192.168.20.250",
            "vsn_private_ip_1" : "10.1.${ecompnet}.3",
            'vfw_name_0':'vofwl01fwl${hostid}', 
            'vpg_name_0':'vofwl01pgn${hostid}', 
            'vsn_name_0':'vofwl01snk${hostid}',
        },
        "vlb_preload.template" : { 
            "repo_url" : "${nexus_repo}/org.openecomp.demo/vlb/${artifacts_version}",
            "vlb_private_net_id" : "volb01_private",
            "vlb_private_net_cidr" : "192.168.30.0/24",
            "vlb_private_ip_0" : "192.168.30.100",
            "vlb_private_ip_1" : "10.1.${ecompnet}.4",
            "vdns_private_ip_0" : "192.168.30.110",
            "vdns_private_ip_1" : "10.1.${ecompnet}.5",
            'vlb_name_0':'vovlblb${hostid}',
            'vdns_name_0':'vovlbdns${hostid}', 
        },
        "dnsscaling_preload.template" : { 
            "repo_url" : "${nexus_repo}/org.openecomp.demo/vlb/${artifacts_version}",
            "vlb_private_net_id" : "volb01_private",
            "vlb_private_ip_0" : "192.168.30.100",
            "vlb_private_ip_1" : "10.1.${ecompnet}.4",
            "vdns_private_ip_0" : "192.168.30.222",
            "vdns_private_ip_1" : "10.1.${ecompnet}.6",
            'scaling_vdns_name_0':'vovlbscaling${hostid}',
        },
        "vvg_preload.template" : { 
        }
    },
# heat template parameter values for heat template instances created during Closed-Loop test cases
    "Closed-Loop" : {                         
		"vfw_preload.template": { 
            "repo_url" : "${nexus_repo}/org.openecomp.demo/vfw/${artifacts_version}",
            "unprotected_private_net_id" : "clfwl01_unprotected",
            "unprotected_private_net_cidr" : "192.168.110.0/24",
            "protected_private_net_id" : "clfwl01_protected",
            "protected_private_net_cidr" : "192.168.120.0/24",
            "vfw_private_ip_0" : "192.168.110.100",
            "vfw_private_ip_1" : "192.168.120.100",
            "vfw_private_ip_2" : "10.1.${ecompnet}.11",
            "vpg_private_ip_0" : "192.168.110.200",
            "vpg_private_ip_1" : "10.1.${ecompnet}.12",
            "vsn_private_ip_0" : "192.168.120.250",
            "vsn_private_ip_1" : "10.1.${ecompnet}.13",
            'vfw_name_0':'clfwl01fwl${hostid}', 
            'vpg_name_0':'clfwl01pgn${hostid}', 
            'vsn_name_0':'clfwl01snk${hostid}',
        },
        "vlb_preload.template" : { 
            "repo_url" : "${nexus_repo}/org.openecomp.demo/vlb/${artifacts_version}",
            "vlb_private_net_id" : "cllb01_private",
            "vlb_private_net_cidr" : "192.168.130.0/24",
            "vlb_private_ip_0" : "192.168.130.100",
            "vlb_private_ip_1" : "10.1.${ecompnet}.14",
            "vdns_private_ip_0" : "192.168.130.110",
            "vdns_private_ip_1" : "10.1.${ecompnet}.15",
            'vlb_name_0':'clvlblb${hostid}',
            'vdns_name_0':'clvlbdns${hostid}', 
        },
        "dnsscaling_preload.template" : { 
            "repo_url" : "${nexus_repo}/org.openecomp.demo/vlb/${artifacts_version}",
            "vlb_private_net_id" : "cllb01_private",
            "vlb_private_ip_0" : "192.168.130.100",
            "vlb_private_ip_1" : "10.1.${ecompnet}.14",
            "vdns_private_ip_0" : "192.168.130.222",
            "vdns_private_ip_1" : "10.1.${ecompnet}.16",
            'scaling_vdns_name_0':'clvlbscaling${hostid}',
        },
        "vvg_preload.template" : { 
        }
    },
 # heat template parameter values for heat template instances created for hands on demo test case
   "Demo" : {                         
        "vfw_preload.template": { 
            "repo_url" : "${nexus_repo}/org.openecomp.demo/vfw/${artifacts_version}",
            "unprotected_private_net_id" : "demofwl_unprotected",
            "unprotected_private_net_cidr" : "192.168.110.0/24",
            "protected_private_net_id" : "demofwl_protected",
            "protected_private_net_cidr" : "192.168.120.0/24",
            "vfw_private_ip_0" : "192.168.110.100",
            "vfw_private_ip_1" : "192.168.120.100",
            "vfw_private_ip_2" : "10.1.${ecompnet}.11",
            "vpg_private_ip_0" : "192.168.110.200",
            "vpg_private_ip_1" : "10.1.${ecompnet}.12",
            "vsn_private_ip_0" : "192.168.120.250",
            "vsn_private_ip_1" : "10.1.${ecompnet}.13",
            'vfw_name_0':'demofwl01fwl', 
            'vpg_name_0':'demofwl01pgn', 
            'vsn_name_0':'demofwl01snk',
        },
        "vlb_preload.template" : { 
            "repo_url" : "${nexus_repo}/org.openecomp.demo/vlb/${artifacts_version}",
            "vlb_private_net_id" : "demolb_private",
            "vlb_private_net_cidr" : "192.168.130.0/24",
            "vlb_private_ip_0" : "192.168.130.100",
            "vlb_private_ip_1" : "10.1.${ecompnet}.14",
            "vdns_private_ip_0" : "192.168.130.110",
            "vdns_private_ip_1" : "10.1.${ecompnet}.15",
            'vlb_name_0':'demovlblb',
            'vdns_name_0':'demovlbdns', 
        },
        "dnsscaling_preload.template" : { 
            "repo_url" : "${nexus_repo}/org.openecomp.demo/vlb/${artifacts_version}",
            "vlb_private_net_id" : "demolb_private",
            "vlb_private_ip_0" : "192.168.130.100",
            "vlb_private_ip_1" : "10.1.${ecompnet}.14",
            "vdns_private_ip_0" : "192.168.130.222",
            "vdns_private_ip_1" : "10.1.${ecompnet}.16",
            'scaling_vdns_name_0':'demovlbscaling',
        },
        "vvg_preload.template" : { 
        }
    }
}
    
