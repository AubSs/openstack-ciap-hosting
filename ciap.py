#!/usr/bin/env python3

import argparse
import configparser
import io
import tarfile

import openstack
from openstack.orchestration.util import template_utils


class CIAP(object):
    def __init__(self, name: str, conf: dict):
        self.name = name
        self.conf = conf
        self.openstack = openstack.connection.Connection(**conf['Openstack'])

    def get_openstack_rc(self):
        conf = self.conf['Openstack']
        rc = '# .openstackrc\n'
        rc += 'export OS_AUTH_URL={}\n'.format(conf['auth_url'])
        rc += 'export OS_PROJECT_ID={}\n'.format(conf['project_id'])
        rc += 'export OS_PROJECT_NAME={}\n'.format(conf['project_name'])
        rc += 'export OS_USER_DOMAIN_NAME={}\n'.format(conf['user_domain_name'])
        rc += 'export OS_PROJECT_DOMAIN_NAME={}\n'.format(conf['project_domain_name'])
        rc += 'export OS_USERNAME={}\n'.format(conf['username'])
        rc += 'export OS_PASSWORD={}\n'.format(conf['password'])
        rc += 'export OS_REGION_NAME={}\n'.format(conf['region_name'])
        rc += 'export OS_INTERFACE={}\n'.format(conf['interface'])
        rc += 'export OS_IDENTITY_API_VERSION={}\n'.format(conf['identity_api_version'])
        rc += 'export STACK_NAME={}\n'.format(self.name)
        return rc

    def New(self):
        print(f'Create {self.name} stack')
        container = self._create_container(self.name, "ansible")
        self.conf['Orchestration']['container_name'] = container['container']
        self.conf['Orchestration']['ansible_tarball'] = container['name']

        with open(self.conf['CIAP']['public_key_file'], 'r') as file:
            self.conf['Orchestration']['ssh_public_key'] = file.read()

        files, template = template_utils.get_template_contents(self.conf['CIAP']['stack_template'])

        self.conf['Orchestration']['openstack_rc'] = self.get_openstack_rc()
        self.openstack.orchestration.create_stack(
            name=self.name,
            template=template,
            files=files,
            parameters=dict(self.conf['Orchestration'])
        )

    def Delete(self):
        print(f'Delete {self.name} stack')
        self._delete_container(self.name)
        self.openstack.orchestration.delete_stack(self.name)

    def List(self):
        print("list ciap")

    def _create_container(self, name: str, *files):
        # Compress all files
        compress_algo = 'bz2'
        buffer = io.BytesIO()
        tar = tarfile.open(mode=f'w:{compress_algo}', fileobj=buffer)
        for file in files:
            tar.add(file)
        tar.close()

        # Push compressed files in a newly created object store
        container = self.openstack.object_store.create_container(name)
        return self.openstack.object_store.upload_object(
            container=container,
            name=f'ciap.tar.{compress_algo}',
            data=buffer.getvalue()
        )

    def _delete_container(self, name: str):
        objects = self.openstack.object_store.objects(name)
        for object in objects:
            self.openstack.object_store.delete_object(object.name, container=name)
        self.openstack.object_store.delete_container(name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help="Specifie config file (default ./ciap.ini)", default="ciap.ini")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--new",    metavar='<user>', help="Create a new CIAP")
    group.add_argument("--delete", metavar='<user>', help="Delete a CIAP")
    group.add_argument("--list",   help="List all CIAP", action="store_true")
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.c)

    stack_name = args.new or args.delete or ""
    ciap = CIAP(
        name=stack_name,
        conf=config
    )
    if args.new:
        ciap.New()
    elif args.delete:
        ciap.Delete()
    elif args.list:
        ciap.List()
    else:
        parser.print_help()
