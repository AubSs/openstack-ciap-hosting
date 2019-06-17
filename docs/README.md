# Documentation

> [Homepage](../README.md "Homepage")

#### Summary

* [Requirements](#requirements)
* [Pre build](#pre-build)
* [Build](#build)
    - [CLI](#cli)
    - [Build cIAP](#build-ciap)
* [Run](#run)


## Requirements

* An Openstack **Stein** version with these modules :
    * Cinder
    * Neutron
    * Glance
    * Swift
    * Heat
    * Octavia
    * Ceilometer
    * Aodh
    * Horizon

* Python 3.6


## Pre build

On a host that can reach the Openstack API, simply install Openstack Python SDK.
```sh
pip install openstacksdk
```
Then clone OCTANE repository.
```sh
git clone <<path to github.com repository>> (eg https://github.com/societe-generale/OCTANE.git)
```


## Build

### CLI

```
$> python3 ciap.py -h

usage: ciap.py [-h] [-c C] [--new <user> | --delete <user> | --list]

optional arguments:
  -h, --help       show this help message and exit
  -c C             Specifie config file (default ./ciap.ini)
  --new <user>     Create a new CIAP
  --delete <user>  Delete a CIAP
  --list           List all CIAP

# Create a new instance
$> python3 ciap.py --new <stack name> -c <configuration file>

# Delete an instance
$> python3 ciap.py --delete <stack name> -c <configuration file>

# List all CIAP instances
$> python3 ciap.py --list -c <configuration file>
```

### Build cIAP

Setup your configuration file (see below)

```ini
[Openstack]
auth_url = http://192.168.1.48/identity/v3
username = admin
password = xxxx
project_id = 5925a4a86d4e4434a94c558df006bfdf
project_name = admin
user_domain_name = Default
project_domain_name = default
region_name = RegionOne
interface = public
identity_api_version = 3

[CIAP]
stack_name      = aubin
stack_template  = heat/main.yaml
public_key_file = ~/.ssh/id_rsa.pub

[Orchestration]
server_image    = <uuid>    # [Required] Image used by the servers
public_net      = <string>  # [Required] Public Network name used by the ciap
server_flavor   = <string>  # [Required] Flavor used by the servers
deploy_plug     = <bool>    # [Optional] (Default to false) Deploy a demo plug
cidr            = <cidr/22> # [Required] CIDR used by the ciap
ssh_username    = <string>  # [Optional] (Default to `ciap`) SSH User to connect to the servers
ssh_public_key  = <string>  # [Optional] SSH public key to install in all servers
```

## Run

