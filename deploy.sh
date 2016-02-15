#!/bin/bash

SITE_PATH=/var/www/html/jamie/jamie/

cp app.py ${SITE_PATH}__init__.py
cp -r static $SITE_PATH
cp -r templates $SITE_PATH
