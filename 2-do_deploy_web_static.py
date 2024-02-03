#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers"""
import os
from fabric.api import env, put, run, local
from datetime import datetime


env.user = 'ubuntu'
env.hosts = ['54.243.56.63', '54.209.3.212']

def do_pack():
    """Module to get the archive path if archive is generated correctly"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_field_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archive_field_path))

    if t_gzip_archive.succeeded:
        return archive_field_path
    else:
        return None


def do_deploy(archive_path):
    """Deploys the archive to web servers"""

    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newer_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newer_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newer_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newer_version,
                                                newer_version))
        run("sudo rm -rf {}/web_static".format(newer_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newer_version))

        print("New version deployed!")
        return True

    return False
