import os
import re
import pymysql
import time
import datetime

def getConnect():
    return pymysql.connect(host="localhost", port=3306,user="thai", passwd="Baotue@123", db="realtate")

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

def queryToDictionary(table, columns, condition):
    # Open database connection
    db = getConnect()
    cursor = db.cursor()
    sql = "select " + columns + " from " + table
    if condition != '':
        sql = sql + " where " + condition
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()

    result = []
    arrCols = columns.split(',')
    for row in data:
        listitem = {}
        icol = 0
        for col in arrCols:
            listitem[col] = row[icol]
            icol=icol+1
        result = result + [listitem]
    return result

def queryCursor(cursor, sql):
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def queryCursorFirst(cursor, sql):
    cursor.execute(sql)
    data = cursor.fetchone()
    return data

def save(obj):
    tableName = type(obj).__name__
    sql = ""
    cols = ""
    values = ""

    for key, prop in obj.__all_properties__:
        if cols == "":
            cols = key
            values = "'" + str(getattr(obj, key)) + "'"
        else:
            cols = cols + "," + key
            values = values + ",'" + str(getattr(obj, key)) + "'"

    sql = "insert into {table}({columns}) values({values})".format(table=tableName,columns=cols,values=values)
    execSql(sql)


def save2(obj):
    tableName = type(obj).__name__
    sql = ""
    cols = ""
    values = ""

    for key in obj.__dict__:
        value = str(obj.__dict__[key])
        if cols == "":
            cols = key
            values = "'" + value + "'"
        else:
            cols = cols + "," + key
            values = values + ",'" + value + "'"

    sql = "insert into {table}({columns}) values({values})".format(table=tableName, columns=cols, values=values)
    execSql(sql)



