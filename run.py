#!/usr/bin/env python3
import os
import sys
import sqlite3
import argparse
from bottle import route, run, template, static_file, request, post


current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
sys.path.append(current_dir)

cur = sqlite3.connect("students.db").cursor()

@route('/static/<filename:path>')
def server_static(filename):
        return static_file(filename, root=os.path.join(current_dir, "static"))


@route('/')
def index():
    data = cur.executescript("select * from students WHERE f_name = '' OR '1'='1'").fetchall()
    return template('templates/home.tpl', data=data)


@route('/addstudent')
def addstudent():
    column_list = []
    for columns in cur.description:
        column_list.append(columns[0])
    return template('templates/addstudent.tpl', column_list=column_list)


@post('/added')
def added():
    try:
        ext_data = []
        column_data = request.forms
        for key in cur.description:
            ext_data.append(column_data[key[0]])
        cmd = "insert into students values ('%s', '%s', '%s', '%s')" % tuple(ext_data)
        cur.executescript(cmd)
        new_id = cur.lastrowid
        sqlite3.connect("students.db").commit()
        cur.close
    except:
        print "error"
    return index()

run(host='localhost', port=8080, debug=True)
