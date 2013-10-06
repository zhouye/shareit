#!/bin/bash
cp shareit/settings.py.template shareit/settings.py
sed -i 's?(__ROOT__)?'`pwd`'?g' shareit/settings.py
./manage.py runserver --insecure
