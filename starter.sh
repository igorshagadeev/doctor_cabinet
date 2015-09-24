#!/bin/bash

#
# this script automatically install and run project
#
#

#==================================================#
# Setup the Ubuntu packages
#==================================================#

sudo apt-get install -y python python-setuptools git


#==================================================#
# Pull the code from git
#==================================================#

mkdir -p /home/project/doctor_cabinet
cd /home/project/doctor_cabinet
git clone https://github.com/igorshagadeev/doctor_cabinet.git




#==================================================#
# Setup the python environment
#==================================================#

sudo easy_install virtualenv

virtualenv -p /usr/bin/python3.4 venv

source venv/bin/activate

sudo pip install -r requirements.txt

cd sheduler

python manage.py runserver 0.0.0.0:8000

























