import pymysql
import imemreze as im

connection = pymysql.connect("localhost","dinko","Dinko_Pass_1","Netscanner")
cursor = connection.cursor()

delete_existing_table = "DROP TABLE IF EXISTS stats"

create_table_query = """CREATE TABLE stats (id int(50) not null auto_increment primary key, \
     ip VARCHAR(20) NOT NULL, seconds int(50) NOT NULL, lastboot VARCHAR(50) NOT NULL)"""

try:
    cursor.execute(delete_existing_table)
    print("Existing table has been deleted.")
    cursor.execute(create_table_query)
    print("Stats table has been created.")

except Exception as e:
    print("Exception occured: ", e)

"""insert = "INSERT INTO stats (ip, seconds, lastboot) \
   VALUES ('%s', '%d', '%s')" % \
   (ip, seconds, lastboot)"""

for key, value in im.uptime.items():
    insert = "INSERT INTO stats (ip, seconds, lastboot) \
    VALUES ('{}', '{}', '{}')".format(key, value['seconds'], value['lastboot'])
    try:
        cursor.execute(insert)
        connection.commit()
    except:
        connection.rollback()

#try:
#   cursor.execute(insert)
#   connection.commit()
#except:
#   connection.rollback()

#ispis rezultata u terminalu
"""
show = SELECT * FROM stats

try:
   # Execute the SQL command
   cursor.execute(show)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      ip = row[1]
      seconds = row[2]
      lastboot = row[3]
      # Now print fetched result
      print ("id = %d, ip = %s, seconds = %d, lastboot = %s" % \
         (id, ip, seconds, lastboot))
except:
   print ("Error: unable to fetch data")"""

connection.close()