# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the vyos_bgp_address_family module
"""


class Bgp_address_familyArgs(object):  # pylint: disable=R0903
    """The arg spec for the vyos_bgp_address_family module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "running_config": {},
        "state": {
            "default": "merged",
            "type": "str",
            "choices": [
                "merged",
                "replaced",
                "deleted",
                "gathered",
                "parsed",
                "rendered",
                "purged",
                "overridden",
            ],
        },
        "config": {
            "type": "dict",
            "options": {
                "neighbors": {
                    "elements": "dict",
                    "type": "list",
                    "options": {
                        "address_family": {
                            "elements": "dict",
                            "type": "list",
                            "options": {
                                "nexthop_local": {"type": "bool"},
                                "soft_reconfiguration": {"type": "bool"},
                                "unsupress_map": {"type": "str"},
                                "nexthop_self": {"type": "bool"},
                                "weight": {"type": "int"},
                                "prefix_list": {
                                    "elements": "dict",
                                    "type": "list",
                                    "options": {
                                        "action": {
                                            "type": "str",
                                            "choices": ["export", "import"],
                                        },
                                        "prefix_list": {"type": "str"},
                                    },
                                },
                                "default_originate": {"type": "str"},
                                "distribute_list": {
                                    "elements": "dict",
                                    "type": "list",
                                    "options": {
                                        "action": {
                                            "type": "str",
                                            "choices": ["export", "import"],
                                        },
                                        "acl": {"type": "int"},
                                    },
                                },
                                "allowas_in": {"type": "int"},
                                "filter_list": {
                                    "elements": "dict",
                                    "type": "list",
                                    "options": {
                                        "action": {
                                            "type": "str",
                                            "choices": ["export", "import"],
                                        },
                                        "path_list": {"type": "str"},
                                    },
                                },
                                "route_server_client": {"type": "bool"},
                                "attribute_unchanged": {
                                    "type": "dict",
                                    "options": {
                                        "as_path": {"type": "bool"},
                                        "med": {"type": "bool"},
                                        "next_hop": {"type": "bool"},
                                    },
                                },
                                "peer_group": {"type": "str"},
                                "maximum_prefix": {"type": "int"},
                                "route_reflector_client": {"type": "bool"},
                                "route_map": {
                                    "elements": "dict",
                                    "type": "list",
                                    "options": {
                                        "action": {
                                            "type": "str",
                                            "choices": ["export", "import"],
                                        },
                                        "route_map": {"type": "str"},
                                    },
                                },
                                "capability": {
                                    "type": "dict",
                                    "options": {
                                        "orf": {
                                            "type": "str",
                                            "choices": ["send", "receive"],
                                        },
                                        "dynamic": {"type": "bool"},
                                    },
                                },
                                "remove_private_as": {"type": "bool"},
                                "as_override": {"type": "bool"},
                                "afi": {
                                    "type": "str",
                                    "choices": ["ipv4", "ipv6"],
                                },
                            },
                        },
                        "neighbor_address": {"type": "str"},
                    },
                },
                "as_number": {"type": "int"},
                "address_family": {
                    "elements": "dict",
                    "type": "list",
                    "options": {
                        "afi": {"type": "str", "choices": ["ipv4", "ipv6"]},
                        "redistribute": {
                            "elements": "dict",
                            "type": "list",
                            "options": {
                                "table": {"type": "str"},
                                "metric": {"type": "int"},
                                "protocol": {
                                    "type": "str",
                                    "choices": [
                                        "connected",
                                        "kernel",
                                        "ospf",
                                        "ospfv3",
                                        "rip",
                                        "ripng",
                                        "static",
                                    ],
                                },
                                "route_map": {"type": "str"},
                            },
                        },
                        "networks": {
                            "elements": "dict",
                            "type": "list",
                            "options": {
                                "backdoor": {"type": "bool"},
                                "prefix": {"type": "str"},
                                "path_limit": {"type": "int"},
                                "route_map": {"type": "str"},
                            },
                        },
                        "aggregate_address": {
                            "elements": "dict",
                            "type": "list",
                            "options": {
                                "summary_only": {"type": "bool"},
                                "prefix": {"type": "str"},
                                "as_set": {"type": "bool"},
                            },
                        },
                    },
                },
            },
        },
    }  # pylint: disable=C0301