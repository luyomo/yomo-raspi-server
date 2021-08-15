#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = ''' This is the test document '''

EXAMPLES = ''' This is the test example '''

RETURN = ''' Return example '''

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
from ansible.module_utils.tidb_utils import fetch_instance_info_by_region
import json, time

def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            filters=dict(type='list', elements='str'),
            description=dict(type='str'),
            instances=dict(type='list', elements='str'),
            name=dict(required=True, type='str'),
            region=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#targetPool'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False
    return_arr = []
    instance_arr = []
    ret = None

    if fetch:
        if state == 'present':
            instance_arr = list(map(lambda __entry: __entry['selfLink'], fetch_instance_info_by_region(module) ) )
            instance_2remove = instance_arr.copy()
            for instance in instance_arr:
                for fetchedInstance in fetch['instances']:
                    if instance == fetchedInstance:
                        instance_2remove.remove(instance)
            if len(instance_2remove) > 0:
                instance_2remove = list(map(lambda __entry: {"instance": __entry} , instance_2remove ) )
                ret = post(module, add_url(module), instance_2remove, kind)
                changed = True

        else:
            for instance in module.params.get('instances'):
                for fetchedInstance in fetch['instances']:
                    arrNameInstance = fetchedInstance.split('/')
                    if arrNameInstance[-1] == instance:
                        return_arr.append(delete_url(module))
                        instance_arr.append({u"instance" : fetchedInstance })
            if len(instance_arr) > 0:
                ret = post(module, delete_url(module), instance_arr, kind)
                changed = True

    module.exit_json(changed=changed, return_str=ret)

def post(module, link, instance_arr, kind):
    auth = GcpSession(module, 'compute')
    return  wait_for_operation(module, auth.post(link, {u"instances" : instance_arr}))

def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def delete_url(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/targetPools/{name}/removeInstance".format(**module.params)

def add_url(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/targetPools/{name}/addInstance".format(**module.params)

def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/targetPools/{name}".format(**module.params)

def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    result = decode_response(result, module)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result

def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    return op_result

def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)

def decode_response(response, module):
    if response['kind'] != 'compute#targetPool':
        return response

    # Map healthChecks[0] => healthCheck
    if 'healthChecks' in response:
        if not response['healthChecks']:
            response['healthCheck'] = response['healthChecks'][0]
            del response['healthChecks']

    return response

if __name__ == '__main__':
    main()
