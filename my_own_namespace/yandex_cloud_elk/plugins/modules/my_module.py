#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

DOCUMENTATION = r'''
---
module: my_module

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    path:
        description: This is absolute file path.
        required: true
        type: str
    content:
        description: Put there content for file
        required: true
        type: str

# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name

author:
    - Bambrino
'''

EXAMPLES = r'''
# Pass in a message
- path: Test with a message
  my_namespace.my_collection.my_module:
    path: '/tmp/some_dir/some_file.ext'
    content: 'some strings'

'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.

message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'File exists'

'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed = True,
        message = ''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # try:
    if os.access(module.params['path'], os.R_OK):
        result['changed'] = False
        result['message'] = 'File exists'
    if not os.path.exists(os.path.split(module.params['path'])[0]):
        os.makedirs(os.path.split(module.params['path'])[0])
    if not os.path.exists(module.params['path']):
        with open(module.params['path'], 'w', encoding='utf-8') as fp:
            fp.write(module.params['content'])
            result['changed'] = True
            result['message'] = 'File created'

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
