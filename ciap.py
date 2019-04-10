#!/usr/bin/env python3

import argparse
import configparser
import io
import json
import os
import tarfile
import yaml

import openstack


class CIAP(object):
    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.openstack = openstack.connection.Connection(**conf['Openstack'])

    def New(self):
        print(f'Create {self.name} stack')
        self._create_container(self.name, "ansible")
        with open(self.conf['CIAP']['stack_template'], "r") as file:
            heat_template = yaml.safe_load(file)
        self.openstack.orchestration.create_stack(
            name=self.name,
            template=heat_template,
            parameters=dict(self.conf['Orchestration'])
        )

    def Delete(self):
        print(f'Delete {self.name} stack')
        self._delete_container(self.name)
        self.openstack.orchestration.delete_stack(self.name)

    def List(self):
        print("list ciap")

    def _create_container(self, name, *files):
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

    def _delete_container(self, name):
        objects = self.openstack.object_store.objects(name)
        for object in objects:
            self.openstack.object_store.delete_object(object.name, container=name)
        self.openstack.object_store.delete_container(name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help="Specifie config file (default ./ciap.ini)", default="ciap.ini")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--new",    help="Create a new CIAP")
    group.add_argument("--delete", help="Delete a CIAP")
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
