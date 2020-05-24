import nmap
import pymysql

#MAP SCANNING CODE
nmScan=nmap.PortScanner()
host=self._firstname.value     # taking input from a pyforms gui input field
result=nmScan.scan(hosts=host, arguments='-sV -v -p 1-1024')
print('Host : %s (%s)' % (host, nmScan[host].hostname()))
print('State : %s' % nmScan[host].state())
for proto in nmScan[host].all_protocols():
    print('----------')
    print('Protocol : %s' % proto)
    lport = nmScan[host][proto].keys()
    #lport.sort()
    for port in lport:
        thisDict = nmScan[host][proto][port]
        print ('port : %s\tstate : %s\tVersion:%s,v%s'% (port, nmScan[host][proto][port]['state'],thisDict['product'] ,thisDict['version']))


 #INSERT into INPUT table CODE
    try:
        connection = mysql.connector.connect(host='localhost',
                                database='testdb',
                                 user='root',
                                 password='Pooja@123')
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO input (sno,ip) VALUES (%s,%s)"""
        so=cursor.lastrowid
        sno=so
        ip=self._firstname.value     # taking input from a pyforms gui input field
        insert_tuple = (sno,ip)
        result = cursor.execute(sql_insert_query, insert_tuple)
        print("inserted")
        connection.commit()
    except mysql.connector.Error as error :
        connection.rollback() #rollback if any exception occured
        print("Failed inserting record into input table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")