# Ansible roles

#### Summary

* [Common role](#common-role)
* [Healtcheck role](#healtcheck-role)
* [Load balancer role](#load-balancer-role)
* [WAF role](#waf-role)
* [FW role](#fw-role)
* [VPN role](#vpn-role)
* [Metering role](#metering-role)

## Common role

* Retrieve information about metering instances
* Elastic Load Balancers
  * add or remove ports for each configured domain
  * grant or revoke ports for VPN streams
* Security Groups: 
  * grant or revoke ports for each configured domain
  * configure metering ports
  * configure VPN ports
  * configure healthcheck ports
* Configure specific repositories:
  * centos
  * ELK
  * Grafana
  * Influx
* Install softwares:
  * epel-release
  * vim
  * iptables
  * filebeat
  * haproxy
  * telegraf
* Remove softwares:
  * firewalld
* Configure system
  * change bash behaviour
  * add motd
  * change vimrc behaviour
* Add healthcheck responder
* Generate technical SSL certificates


## Healtcheck role
## Load balancer role

* Create self-signed certificates (per domain, needed to start haproxy)
* Generate technical SSL certificates
* Install and configure softwares:
  * SELinux
  * haproxy (included grant/revoke per domain)
  * rsyslog
* Customization of common softwares


## WAF role

* Create self-signed certificates (per domain, needed to start Nginx)
* Generate technical SSL certificates
* Customization of common softwares
* Configure SELinux
* Install and configure softwares:
  * Nginx and its dependencies
  * Mod Security (WAF module)
  * CLAMAV and its dependencies
  * HAVP (proxy for AV softwares)
  * SURICATA (IDS)
* Configure system
  * add special path onto fstab
  * create specific loopback
* Configure per domain (grant or revoke):
  * Nginx
  * HAVP
  * SURICATA
  * iptables
  * telegraf
  * filebeat


## FW role

* Generate technical SSL certificates
* Customization of common softwares
* Configure SELinux
* Install and configure softwares:
  * Nginx
* Configure sudoers for telegraf
* Configure system
  * enable router mode


## VPN role

* Generate technical SSL certificates
* Customization of common softwares
* Install and configure softwares:
  * OpenVPN
* Grant/Revoke VPN clients


## Metering role

* Generate technical SSL certificates
* Customization of common softwares
* Install and configure softwares:
  * Logstash
  * Grafana
  * Influxdb
* Add/Remove domain meterings
