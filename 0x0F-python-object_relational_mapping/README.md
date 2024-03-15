#  0x0F-python-object_relational_mapping

## Background Context

In this project, I will link two amazing worlds: Databases and Python!

In the first part, I will use the module MySQLdb to connect to a MySQL database and execute my SQL queries.

In the second part, I will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

## SETTING UP
### Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:


* `$ sudo apt-get install python3.8-venv`
* `$ python3 -m venv venv`
* `$ source venv/bin/activate`

### Install MySQLdb module
For installing `MySQLdb`, you need to have `MySQL` installed:
- [CLICK HERE](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04) to learn how to install `MySQL 8.0` in `Ubuntu 20.04`.

* `$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config` # Debian / Ubuntu

* `% sudo yum install python3-devel mysql-devel pkgconfig` # Red Hat / CentOS

Then install mysqlclient via pip:
```
$ pip install mysqlclient
```
```
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

### Install SQLAlchemy module
* `$ pip install SQLAlchemy`
```
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

## The biggest difficulty with ORM is: The syntax!
