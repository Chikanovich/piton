import nmap
import settings as s #za NET_ADDR I NMAP_ARGS

#dodjeljivanje scana varijabli
scanner = nmap.PortScanner()

#umjesto staticke IP adrese i argumenata za nmap, iz settings.py se povlace s.NMAP_ADDR i sNMAP_ARGS
scanner.scan(s.NET_ADDR, arguments = s.NMAP_ARGS + " --exclude " + s.EXCLUDE_IPS)
print(scanner.command_line())
print(scanner.scaninfo())
print(scanner.all_hosts())
for host in scanner.all_hosts():
    print("-------------------")
    print("Host:", host, "(", scanner[host].hostname(), ")")
    print("State:", scanner[host].state())
    print("MAC:", scanner[host]['addresses']['mac'])
    try:
        print(scanner[host]['tcp'].keys())
        print(scanner[host].keys())
        print(scanner[host].all_protocols())
    except KeyError:
        print("Host is not TCP based")
    for proto in scanner[host].all_protocols():
        print("-------------------")
        lport = scanner[host][proto].keys()
        for port in lport:
            print('Port:', port, "\tState:", scanner[host][proto][port]['state'])

print("\n")

#dictionary koji se koristi za databazu u pymysqltable.py
mydict = {}

#spremanje scana u dictionary
scanner.scan(s.NET_ADDR, arguments=s.NMAP_ARGS2 + " --exclude " + s.EXCLUDE_IPS)
for h in scanner.all_hosts():
    #print(dir(scanner[h])) - provjera svih varijabli koje se mogu koristiti, koje su privatne, a koje ne
    if 'mac' in scanner[h]['addresses']:
        print("IP & MAC:", scanner[h]['addresses'], "\nState:", scanner[h]['status']['state'], "\nHost names:", 
        scanner[h]['hostnames'], "\nVendor:", scanner[h]['vendor'], "\nUptime:", scanner[h]['uptime'])
        print('------------------------------------------------------')
        scanner[h]['uptime']['seconds'] = int(scanner[h]['uptime']['seconds']) #parsiranje sekundi iz stringa u int za rad s vizualizacijom
        mydict[h] = scanner[h]['vendor'], scanner[h]['uptime'], scanner[h]['hostnames']

"""print('\n')
print(mydict)
print(mydict.keys())
print(mydict.values())"""