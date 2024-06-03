#!/usr/bin/python3
"""
A fabric script that generates a tgz archive from the contents of the
web_static folder of your Airbnb Clone repo
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    A function that generates a tgz archive from the contents of
    web_static folder
    """
    try:
        local('mkdir -p versions')
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        archive = f'web_static_{date}.tgz'
        local(f'tar -cvzf versions/{archive} web_static')
    except Exception:
        return None
    else:
        return archive