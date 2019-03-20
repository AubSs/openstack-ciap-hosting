# IT WORK WITH OBJECT STORE


[[local|localrc]]

HOST_IP=192.168.1.45
FLOATING_RANGE=192.168.1.224/27
FIXED_RANGE=10.11.12.0/24
FIXED_NETWORK_SIZE=256
FLAT_INTERFACE=ens192
IP_VERSION=4

ADMIN_PASSWORD=supersecret83
DATABASE_PASSWORD=$ADMIN_PASSWORD
RABBIT_PASSWORD=$ADMIN_PASSWORD
SERVICE_PASSWORD=$ADMIN_PASSWORD

# Enable Logging
LOGFILE=$DEST/logs/stack.sh.log
VERBOSE=True
LOG_COLOR=True

# PLUGINS
OSBRANCH=stable/rocky

# Enable Swift (Object Store) without replication
enable_service s-proxy s-object s-container s-account
SWIFT_HASH=66a3d6b56c1f479c8b4e70ab5c2000f5
SWIFT_REPLICAS=1
SWIFT_DATA_DIR=$DEST/data/swift

## Heat
enable_plugin  heat https://git.openstack.org/openstack/heat $OSBRANCH
enable_plugin  heat-dashboard https://git.openstack.org/openstack/heat-dashboard $OSBRANCH
enable_service h-eng h-api h-api-cfn h-api-cw
