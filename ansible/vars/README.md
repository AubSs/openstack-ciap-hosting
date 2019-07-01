# Ansible Variables

> Return to [Homepage](../../README.md "Homepage") <br>
  Return to [Ansible Playbook](../README.md "Ansible Playbook")

#### Summary

* [Domain variables](#domain-variables)
* [VPN clients variables](#vpn-clients-variables)
* [Plug variables](#plug-variables)


## Domain variables

The file [domains.yml](domains.yml "domains.yml") is required and must at least include these two empty fields :

```yaml
---

granted_domains:

revoked_domains:
```

You must repeat for each domain you want to grant access to the following lines. Order is not important, but you must start the first item with `-`

**Example of a complete configuration file**
```yaml
granted_domains:
  - backend_ip_or_fqdn: 10.1.0.135
    backend_port: 80
    backend_protocol: http # can be https
    domain: wordpress.ciap.demo
    email: wordpress@ciap.demo
    havp_listening_ip: 127.0.0.1
    havp_listening_port: 20010
    havp_protocol: http
    http: true
    http2_listening_ip: 127.0.0.1
    http2_listening_port: 20011
    http_listening_ip: 0.0.0.0
    http_listening_port: 80
    https_listening_ip: 0.0.0.0
    https_listening_port: 443
    id: 50
    mod_security: 'on' # can be http
    preserve_host: true # can be false
    proxy_timeout: 5

revoked_domains:
  - backend_ip_or_fqdn: 10.1.0.135
    backend_port: 443
    backend_protocol: https # can be https
    domain: wordpress-del.ciap.demo
    email: wordpress@ciap.demo
    havp_listening_ip: 127.0.0.1
    havp_listening_port: 20012
    havp_protocol: http
    http: true
    http2_listening_ip: 127.0.0.1
    http2_listening_port: 20013
    http_listening_ip: 0.0.0.0
    http_listening_port: 80
    https_listening_ip: 0.0.0.0
    https_listening_port: 443
    id: 51
    mod_security: 'on' # can be http
    preserve_host: true # can be false
    proxy_timeout: 5
```
---
```yaml
- backend_ip_or_fqdn: my.backend.none | 192.168.0.1
```

FQDN or IP of the backend.

Example: if you declare two domains myfirst.domain.org and mysecond.domain.org, they may have the same backend common.domain.org.

---
```yaml
backend_port: 1234
```

The listening port of the backend. May be defined also for other domains.

---
```yaml
backend_protocol: http | https
```

If the backend use http (not encrypted stream) or https (encrypted stream).

If you use https, the infrastructure will not check the validity of the backend certificate.

---
```yaml
domain: my.public.domain
```

This is the exposed (public) FQDN of your domain. This must be uniq for each domain.

---
```yaml
email: my_name@my.public.domain
```

Contact mail.

---
```yaml
havp_listening_ip: 127.0.0.1
```

The listening IP for HAVP software. For security reason, you should not change this, since the communication between nginx and havp is not crypted. Therefor, limiting exchange to the loopback is more secure.

Now, using an another IP than one linked to the loopback is not supported.

---
```yaml
havp_listening_port: 12350
```

Uniq HAVP listening port. This must be uniq for each domain. Do not share this port with others ports.

---
```yaml
havp_protocol: http
```

Only http is supported.

---
```yaml
http: false
```

Set if the exposed domain is listening also on http. Otherwise the domain will listen only on https.

---
```yaml
http2_listening_ip: 127.0.0.1
```

Second nginx vhost listening IP (from where the name :-)).

on the midwaf EC2 instance, the stream is:

* (http&|https)_listening_ip:(http&|https)_listening_port: nginx with mod_security -> havp
* havp -> suricata
* http2_listening_ip:http2_listening_port: suricata -> last nginx vhost.

---
```yaml
http2_listening_port: 12360
```

Second nginx vhost listening port (from where the name :-)). Do not share this port with others ports.

on the midwaf instance, the stream is:

* (http&|https)_listening_ip:(http&|https)_listening_port: nginx with mod_security -> havp
* havp -> suricata
* http2_listening_ip:http2_listening_port: suricata -> last nginx vhost.

---
```yaml
http_listening_ip: 0.0.0.0
```

HTTP nginx vhost listening IP. Only support 0.0.0.0.

on the midwaf instance, the stream is:

* (http&|https)_listening_ip:(http&|https)_listening_port: nginx with mod_security -> havp
* havp -> suricata
* http2_listening_ip:http2_listening_port: suricata -> last nginx vhost.

---
```yaml
http_listening_port: 12370
```

HTTP nginx vhost listening port. Do not share this port with others ports.

on the midwaf instance, the stream is:

* (http&|https)_listening_ip:(http&|https)_listening_port: nginx with mod_security -> havp
* havp -> suricata
* http2_listening_ip:http2_listening_port: suricata -> last nginx vhost.

---
```yaml
https_listening_ip: 0.0.0.0
```

HTTPS nginx vhost listening IP. Only support 0.0.0.0.

on the midwaf instance, the stream is:

* (http&|https)_listening_ip:(http&|https)_listening_port: nginx with mod_security -> havp
* havp -> suricata
* http2_listening_ip:http2_listening_port: suricata -> last nginx vhost.

---
```yaml
https_listening_port: 12380
```

HTTPS nginx vhost listening port. Do not share this port with others ports.

on the midwaf instance, the stream is:

* (http&|https)_listening_ip:(http&|https)_listening_port: nginx with mod_security -> havp
* havp -> suricata
* http2_listening_ip:http2_listening_port: suricata -> last nginx vhost.

---
```yaml
id: 1..65535
```

This id must be uniq for each domain.

---
```yaml
mod_security: 'on'
```

Two available settings:

* `on`: mod_security is enabled (default)
* `off`: mod_security is disabled

---
```yaml
preserve_host: true
```

Two available settings:

* `true`: this setting is active (default)
* `false`: this setting is inactive

You may refere to Nginx internet documentation for behaviour of this setting.

---
```yaml
proxy_timeout: 5
```

If you use the IDS as an IPS, this will set the Nginx proxy timeout. Why using this setting ? Suricata is not rejecting the stream in case it identifies a threat, it drops. There is no mecanism for Nginx to know that it's the IDS whom had dropped the connection. Fromwhere this timeout.

## VPN clients variables

The file [vpn.yml](vpn.yml "vpn.yml") is required and must at least include these two empty fields :

```yaml
---

openvpn_grant_clients:

openvpn_revoke_clients:
```

You must repeat for each domain you want to grant/revoke access to the following lines. Order is not important, but you must start the first item with `-`

**Example of a complete configuration file**
```yaml
---

openvpn_grant_clients:
  - name: "riri"
    ip: 7
    email: "riri@mail.com"
    client_network: "10.10.100.77"
    client_netmask: "255.255.255.255"

openvpn_revoke_clients:
  - name: "lulu"
    ip: 5
    email: "lulu@mail.com"
    client_network: "10.10.100.77"
    client_netmask: "255.255.255.255"
```

---
```yaml
- name: "<whatever name you want>"
```

This item must be uniq.

---
```yaml
ip: 1..254
```

This item must be uniq. The interval depends on the `openvpn_server_network` variable.

---
```yaml
email: "<whatever mail you want>"
```

This item must be uniq.

---
```yaml
client_network: "<whatever network you want>"
```

This is used by `OpenVPN` for routing traffic to the client backend network.

---
```yaml
client_netmask: "<whatever netmask you want>"
```

This is used by `OpenVPN` for routing traffic to the client backend network.

## Plug variables

The file [plug.yml](plug.yml "plug.yml") is required if you enable plug instance.

**Example of a complete configuration file**
```yaml
---

wp_db_name: "wordpress"
wp_db_user: "wordpress"
wp_db_password: "wordpress"
```

---
```yaml
wp_db_name: "<whatever name you want>"
```

Required. It's used to initialize the mysql database name.

---
```yaml
wp_db_user: "<whatever user you want>"
```

Required. It's used to initialize the mysql database user.

---
```yaml
wp_db_password: "<whatever password you want>"
```

Required. It's used to initialize the mysql database password.
