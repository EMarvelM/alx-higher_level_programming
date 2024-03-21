#!/usr/bin/python3
import MySQLdb
from sys import argv

db = MySQLdb.Connect( host="localhost", user=argv[1], password=argv[2], database=argv[3] )
