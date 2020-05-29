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
create_table_query = "CREATE TABLE stats (id int(50) not null auto_increment primary key, \
     ip VARCHAR(20) NOT NULL, hostname VARCHAR(30), vendor VARCHAR(30) NOT NULL, seconds int(50) NOT NULL, lastboot VARCHAR(50) NOT NULL, MAC VARCHAR(20) NOT NULL)"

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
for key, value in im.mydict.items():
    (MAC, vendor), = value[0].items()
    seconds, lastboot = value[1].items()
    hostname = value[2]
    insert = "INSERT INTO stats (ip, hostname, vendor, seconds, lastboot, MAC) \
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(key, hostname[0]['name'], vendor, seconds[1], lastboot[1], MAC)

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
      hostname = row[2]
      vendor = row[3]
      seconds = row[4]
      lastboot = row[5]
      MAC = row[6]
      print ("id = %d, ip = %s, hostname = %s, name = %s, seconds = %d, lastboot = %s, MAC = %s" % \
         (id, ip, hostname, vendor, seconds, lastboot, MAC))
except:
   print ("Error: unable to fetch data")

#zatvaranje konekcije
connection.close()