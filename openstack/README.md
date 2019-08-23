# Bring up a complete OpenStack environment

> Return to [Homepage](../README.md "Homepage")

The purpose of this page is to provide a guide for installing an OpenStack Stein version with all the modules necessary for the deployment of a CIAP.

**This guide is not intended for a production-ready environment, but only for testing purposes.**

#### Summary

* [Requirements](#requirements)
* [Optional Set up a VMware ESXi Hypervisor](optional-set-up-a-vmware-esxi-hypervisor)
* [Set up a fully working environment](#set-up-a-fully-working-environment)
    * [Install Linux (Ubuntu 18.04 LTS)](#install-linux-(ubuntu-18.04-lts))
    * [Add Stack User](#add-stack-user)
    * [Download DevStack](#download-devstack)
    * [Create a local.conf](#create-a-local.conf)
    * [Start the install](#start-the-install)
* [Post installation](#post-installation)
    * [Download and install images](#download-and-install-images)
    * [Reach openstack instances outside host machine](#reach-openstack-instances-outside-host-machine)
* [Profit!](#profit!)


## Requirements

The following minimum requirements should support a proof-of-concept environment with core services and several instances :

* Min 1 processor / 6 cores
* 32 GB memory
* 200 GB storage


## Optional Set up a VMware ESXi Hypervisor

For testing the cIAP, it’s strongly recommended to use a clean virtual machine. Using Public Cloud (AWS, Azure, GCP and so on) is not recommended since configuring the network will be difficult. Another way is to use a host on VMware ESXi. If this solution is chosen, do not forget to change the NIC teaming, however, Openstack instances will not be able to reach internet.

To do that :

* Go to the VMware vSphere WebClient
* Go to networking
* Edit the settings of your virtual switches
* Extend NIC teaming
* Change Load balancing to "Route based on IP hash"


## Set up a fully working environment

### Install Linux (Ubuntu 18.04 LTS)

Start with a clean and minimal install of a Linux system. DevStack attempts to support the two latest LTS releases of Ubuntu, the latest/current Fedora version, CentOS/RHEL 7, as well as Debian and OpenSUSE.

Currently, Ubuntu 18.04 (Bionic Beaver) is the most tested, and will go the smoothest so it's warmly encouraged to use it.

### Add Stack User

DevStack should be run as a non-root user with sudo enabled

```sh
sudo useradd -s /bin/bash -d /opt/stack -m stack
echo "stack ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/stack
```

### Download DevStack

```sh
sudo su - stack
git clone https://opendev.org/openstack/devstack
cd devstack
git checkout stable/stein
```

The *devstack* repo contains a script that installs OpenStack and templates for configuration files.


### Create a local.conf

For testing use the [local.conf](local.conf "local.conf") preconfigured file provided.
Copy it to the root devstack folder.

Some changes are required:

* HOST_IP=192.168.1.18 => Should be set according to the local ip of the machine
* FLOATING_RANGE=192.168.1.192/26 => Your public ip range
* FIXED_RANGE=10.10.0.0/16 => Your private ip range
* FIXED_NETWORK_SIZE=256 => Size of your public network range
* FLAT_INTERFACE=ens160 => Should be set according to the interface of the machine
* ADMIN_PASSWORD=xx => Required to connect to the Horizon dashboard


This configuration is setup to:
* Bring up a complete OpenStack Stein version
* Install container module (Swift)
* Install orchestration module (Heat)
* Install load balancer module (Octavia)
* Install telemetry modules (Ceilometer, AODH)

### Start the install

```sh
./stack.sh
```

This will take a 50 - 60 minutes, largely depending on the speed of your internet connection. Many git trees and packages will be installed during this process.

### Post installation

#### Download and install images

Copy the script [images.sh](images.sh "images.sh") in the devstack directory.

```sh
cd devstack
. openrc admin admin
sh images.sh
```

#### Reach openstack instances outside host machine

Devstack alone do not permit to reach openstack instance from outside the openstack host machine, to allow that, add a nat masquerade using iptable.

Be aware :

* <FLAT_INTERFACE> : should be the same as defined in local.conf
* <FLOATING_RANGE MIN> : is the minimum FLOATING_RANGE ip defined in local.conf
* <FLOATING_RANGE MAX> : is the maximum FLOATING_RANGE ip defined in local.conf

```sh
echo 1 > /proc/sys/net/ipv4/ip_forward
echo 1 > /proc/sys/net/ipv4/conf/<FLAT_INTERFACE>/proxy_arp
iptables -t nat -A POSTROUTING -m iprange --src-range <FLOATING_RANGE MIN>-<FLOATING_RANGE MAX> -o <FLAT_INTERFACE> -j MASQUERADE

## Example ##
# iptables -t nat -A POSTROUTING -m iprange --src-range 192.168.1.192-192.168.1.255 -o ens160 -j MASQUERADE
```


## Profit!

You now have a working DevStack! Congrats!

Your devstack will have installed keystone, glance, nova, placement, cinder, neutron, horizon, swift, heat, octavia, and more. Floating IPs will be available, guests have access to the external world.

You can access horizon to experience the web interface to OpenStack, and manage vms, networks, volumes, and images from there.

You can source openrc in your shell, and then use the openstack command line tool to manage your devstack.
