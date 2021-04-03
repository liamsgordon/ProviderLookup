# ProviderLookup

"""

This is a Django web application which allows people to easily search for porviders based on name, location and practice. 
This web application is based on the the NPPES NPI search database here:

https://npiregistry.cms.hhs.gov/

My applicatio aims to be more user friendly, for someone who does not know what an NPI or a taxonomy code is.

"""


"""

Requirements:

python 3.7+
Postgresql 13.2
django 3.1.7

steps:

1) download folder

2) insert data into postgresql
 
 i) download 'Full Replacement Monthly NPI File' in https://download.cms.gov/nppes/NPI_Files.html
 ii) place file in data folder
 iii) open postgresql, create database call lookup, download any requirments for postgreql python connection
 iv) run Cross_sectional_data.py, and follow terminal instructions.
  **** this will take time ****

3) create virtual env
code in terminal:
  apt-get install python-venv 
  python -m venv env 
  source env/bin/activate  
  cd src
  pip install Django
  python manage.py runserver
  


"""
