#!/usr/bin/python3
"""
distrubting the web server
"""
from fabric.api import *
import os.path

env.user = 'ubuntu'
env.hosts = ["34.224.2.4", "54.144.239.50"]
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """
    archive distribution
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        arc = archive_path.split("/")
        base = arc[1].strip('.tgz')
        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/{}'.format(base))
        main = "/data/web_static/releases/{}".format(base)
        sudo('tar -xzf /tmp/{} -C {}/'.format(arc[1], main))
        sudo('rm /tmp/{}'.format(arc[1]))
        sudo('mv {}/web_static/* {}/'.format(main, main))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(main))
        return True
    except:
        return False
