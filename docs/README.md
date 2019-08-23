# Documentation

> Return to [Homepage](../README.md "Homepage")

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

usage: ciap.py [-h] [-c C] [--new | --delete | --list]

optional arguments:
  -h, --help  show this help message and exit
  -c C        Specifie config file (default ./ciap.ini)
  --new       Create a new CIAP
  --delete    Delete a CIAP
  --list      List all CIAP

# Create a new instance
$> python3 ciap.py --new -c <configuration file>

# Delete an instance
$> python3 ciap.py --delete -c <configuration file>

# List all CIAP instances
$> python3 ciap.py --list -c <configuration file>
```

### Build cIAP

Setup your configuration file (see below) (Must be a .ini file)

```ini
# For the [Openstack] section, all information are available in the clouds.yaml
# Look at https://docs.openstack.org/openstacksdk/latest/user/config/configuration.html
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
stack_name      = aubin             # [Required] Stack name
stack_template  = heat/main.yaml    # [Required] Openstack main stack template file
public_key_file = ~/.ssh/id_rsa.pub # [Required] SSH public key to install in admin server

[Orchestration]
server_image    = <uuid>    # [Required] Image used by the servers
public_net      = <string>  # [Required] Public Network name used by the ciap
server_flavor   = <string>  # [Required] Flavor used by the servers
deploy_plug     = <bool>    # [Optional] (Default to false) Deploy a demo plug
cidr            = <cidr/24> # [Required] CIDR used by the ciap
ssh_username    = <string>  # [Optional] (Default to `ciap`) SSH User to connect to the servers
ssh_public_key  = <string>  # [Optional] SSH public key to install in all servers
```

## Run

The admin server will check every five minutes for new instances available (Cron Job).
When it detect a new instance, it will automaticaly initiate it.

```sh
# List all stack and wait for 'CREATE_COMPLETE'
$> python3 ciap.py --list -c <configuration file>

===========================================
Name: ciap-aubin
Stack: CIAP OCTANE v4
ID: 7587c6e4-6fa4-4a91-a4ed-5d13dbf491e3
Created at: 2019-07-04T13:58:59Z
Status: CREATE_COMPLETE
SSH user: ciap
Floating IP address of ciap: 192.168.1.247
Floating IP address of admin server: 192.168.1.225

# Connect to the admin server
$> ssh <SSH user>@<Floating IP address of admin server>
```

Check Ansible folder to understand how the CIAP Hosting work
