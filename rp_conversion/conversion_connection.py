__author__ = 'MFlores1'

import psycopg2
import sys


def import_customers_onesite(file_name):
    con = None
    f = None

    try:
        con = psycopg2.connect(database='conversion', user='postgres')
        cur = con.cursor()
        copy_sql = "COPY onesite_residents FROM STDIN WITH CSV HEADER DELIMITER as ','"
        print copy_sql
        with open(file_name, 'r') as f:
            cur.copy_expert(sql=copy_sql, file=f)
            con.commit()
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
        sys.exit(1)
    except IOError, e:
        print 'Error %s' % e
        sys.exit(1)
    finally:
        if con:
            con.close()
        if f:
            f.close()


def import_prospects_level_one(file_name):
    con = None
    f = None

    try:
        con = psycopg2.connect(database='conversion', user='postgres')
        cur = con.cursor()
        copy_sql = "COPY prospects_level_one FROM STDIN WITH CSV HEADER DELIMITER as ','"
        print copy_sql
        with open(file_name, 'r') as f:
            cur.copy_expert(sql=copy_sql, file=f)
            con.commit()
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
        sys.exit(1)
    except IOError, e:
        print 'Error %s' % e
        sys.exit(1)
    finally:
        if con:
            con.close()
        if f:
            f.close()

# version()
# inserting_data()
# retrieve_data()
# retrieve_data_one_by_one()
file_name = "C:/Users/mflores1/dropbox/Mauricio/matching/forest_city_residents.csv"
import_customers_onesite(file_name)
# file_name = "C:/Users/mflores1/dropbox/Mauricio/matching/l1_guest_cards.csv"
# import_prospects_level_one(file_name)