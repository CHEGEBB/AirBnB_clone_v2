#!/usr/bin/python3
"""This Fabric script based on the file 2-do_deploy_web_static.py that creates and
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
it uses the fabric module to run commands on the server
"""

from fabric.api import env, put, run
from datetime import datetime
from os.path import isdir
env.hosts = ['