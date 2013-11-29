#!/bin/bash

yum install python-setuptools python-devel autoconf make gcc gettext

chkconfig mongod on

useradd gecosccmockups --home /opt/gecosccmockups/

easy_install virtualenv
sudo -u gecosccmockups virtualenv /opt/gecosccmockups

lokkit -s http
lokkit -s https
lokkit -p 6543:tcp

echo "Execute python setup.py develop in the gecoscc egg"
echo "You should start the http:"
echo "pserve config-templates/development.ini"
