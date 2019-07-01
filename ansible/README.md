# Ansible Playbook

> Return to [Homepage](../README.md "Homepage")

#### Summary

* [Presentation](#presentation)
* [Roles](#roles)
* [Usage](#usage)
* [Ansible Dynamic Inventory](#ansible-dynamic-inventory)
* [Ansible configuration](#ansible-configuration)

## Presentation

We presupose the reader has minimal knowledge on :
* Openstack technologies
* Python
* Ansible

First of all you will need to have a proper Openstack environment and sufficient authorizations to perform all actions.


## Roles

There are six roles:

* common : common tasks
* healtcheck : role use to setup health endpoint for autoscaled instances
* lb : shunt streams based on rules
* waf : performs security tasks for HTTP/HTTPS streams
* vpn : grant customers access to theirs instances
* fw : filter access to customers instances
* met : statistics about this instances

> For more details look at [Roles documentation](roles/README.md "Roles documentation")

## Usage

A CLI is provided. This CLI is one python script.

```
./cli.py -h

usage: cli.py [-h] [--list-hosts] [--list-tags] [--tags TAGS [TAGS ...]]
              [--hosts HOSTS [HOSTS ...]] [--playbook PLAYBOOK]

CLI API for OCTANE

optional arguments:
  -h, --help            show this help message and exit

Info:
  --list-hosts          List all available hosts
  --list-tags           List all available tags

Execute:
  --tags TAGS [TAGS ...]    Only run tasks tagged with these values
  --hosts HOSTS [HOSTS ...] Only run hosts roles
  --playbook PLAYBOOK       Specify ansible playbook (Default: main.yml)
```

For exemple, if you want to initialize only the plug, then :
```bash
./cli.py --hosts plug --tags init
```


## Ansible Dynamic Inventory

```
./openstack-inventory.py  -h

usage: openstack-inventory.py [-h] [--public] (--list | --host HOST)

Build an Ansible inventory based on group.

optional arguments:
  -h, --help   show this help message and exit
  --public     Use public address for ansible host
  --list       List active servers
  --host HOST  List details about the specific host
```


## Ansible configuration

An `ansible.cfg` is present on the current directory with :
```ini
[defaults]
retry_files_enabled = false
inventory = openstack-inventory.py
stdout_callback = debug
host_key_checking = false
```
