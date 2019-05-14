# Quickly bring up a complete OpenStack

### Requirements

The following minimum requirements should support a proof-of-concept environment with core services and several instances:

* Min 1 processor / 6 cores
* 16 GB memory
* 100 GB storage


### Optional: Set up VM
For testing the CIAP, it's warmly advise using a clean virtual machine.
Using Public Cloud (AWS, Azure, GCP and so on) is not recomended since configuring the network will be difficult.
Another way is to use an host on VMware ESXi.
If this solution is chosen, do not forget to change the NIC teaming.
To do that:
* Go to the VMware vSphere WebClient
* Go to networking
* Edit the settings of your virtual switches
* Extend NIC teaming
* Change Load balancing to "Route based on IP hash"

### Install Linux

Start with a clean and minimal install of a Linux system. DevStack attempts to support the two latest LTS releases of Ubuntu, the latest/current Fedora version, CentOS/RHEL 7, as well as Debian and OpenSUSE.

Currently, Ubuntu 18.04 (Bionic Beaver) is the most tested, and will go the smoothest.

### Add Stack User

DevStack should be run as a non-root user with sudo enabled

```sh
sudo useradd -s /bin/bash -d /opt/stack -m stack
echo "stack ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/stack
sudo su - stack
```

### Download DevStack

```sh
git clone https://opendev.org/openstack/devstack
cd devstack
git checkout stable/stein
```

The *devstack* repo contains a script that installs OpenStack and templates for configuration files.


### Create a local.conf

For testing use the local.conf preconfigured file provided.
Copy it to the root devstack folder.

Some changes are required:
* HOST_IP => Should be set according to the local ip of the machine
* FLAT_INTERFACE => Should be set according to the interface of the machine
* ADMIN_PASSWORD => Required to connect to the Horizon dashboard


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

### Post configuration

Copy the script images.sh in the devstack directory.

```sh
cd devstack
. openrc admin admin
sh images.sh
```

### Profit!

You now have a working DevStack! Congrats!

Your devstack will have installed keystone, glance, nova, placement, cinder, neutron, horizon, swift, heat, octavia, and more. Floating IPs will be available, guests have access to the external world.

You can access horizon to experience the web interface to OpenStack, and manage vms, networks, volumes, and images from there.

You can source openrc in your shell, and then use the openstack command line tool to manage your devstack.
