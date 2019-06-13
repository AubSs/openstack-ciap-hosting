# Documentation

[Homepage](../README.md "Homepage")


## How to use OCTANE ?

### Requirements

* An Openstack **Stein** version with these modules:
    * Cinder
    * Neutron
    * Glance
    * Swift
    * Heat
    * Octavia
    * Ceilometer
    * Aodh
    * Horizon

* Python 3.6 (or >) with these modules:
    * openstacksdk

### CLI
Setup your configuration file (see below)

```sh
# Create a new instance
python3 ciap.py --new <stack name> -c <configuration file>

# Delete an instance
python3 ciap.py --delete <stack name> -c <configuration file>

# List all CIAP instances
python3 ciap.py --list -c <configuration file>
```

### Configuration file

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
public_net      = <string>  # [Optional] Public Network name used by the ciap
server_flavor   = <string>  # [Optional] Flavor used by the servers
deploy_plug     = <bool>    # [Optional] (Default to false) Deploy a demo plug
cidr            = <cidr/22> # [Optional] CIDR used by the ciap
ssh_username    = <string>  # [Optional] SSH User to connect to the servers
ssh_public_key  = <string>  # [Optional] SSH public key to install in all servers
```

Get latest openstack sdk

```sh
sudo pip3 install git+https://github.com/openstack/openstacksdk.git
```
