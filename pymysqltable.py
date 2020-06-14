import sys
sys.path.append('/home/dinko/.local/lib/python3.6/site-packages')
import pymysql
import imemreze as im

#spajanje na server i bazu
connection = pymysql.connect("localhost","dinko","Dinko_Pass_1","Netscanner")
cursor = connection.cursor()

#query za brisanje postojece tablice
delete_existing_table = "DROP TABLE IF EXISTS stats"

#query za stvaranje nove tablice
"""create_table_query = "CREATE TABLE stats (id int(50) not null auto_increment primary key, \
     ip VARCHAR(20) NOT NULL, hostname VARCHAR(30), vendor VARCHAR(30) NOT NULL, seconds int(50) NOT NULL, lastboot VARCHAR(50) NOT NULL, MAC VARCHAR(20) NOT NULL)"""

create_table_query = "CREATE TABLE stats (id int(50) not null auto_increment primary key, \
     vendor VARCHAR(30) NOT NULL, ip VARCHAR(20) NOT NULL, MAC VARCHAR(20) NOT NULL, hostname VARCHAR(30), time VARCHAR(30) NOT NULL)"

#brisanje stare tablice i stvaranje nove tablice
try:
    cursor.execute(delete_existing_table)
    print("Existing table has been deleted.")
    cursor.execute(create_table_query)
    print("New 'stats' table has been created.")
except:
    connection.rollback()
    print("Exception occured. Could not create table.")

#unos vrijednosti u tablicu
"""for key, value in im.mydict.items():
    (MAC, vendor), = value[0].items()
    seconds, lastboot = value[1].items()
    hostname = value[2]
    insert = "INSERT INTO stats (vendor, ip, MAC, hostname, time) \
    VALUES ('{}', '{}', '{}', '{}', '{}')".format(key, hostname[0]['name'], vendor, seconds[1], lastboot[1], MAC)"""

for key, value in im.mydict.items():
    (MAC, vendor), = value[0].items()
    ip = value[1]
    hostname = value[2]
    time = value[3]
    insert = "INSERT INTO stats (vendor, ip, MAC, hostname, time) \
    VALUES ('{}', '{}', '{}', '{}', '{}')".format(vendor, ip['ipv4'], MAC, hostname[0]['name'], time)

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
      vendor = row[1]
      ip = row[2]
      MAC = row[3]
      hostname = row[4]
      time = row[5]
      print ("id = %d, vendor = %s, ip = %s, MAC = %s, hostname = %s, time = %s" % \
         (id, vendor, ip, MAC, hostname, time))
except:
   print ("Error: unable to fetch data")

#zatvaranje konekcije
connection.close()