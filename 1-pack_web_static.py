#!/usr/bin/python3
"""
distributes the web server via ssh
"""
from fabric.api import local
import tarfile
import os.path
import re
from datetime import datetime


def do_pack():
    """
    archive distribution
    """
    target = local("mkdir -p versions")
    name = str(datetime.now()).replace(" ", '')
    opt = re.sub(r'[^\w\s]', '', name)
    tar = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(opt))
    if os.path.exists("./versions/web_static_{}.tgz".format(opt)):
        return os.path.normpath("/versions/web_static_{}.tgz".format(opt))
    else:
        return None
