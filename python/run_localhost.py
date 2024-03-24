#!/usr/bin/env python3

import os
from sys import path

this_file_path = os.path.abspath(__file__)
this_dir = os.path.dirname(this_file_path)
path.append(this_dir)

from app import app as application


if __name__ == "__main__":
    application.run()

# run as:
# uwsgi --http-socket :9000 --plugin python3 --wsgi-file python/run_localhost.py --enable-threads --master
# access the gui in browser at address: localhost:9000