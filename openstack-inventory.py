#!/usr/bin/env python3

import argparse
import json

import openstack


class Inventory(object):
    def __init__(self, conf_path, public):
        self.openstack = openstack.connection.Connection(
            auth_url='http://192.168.1.45/identity',
            project_name='admin',
            user_domain_name='default',
            project_domain_name='default',
            username='admin',
            password='xxx'
        )
        self.data = {'_meta': {'hostvars': {}}}

        generator = self.openstack.compute.servers()
        for server in generator:
            group = self.data.setdefault(server['name'], [])
            group.append(server['id'])
            server_obj = self.data['_meta']['hostvars'].setdefault(server['id'], {'openstack': server})
            server_obj['ansible_host'] = self.get_ip_from_server(server, public=True)
            server_obj['ansible_user'] = 'centos'

    def get_ip_from_server(self, server, public=False, ip_version=4):
        ip_type = 'floating' if public else 'fixed'
        for address in server['addresses']:
            for ip in server['addresses'][address]:
                if ip['version'] == ip_version and ip['OS-EXT-IPS:type'] == ip_type:
                    return ip['addr']
        return 'null'

    def get_host_info(self, id):
        info = self.data['_meta']['hostvars'].get(id, 'null')
        print(json.dumps(info, indent=4))

    def list(self):
        for server in self.data['_meta']['hostvars']:
            del(self.data['_meta']['hostvars'][server]['openstack'])
        print(json.dumps(self.data, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build an Ansible inventory based on group.')
    parser.add_argument('--public', action='store_true', help='Use public address for ansible host')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', help='List active servers', action='store_true')
    group.add_argument('--host', help='List details about the specific host')
    args = parser.parse_args()

    inventory = Inventory('lol', args.public)
    if args.list:
        inventory.list()
    elif args.host:
        inventory.get_host_info(args.host)
    else:
        parser.print_help()
