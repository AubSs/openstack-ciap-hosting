[[local|localrc]]

HOST_IP=192.168.1.43
SERVICE_HOST=$HOST_IP
MYSQL_HOST=$HOST_IP
RABBIT_HOST=$HOST_IP
GLANCE_HOSTPORT=$HOST_IP:9292
ADMIN_PASSWORD=secret
DATABASE_PASSWORD=$ADMIN_PASSWORD
RABBIT_PASSWORD=$ADMIN_PASSWORD
SERVICE_PASSWORD=$ADMIN_PASSWORD

## Neutron options
Q_USE_SECGROUP=True
FLOATING_RANGE="192.168.1.0/24"
IPV4_ADDRS_SAFE_TO_USE="10.0.0.0/22"
Q_FLOATING_ALLOCATION_POOL=start=192.168.1.150,end=192.168.1.254
PUBLIC_NETWORK_GATEWAY="192.168.1.1"
PUBLIC_INTERFACE=ens192
IP_VERSION=4

# Linuxbridge Settings
Q_USE_PROVIDERNET_FOR_PUBLIC=True
Q_AGENT=linuxbridge
LB_PHYSICAL_INTERFACE=$PUBLIC_INTERFACE
PUBLIC_PHYSICAL_NETWORK=default
LB_INTERFACE_MAPPINGS=$PUBLIC_PHYSICAL_NETWORK:$PUBLIC_INTERFACE
