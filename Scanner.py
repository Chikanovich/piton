import nmap #importanje python-nmap libraryja

scanner = nmap.PortScanner() #dodjeljivanje varijabli mogućnost rada s nmap scannerom

scanner.scan('192.168.1.1', '21-25') #postavljanje ip adrese i portova koji će se gledati
print(scanner.command_line()) #što treba upisati u obični command line ako se ne radi preko python-nmapa
print(scanner.scaninfo()) #informacije o mreži: tcp/udp, metode, servisi
print(scanner.all_hosts()) #lista svih hostova trenutno na mreži
print(scanner['192.168.1.1'].hostname()) #ime mreže na kojoj je trenutno spojeno
print(scanner['192.168.1.1'].state()) #stanje mreže
print(scanner['192.168.1.1'].all_protocols()) #protokol korišten na mreži (tcp/udp...)
print(scanner['192.168.1.1'].keys()) #hostname, adrese, status...
print(scanner['192.168.1.1'].has_tcp(22)) #postoji li port 22 na tcp-u
print(scanner['192.168.1.1']['tcp'][22]) #opis porta 22 na tcp konekciji zadanog IPa
print(scanner['192.168.1.1'].tcp(22)) #isto kao linija 14
print(scanner['192.168.1.1']['tcp'][22]['state']) #govori je li otvoren port 22 na tcp konekciji zadanog IPa
#Izbacuje error na 127.0.0.1 jer baca prazno polje na scanner['192.168.1.1'].all_protocols(), trebalo bi baciti tcp, a baca []

#Ispisuje imena svih hostova, otvorene portove, vrste protokola i stanja portova
"""for host in scanner.all_hosts():
    print('----------------------------------------------------')
    print('Host :', host, '', scanner[host].hostname())
    print('State :', scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('----------')
        print('Protocol :', proto)
        lport = scanner[host][proto].keys()
        for port in lport:
            print ('port : ', port, '\tstate :', scanner[host][proto][port]['state'])"""
#Izbacuje prazno polje kod all_protocolsa ako ubacim 127.0.0.1 (trebalo bi biti tcp). Ovo valja osim ako ne upišem dobar IP.


"""scanner.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
for host, status in hosts_list:
    print('{0}:{1}'.host)"""
#Instance of 'str' has no 'host' member na liniji 36
#Ovo ne valja


#Asinkrono traženje otvorenih IPova valjda? Ispisuje sve spojene IPove na računalu.
"""nma = nmap.PortScannerAsync()
def callback_result(host, scan_result):
    print('------------------')
    print(host, scan_result)

nma.scan(hosts='192.168.1.0/30', arguments='-sP', callback=callback_result)
while nma.still_scanning():
    print("Waiting >>>")
    nma.wait(2)   # you can do whatever you want but I choose to wait after the end of the scan"""
#Ovo valja!


#Algoritam za ručno unošenje IP adrese i skeniranje istog.
"""print("\n")
print("Welcome, this is a simple nmap automation tool")
print("<--------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input( #ovdje dodati 3 navodnika \nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan\n #ovdje dodati 3 navodnika)
print("You have selected option: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner[ip_addr].hostname())
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    print("Command line: ", scanner.command_line())

elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner[ip_addr].hostname())
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    print("Command line: ", scanner.command_line())

elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner[ip_addr].hostname())
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    print("Command line: ", scanner.command_line())

else:
    print("Please enter a valid number.")"""

