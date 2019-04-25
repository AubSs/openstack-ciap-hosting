# CIAP OCTANE Openstack

## What is OCTANE ?

**OCTANE** is:

* A CIAP (**C**loud **I**nternet **A**ccess **P**oint). Mainly, it is a **security product** between Internet and your public application hosted in your private zone
* The acronym (with imagination and goodwill) of **Opensource cIAP Nextgen**
* A Societe Generale Open Source project developped within **Public Cloud Feature Team (Cloud Center Of Excellence)** by:
    * [Aubin LAGORCE](https://github.com/AubSs) for Openstack
    * [Eric BOUTEVILLE](https://github.com/qrn77) for [AWS](https://github.com/societe-generale/OCTANE)
* Is currently available for AWS, Azure and Openstack

**OCTANE** can:

* **Securly expose** a WebSite to Internet
* Protect you against **intrusions** (SQL injection, cross-site scripting (XSS), file inclusion...) & **virus**
* Limit you against **deny of service**
* Detect **malicious activities** or **policy violations**
* Securly **connect your external users** to your internal zone
* Collect **all the logs** and provide **metrics, search and analytics**
* Be **easly derivated on other x86** (GCP, Bare-Metal, etc.) platform in order to have **the same Internet Access Point in a multi-cloud context**


## How OCTANE is designed ?

There are several layers (from the most exposed -Internet- to the less exposed -Internal-):

* redundant load-balancers
* redundant filtering layer
* redundant reverse-proxies
* redundant proxies with SSL terminaison
* redundant WAF or TCP relay (it depends on the protocol used)
* redundant Antivirus & IDS
* redundant VPN
* redundant firewalls

Those functionnalities are deployed by:
* The **heat template** aims to build the Openstack infrastructure
* The **ansible playbook** will configure all software components


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

## Misc

Reach openstack vm outside host

```sh
echo 1 > /proc/sys/net/ipv4/ip_forward
echo 1 > /proc/sys/net/ipv4/conf/ens160/proxy_arp
iptables -t nat -A POSTROUTING -o ens160 -j MASQUERADE
```

Get latest openstack sdk

```sh
sudo pip3 install git+https://github.com/openstack/openstacksdk.git
```
