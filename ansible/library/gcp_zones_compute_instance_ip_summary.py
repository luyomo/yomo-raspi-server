#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
'''

EXAMPLES = '''
'''

RETURN = '''
'''

################################################################################
# Imports
################################################################################
from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict(filters=dict(type='list', elements='str'), region=dict(required=True, type='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    zones = map(returnZoneStr, fetch_list(module, zonesCollection(module), zoneQuery(module)))

    return_list = []
    return_dict = {}

    for zone in zones:
        module.params['zone'] = zone
        instanceList = fetch_list(module, collection(module), query_options(module.params['filters']) )
        for instanceInfo in instanceList:
            if return_dict.get(instanceInfo['labels']['component']) == None:
                return_dict[instanceInfo['labels']['component']] = [ instanceInfo["networkInterfaces"][0]['networkIP'] ]
            else:
                return_dict[instanceInfo['labels']['component']].append(instanceInfo["networkInterfaces"][0]['networkIP'])

            if return_dict.get('all') == None:
                return_dict['all'] = [ instanceInfo["networkInterfaces"][0]['networkIP'] ]
            else:
                return_dict['all'].append(instanceInfo["networkInterfaces"][0]['networkIP'])

            if instanceInfo["networkInterfaces"][0].get("accessConfigs") != None:
                return_dict['externalIP'] = instanceInfo["networkInterfaces"][0].get("accessConfigs")[0].get("natIP")

    return_value = { 'resources': return_dict }

    module.exit_json(**return_value)


def returnZoneStr(zoneInfo):
    return zoneInfo["name"]

def collection(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instances".format(**module.params)

def zonesCollection(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/zones".format(**module.params)

def zoneQuery(module):
    return 'region="https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}"'.format(**module.params)


def fetch_list(module, link, query):
    auth = GcpSession(module, 'compute')
    return auth.list(link, return_if_object, array_name='items', params={'filter': query})


def query_options(filters):
    if not filters:
        return ''

    if len(filters) == 1:
        return filters[0]
    else:
        queries = []
        for f in filters:
            # For multiple queries, all queries should have ()
            if f[0] != '(' and f[-1] != ')':
                queries.append("(%s)" % ''.join(f))
            else:
                queries.append(f)

        return ' '.join(queries)


def return_if_object(module, response):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


if __name__ == "__main__":
    main()
