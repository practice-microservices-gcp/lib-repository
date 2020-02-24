#! /bin/bash

export MYSQL_USER='root'
export MYSQL_PASSWORD='example'
export MYSQL_DATABASE='people'
export MYSQL_RAISE_ON_WARNINGS='True'
export MYSQL_HOST='127.0.0.1'

python test_lib.py