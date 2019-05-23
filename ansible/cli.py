#!/usr/bin/env python3

import argparse
import subprocess
import sys
import os

import openstack


class CLI(object):
    def __init__(self):
        self.openstack = openstack.connection.Connection(
            auth_url=os.environ['OS_AUTH_URL'],
            project_name=os.environ['OS_PROJECT_NAME'],
            user_domain_name=os.environ['OS_USER_DOMAIN_NAME'],
            project_domain_name=os.environ['OS_PROJECT_DOMAIN_NAME'],
            username=os.environ['OS_USERNAME'],
            password=os.environ['OS_PASSWORD']
        )
        self.stack_name = os.environ['STACK_NAME']
        self.servers = []

        servers = self.openstack.compute.servers()
        for server in servers:
            if 'ciap' not in server['metadata'] or server['metadata']['ciap'] != self.stack_name:
                continue
            self.servers.append(server)

    def argparse(self):
        parser = argparse.ArgumentParser(description='CLI API for OCTANE')
    
        group_info = parser.add_argument_group('Info')
        group_info.add_argument('--list-hosts', help='List all available hosts', action='store_true')
        group_info.add_argument('--list-tags',  help='List all available tags',  action='store_true')

        group_execute = parser.add_argument_group('Execute')
        group_execute.add_argument('--tags', nargs='+', type=str, help='Only run tasks tagged with these values')
        group_execute.add_argument('--hosts', nargs='+', type=str, help='Only run hosts roles')
        group_execute.add_argument('--playbook', default='main.yml', help='Specify ansible playbook (Default: main.yml)')

        return parser.parse_args()

    def get_instance_types(self):
        types = set()
        for server in self.servers:
            types.add(server['metadata'].get("instance", None))
        return types

    def check_host(self, host):
        return host in self.get_instance_types()

    def print_instance_types(self):
        types = self.get_instance_types()
        print('List of all available hosts:')
        for item in sorted(types):
            print(f'  - {item}')

    def get_tags(self):
        return set(('init', 'grantdomain', 'revokedomain'))

    def check_tag(self, tag):
        return tag in self.get_tags()

    def print_tags(self):
        tags = self.get_tags()
        print('List of all available tags:')
        for item in sorted(tags):
            print(f'  - {item}')


if __name__ == "__main__":
    cli = CLI()

    args = cli.argparse()
    
    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)

    if args.list_hosts or args.list_tags:
        if args.list_hosts:
            cli.print_instance_types()
        if args.list_hosts or args.list_tags:
            print()
        if args.list_tags:
            cli.print_tags()
        exit(0)

    tags = None
    if args.tags:
        for item in args.tags:
            if not cli.check_tag(item):
                print(f'Tag `{item}` do not exist.')
                cli.print_tags()
                exit(1)
        tags = str.join(',', args.tags)

    hosts = None
    if args.hosts:
        for item in args.hosts:
            if not cli.check_host(item):
                print(f'host `{item}` do not exist.')
                cli.print_instance_types()
                exit(1)
        hosts = str.join(',', args.hosts)

    cmd = ['ansible-playbook', args.playbook]
    if hosts:
        cmd.extend(['-l', hosts])
    if tags:
        cmd.extend(['--tags', tags])
    subprocess.run(cmd)
