#!/usr/bin/env bash

# Fedora 30
IMG_Fedora=Fedora-Cloud-Base-30-1.2.x86_64.qcow2
wget http://mirror.in2p3.fr/pub/fedora/linux/releases/30/Cloud/x86_64/images/${IMG_Fedora}
openstack image create --public --disk-format qcow2 --container-format bare --file ${IMG_Fedora} \
                       --property murano_image_info='{"title": "Fedora 30", "type": "fedora"}' 'Fedora 30'
rm ${IMG_Fedora}

# CentOS 7
IMG_CentOS=CentOS-7-x86_64-GenericCloud-1901.qcow2
wget https://cloud.centos.org/centos/7/images/${IMG_CentOS}
openstack image create --public --disk-format qcow2 --container-format bare --file ${IMG_CentOS} \
                       --property murano_image_info='{"title": "CentOS 7 1901", "type": "centos"}' 'CentOS 7 1901'
rm ${IMG_CentOS}

# Debian 9
IMG_Debian=debian-9.9.0-openstack-amd64.qcow2
wget https://cdimage.debian.org/cdimage/openstack/9.9.0/${IMG_Debian}
openstack image create --public --disk-format qcow2 --container-format bare --file ${IMG_Debian} \
                       --property murano_image_info='{"title": "Debian 9.9.0", "type": "debian"}' 'Debian 9.9.0'
rm ${IMG_Debian}

# Ubuntu Xenial 16.04 LTS
IMG_Xenial=xenial-server-cloudimg-amd64-disk1.img
wget http://cloud-images.ubuntu.com/xenial/current/${IMG_Xenial}
openstack image create --public --disk-format qcow2 --container-format bare --file ${IMG_Xenial} \
                       --property murano_image_info='{"title": "Ubuntu Xenial 16.04 LTS", "type": "ubuntu"}' 'Ubuntu Xenial 16.04 LTS'
rm ${IMG_Xenial}

# Ubuntu Bionic 18.04 LTS
IMG_Bionic=bionic-server-cloudimg-amd64.img
wget http://cloud-images.ubuntu.com/bionic/current/${IMG_Bionic}
openstack image create --public --disk-format qcow2 --container-format bare --file ${IMG_Bionic} \
                       --property murano_image_info='{"title": "Ubuntu Bionic 18.04 LTS", "type": "ubuntu"}' 'Ubuntu Bionic 18.04 LTS'
rm ${IMG_Bionic}
