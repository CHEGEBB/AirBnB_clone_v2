#!/usr/bin/python3
"""This module generates a .tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
It uses the fabric module to run commands on the server
"""

from os.path import isdir
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder
    of the AirBnB Clone repo
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
