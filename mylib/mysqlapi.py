import os
import re
import MySQLdb
import time
import datetime

def getConnect():
    return MySQLdb.connect("localhost", "thai", "Baotue@123", "realtate")

def execSql(sql):
    # Open database connection
    db = getConnect()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()

def query(sql):
    # Open database connection
    db = getConnect()
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data

def queryCursor(cursor, sql):
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def queryCursorFirst(cursor, sql):
    cursor.execute(sql)
    data = cursor.fetchone()
    return data


