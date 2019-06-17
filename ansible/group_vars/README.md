# Ansible Global variables

This file contains global variables you may (or not) configure.

```yaml
v_certificates_path
```

* Default value: `/etc/ssl`
* Where all the certficates are stored

```yaml
v_clamd_temporary_directory
```

* Default value: `/var/run/clamd.scan`
* This directory is needed by CLAMD software.

```yaml
v_clamd_listening_port
```

* Default value: must be a uniq integer (1024..65535)
* The port where CLAMD is listening

```yaml
v_clamd_listening_address
```

* Default value: `127.0.0.1`
* The address to bind the CLAMD daemon.

```yaml
v_havp_root_directory
```

* Default value: `/opt/havp`
* HAVP root directory

```yaml
v_suricata_root_directory
```

* Default value: `/opt/suricata`
* Suricata root directory

```yaml
v_external_listening_address
```

* Default value: `127.0.0.1`
* Suricata: network source

```yaml
v_suricata_listening_address
```

* Default value: `127.0.0.2`
* The address to bind Suricata daemon


```yaml
v_haproxy_stats_listening_port
```

* Default value: must be a uniq integer (1024..65535)
* Haproxy stats listening port

```yaml
v_haproxy_stats_listening_ip
```

* Default value: `127.0.0.1`
* Exposed IP for HAProxy stats

```yaml
v_haproxy_stats_uri
```

* Default value: `haproxy-stats`
* URI to access the HAProxy stats

```yaml
v_metrology_influxdb_host
```

* Default value: `localhost`
* IP to bind the Influxdb deamon

```yaml
v_metrology_grafana_host
```

* Default value: `localhost`
* IP to bind the grafana daemon

```yaml
v_metrology_grafana_port
```

* Default value: `3000`
* Grafana listening port

```yaml
v_mingtree_port
```

* Default value: `must be a uniq integer (1024..65535)`
* Mingtree access port

```yaml
v_metrology_influxdb_port
```

* Default value: `8086`
* Influxdb listening port

```yaml
v_metrology_tcp_socket_port
```

* Default value: `8094`
* Influxdb TCP listening port

```yaml
v_metrology_influxdb_db
```

* Default value: `octane`
* Name of the database where to store all your measurments

```yaml
v_metrology_influxdb_user
```

* Default value: `octane`
* Metrology user name (restricted rights)

```yaml
v_metrology_influxdb_password
```

* Default value: `octane`
* Metrology user password (restricted rights)

```yaml
v_metrology_logstash_port
```

* Default value: `5044`
* Default logstash listening port

```yaml
v_grafana_admin
```

* Default value: `admin`
* Grafana admin name

```yaml
v_grafana_admin_password
```

* Default value: `admin`
* Grafana admin password

```yaml
v_influxdb_admin
```

* Default value: `admin`
* Influxdb master admin name

```yaml
v_influxdb_admin_password
```

* Default value: `admin`
* Influxdb master admin password

```yaml
v_influxdb_logstash_writer
```

* Default value: `logstash_writer`
* Influxdb logstash name (Write only)

```yaml
v_influxdb_logstash_writer_password
```

* Default value: `logstash_writer_password`
* Influxdb logstah password

```yaml
v_influxdb_grafana_reader
```

* Default value: `grafana_reader`
* Influxdb grafana name (Read only)

```yaml
v_influxdb_grafana_reader_password
```

* Default value: `grafana_reader_password`
* Influxdb grafana password

```yaml
v_vpn_port
```

* Default value: `must be a uniq integer (1024..65535)`
* VPN port on VPN zone

```yaml
v_log_path
```

* Default value: `/var/log`
* Path log
