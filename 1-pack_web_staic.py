#!/usr/bin/env python3
"""a fabric script that generates a .tgz archive from the contents of the web_static folder
"""

from fabric .api import *
from datetime import datetime
import os.path

def do_pack():

    local('sudo mkdir -p versions')

    t = datetime.now()
    t_str = t.strftime('%Y%m%d%H%M%S')

   # local(f'tar -cvzf versions/web_static_{t_{str}.tgz web_static')
    local('tar -cvzf versions/web_static_{}.tgz web_static'.format(t_str))

    f_path = f"versions/web_static_{t_str}.tgz"
    f_size = os.path.getsize(f_path)
    print(f"web_static packed: versions/web_static_{t_str}.tgz -> {f_size}Bytes")
