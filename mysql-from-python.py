import os
import pymysql

#Get username from Cloud9 workspace
username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='Chinook')

try:
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred']
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    connection.close()