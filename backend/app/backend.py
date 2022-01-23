#!/usr/bin/python3
# -*- coding: utf-8 -*-

#111import re

# import the psycopg2 database adapter for PostgreSQL
from psycopg2 import connect, Error

# import Python's built-in JSON library
import json
import requests
# import the JSON library from psycopg2.extras
from psycopg2.extras import Json

# import psycopg2's 'json' using an alias
from psycopg2.extras import json as psycop_json

# import Python's 'sys' library
import sys

conn=connect("dbname='postgres' user='postgres' password='Password1' host='192.168.0.105' port='5432' ")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Pink_Floyd")
#DROP TABLE IF EXIST w5
#cur.execute("CREATE TABLE IF NOT EXISTS Pink_Floyd (id BIGSERIAL, kind VARCHAR, wrapperеype VARCHAR, artistid VARCHAR, trackprice VARCHAR, trackviewurl VARCHAR)")
#cur.execute("CREATE TABLE IF NOT EXISTS Pink_Floyd (id BIGSERIAL, kind VARCHAR(50), collectionName VARCHAR(50), trackName VARCHAR(50), collectionPrice VARCHAR(50), trackPrice VARCHAR(50), primaryGenreName VARCHAR(50), trackCount VARCHAR(50), trackNumber VARCHAR(50), releaseDate DATE)")
cur.execute("CREATE TABLE IF NOT EXISTS Pink_Floyd (id BIGSERIAL, wrappertype VARCHAR, kind VARCHAR, artistid VARCHAR, collectionid VARCHAR, trackid VARCHAR, artistname VARCHAR, collectionname VARCHAR, trackname VARCHAR, collectioncensoredname VARCHAR, trackviewurl VARCHAR, previewurl VARCHAR, artworkurl30 VARCHAR, artworkurl60 VARCHAR,trackcensoredname VARCHAR, artistviewurl VARCHAR, collectionviewurl VARCHAR, artworkurl100 VARCHAR, collectionprice VARCHAR, trackprice VARCHAR, releasedate DATE, collectionexplicitness VARCHAR, trackexplicitness VARCHAR, disccount VARCHAR, discnumber VARCHAR, trackcount VARCHAR, tracknumber VARCHAR, tracktimemillis VARCHAR, country VARCHAR, currency VARCHAR, primarygenrename VARCHAR, isstreamable VARCHAR)")

conn.commit()
#conn.close()
print ("\ncreated cursor object:", cur)


# accept command line arguments for the Postgres table name
if len(sys.argv) > 1:
    table_name = '_'.join(sys.argv[1:])
else:
    # ..otherwise revert to a default table name
    table_name = "Pink_Floyd"


#url=("https://itunes.apple.com/search?term=Pink+Floyd&limit=54")
url=("https://itunes.apple.com/search?term=Pink+Floyd")
basetask=requests.get(url)
#команда ниже сохраняет файл который мы скачиваем по url ссылке и сохраняет его как data.json
with open('data4.json', 'w') as f:
     f.write(basetask.text)

n = 6
with open('data4.json', 'r') as inp:
    l = inp.readlines()
with open('data3.json', 'w') as out:
    out.writelines(l[n:])

with open('data3.json', 'r') as f:
    lines = f.readlines()
    lines = lines[:-3]
with open('data2.json', 'w') as f:
    f.writelines(lines)


with open('data2.json', 'r') as f:
    data = f.read()
with open('data.json', 'w') as f:
    f.writelines('[')
    f.write(data)


# use Python's open() function to load the JSON data
with open('data.json') as json_data:


# use load() rather than loads() for JSON files
     record_list = json.load(json_data)

print ("\nrecords:", record_list)
print ("\nJSON records object type:", type(record_list)) # should return "<class 'list'>"


# concatenate an SQL string
sql_string = 'INSERT INTO {} '.format( table_name )

# if record list then get column names from first key
if type(record_list) == list:
    first_record = record_list[0]

    columns = list(first_record.keys())
    print ("\ncolumn names:", columns)

# if just one dict obj or nested JSON dict
else:
    print ("Needs to be an array of JSON objects")
    sys.exit()

# enclose the column names within parenthesis
sql_string += "(" + ', '.join(columns) + ")\nVALUES "

# enumerate over the record
for i, record_dict in enumerate(record_list):
    # iterate over the values of each record dict object
    values = []
    for col_names, val in record_dict.items():

        # Postgres strings must be enclosed with single quotes
        if type(val) == str:
            # escape apostrophies with two single quotations
            val = val.replace("'", "''")
            val = "'" + val + "'"

        values += [ str(val) ]

    # join the list of values and enclose record in parenthesis
    sql_string += "(" + ', '.join(values) + "),\n"

# remove the last comma and end statement with a semicolon
sql_string = sql_string[:-2] + ";"

print ("\nSQL string:")
print (sql_string)
# only attempt to execute SQL if cursor is valid
if cur != None:

    try:
        cur.execute( sql_string )
        conn.commit()

        print ('\nfinished INSERT INTO execution')

    except (Exception, Error) as error:
        print ("\nexecute_sql() error:", error)
        conn.rollback()

    # close the cursor and connection
    cur.close()
    conn.close()

