#!/usr/bin/python


################################################################################
# Imports
################################################################################
from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest
import json

################################################################################
# Main
################################################################################


#def main():
#    module = GcpModule(argument_spec=dict(filters=dict(type='list', elements='str'), region=dict(required=True, type='str')))
#
#    if not module.params['scopes']:
#        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']
#
#    zones = map(returnZoneStr, fetch_list(module, zonesCollection(module), zoneQuery(module)))
#
#    return_list = []
#
#    for zone in zones:
#        module.params['zone'] = zone
#        return_list = return_list + fetch_list(module, collection(module), query_options(module.params['filters']) )
#
#    return_value = {'resources': return_list}
#
#    module.exit_json(**return_value)


def fetch_instance_info_by_region(module):
    zones = map(returnZoneStr, fetch_list(module, zonesCollection(module), zoneQuery(module)))

    return_list = []

    for zone in zones:
        module.params['zone'] = zone
        return_list = return_list + fetch_list(module, collection(module), query_options(module.params['filters']) )

    return return_list


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


#if __name__ == "__main__":
#    main()
