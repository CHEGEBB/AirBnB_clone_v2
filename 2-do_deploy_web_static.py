#!/usr/bin/python3

"""This Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
it uses the fabric module to run commands on the server
"""
from os.path import isfile
from fabric.api import env, put, run
env.hosts = ['34.202.234.181', '54.173.84.105']


def do_deploy(archive_path):
    """This function distributes an archive to the web servers
    it uses the fabric module to run commands on the server
    The function returns False if the file at the path archive_path doesn't exist
    """
    if isfile(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
