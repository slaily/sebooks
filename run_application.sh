#!/bin/bash
uwsgi --http 127.0.0.1:5000 --wsgi-file sebooks.py --callable app_dispatcher
