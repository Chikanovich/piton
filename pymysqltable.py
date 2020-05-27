import pymysql
import imemreze as im

connection = pymysql.connect("localhost","dinko","Dinko_Pass_1","Netscanner")
cursor = connection.cursor()

delete_existing_table = "DROP TABLE IF EXISTS stats"

create_table_query = """CREATE TABLE stats (id int(50) not null auto_increment primary key, \
     ip VARCHAR(20) NOT NULL, name VARCHAR(30) NOT NULL, seconds int(50) NOT NULL, lastboot VARCHAR(50) NOT NULL, MAC VARCHAR(20) NOT NULL)"""

try:
    cursor.execute(delete_existing_table)
    print("Existing table has been deleted.")
    cursor.execute(create_table_query)
    print("New stats table has been created.")

except:
    connection.rollback()
    print("Exception occured. Could not create table.")

for key, value in im.mydict.items():
    (mac, name), = value[0].items()
    seconds, lastboot = value[1].items()
    insert = "INSERT INTO stats (ip, name, seconds, lastboot, MAC) \
    VALUES ('{}', '{}', '{}', '{}', '{}')".format(key, name, seconds[1], lastboot[1], mac)
    try:
        cursor.execute(insert)
        connection.commit()
    except:
        connection.rollback()
        print("Exception occured. Could not insert data.")


print("\n")

#ispis tablice u terminalu
show = "SELECT * FROM stats"
try:
   cursor.execute(show)
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      ip = row[1]
      name = row[2]
      seconds = row[3]
      lastboot = row[4]
      MAC = row[5]
      print ("id = %d, ip = %s, name = %s, seconds = %d, lastboot = %s, MAC = %s" % \
         (id, ip, name, seconds, lastboot, MAC))
except:
   print ("Error: unable to fetch data")


connection.close()