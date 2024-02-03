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

    if not os.path.exists(archive_path):
        return False

    try:
        """Upload the archive to /tmp/ directory on the web server"""
        put(archive_path, '/tmp/')

        """Extract the archive to /data/web_static/releases/<archive filename without extension>"""
        archive_filename = os.path.basename(archive_path)
        release_folder = '/data/web_static/releases/{}'.format(
            archive_filename[:-4] if archive_filename.endswith('.tgz') else archive_filename
        )
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        """Delete the archive from the web server"""
        run('rm /tmp/{}'.format(archive_filename))

        """Delete the symbolic link /data/web_static/current"""
        current_link = '/data/web_static/current'
        run('rm -rf {}'.format(current_link))

        """Create a new symbolic link /data/web_static/current linked to the new version"""
        run('ln -s {} {}'.format(release_folder, current_link))

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
