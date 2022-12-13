Role Name
=========

This single task role running my_module

Requirements
------------

There is no any special requirements

Role Variables
--------------

Role vars:
* {{ path_string }}    : string with absolute file path for creation
* {{ content_string }} : string containing file content

defaul params:
```yaml
path_string: '/tmp/some_file.txt'
content_string: 'some strings here'
```

Example Playbook
----------------
```yaml
- name: Create file 
  my_module:
    path: {{ path_string }}
    content: {{ content_sting }}
```
License
-------

BSD

Author Information
------------------

Bambrino
