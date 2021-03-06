__author__ = 'MFlores1'

import psycopg2
import sys


def version():
    con = None

    try:
        con = psycopg2.connect(database='conversion', user='postgres')
        cur = con.cursor()
        cur.execute('SELECT version()')
        ver = cur.fetchone()
        print ver

    except psycopg2.DatabaseError, e:
        print "Error %s" % e
        sys.exit(1)
    finally:
        if con:
            con.close()


def inserting_data():
    con = None

    cars = (
        (1, 'Audi', 52642),
        (2, 'Mercedes', 57127),
        (3, 'Skoda', 9000),
        (4, 'Volvo', 29000),
        (5, 'Bentley', 350000),
        (6, 'Citroen', 21000),
        (7, 'Hummer', 41400),
        (8, 'Volkswagen', 21600))

    try:
        con = psycopg2.connect(database='conversion', user='postgres')
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Cars")
        cur.execute("CREATE TABLE Cars(Id INT PRIMARY KEY, Name TEXT, Price INT)")
        query = "INSERT INTO Cars (Id, Name, Price) VALUES (%s, %s, %s)"
        cur.executemany(query, cars)
        con.commit()
    except psycopg2.DatabaseError, e:
        if con:
            con.rollback()
        print 'Error %s' % e
        sys.exit(1)
    finally:
        if con:
            con.close()


def retrieve_data():
    con = None

    try:
        con = psycopg2.connect(database='matching', user='postgres')
        cur = con.cursor()
        cur.execute("SELECT * FROM Cars")
        rows = cur.fetchall()
        for row in rows:
            print row
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
        sys.exit(1)
    finally:
        if con:
            con.close()


def retrieve_data_one_by_one():
    con = None

    try:
        con = psycopg2.connect(database='conversion', user='postgres')
        cur = con.cursor()
        cur.execute("SELECT * FROM Cars")
        while True:
            row = cur.fetchone()
            if None:
                break
            print row[0], row[1], row[2]
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
        sys.exit(1)
    finally:
        if con:
            con.close()


