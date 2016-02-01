__author__ = 'MFlores1'

import psycopg2
import sys


def import_customers_onesite(file_name):
    con = None
    f = None

    try:
        con = psycopg2.connect(database='avalon', user='postgres')
        cur = con.cursor()
        copy_sql = "COPY keywords FROM STDIN WITH CSV HEADER DELIMITER as ','"
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


file_name = "C:/Users/mflores1/dropbox/Mauricio/avln/keywords_result_all_without_nulls.csv"
import_customers_onesite(file_name)