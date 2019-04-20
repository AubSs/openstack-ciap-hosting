# CIAP Openstack

## Conf

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
stack_name = aubin
stack_template = heat/main.yaml
public_key_file = /home/aubin/.ssh/id_rsa.pub

[Orchestration]
server_image = 205a30b1-0347-4412-a32e-63216a912d38
```

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
