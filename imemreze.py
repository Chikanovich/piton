import nmap
import time
import datetime
import settings as s #za NET_ADDR I NMAP_ARGS

scanner = nmap.PortScanner()

#umjesto statičke IP adrese sam dodao s.NET_ADDR i umjesto argumenta sam dodao s.NMAP_ARGS koji se povlače iz settings.py filea
scanner.scan(s.NET_ADDR, arguments = s.NMAP_ARGS + " --exclude " + s.EXCLUDE_IPS)
print(scanner.command_line())
print(scanner.scaninfo())
print(scanner.all_hosts())
for host in scanner.all_hosts():
    print('-------------------')
    print('Host:', host, "(", scanner[host].hostname(), ")")
    print('State:', scanner[host].state())
    print('MAC:', scanner[host]['addresses']['mac'])
    try:
        print(scanner[host]['tcp'].keys())
        print(scanner[host].keys())
        print(scanner[host].all_protocols())
    except KeyError:
        print('Host is not TCP based')
    for proto in scanner[host].all_protocols():
        print('-------------------')
        lport = scanner[host][proto].keys()
        for port in lport:
            print('port:', port, "\tstate:", scanner[host][proto][port]['state'])

print('\n')
#IP i state, dupli posao je bio pa sam zakomentirao
"""scanner.scan(s.NET_ADDR, arguments=s.NMAP_ARGS + " --exclude " + s.EXCLUDE_IPS)
hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
print(hosts_list)
print('\n')"""

mydict = {}
uptime = {}

# Vendor list for MAC address
scanner.scan(s.NET_ADDR, arguments=s.NMAP_ARGS2 + " --exclude " + s.EXCLUDE_IPS) #ovdje ide NMAP_ARGS2 jer je drugačija vrsta skena, vidi se u settings.py
for h in scanner.all_hosts():
    #print(dir(scanner[h]))
    if 'mac' in scanner[h]['addresses']:
        print("IP & MAC:", scanner[h]['addresses'], "\nState:", scanner[h]['status']['state'], "\nHost names:", 
        scanner[h]['hostnames'], "\nVendor:", scanner[h]['vendor'], "\nUptime:", scanner[h]['uptime']) #uptime izbacuje dictionary sa vrijednostima koliko dugo je uređaj na mreži i kad se bootao
        print('------------------------------------------------------')

        #samo provjera što je koja vrsta, nije ni potrebno u kodu
        """print(isinstance(scanner[h]['addresses'], dict))
        print(isinstance(scanner[h]['hostnames'], list))
        print(isinstance(scanner[h]['vendor'], dict))
        print(isinstance(scanner[h]['uptime'], dict))"""

        scanner[h]['uptime']['seconds'] = int(scanner[h]['uptime']['seconds']) #ovdje sam sekunde parsirao u int za lakši rad s vizualizacijom
        mydict[h] = scanner[h]['vendor'], scanner[h]['uptime']
        uptime[h] = scanner[h]['uptime']

"""print('\n')
print(mydict)
print(mydict.keys())
print(mydict.values())"""
print('\n')
print(uptime)
print(uptime.keys())
print(uptime.values())


#lastboot 'str' -> 'date'
#date_time_str = uptime['192.168.1.1']['lastboot']
#date_time_obj = datetime.datetime.strptime(date_time_str, '%a %B %d %H:%M:%S %Y') (možda ide %I umjesto %H)
#print('Date:', date_time_obj.date())