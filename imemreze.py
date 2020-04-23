import nmap
import time

scanner = nmap.PortScanner()

scanner.scan('192.168.1.1', '0-443', '-sS')
print(scanner['192.168.1.1'].hostname())
print(scanner.command_line())
print(scanner.scaninfo())
print(scanner.all_hosts())
print(scanner['192.168.1.1'].all_protocols())
print(scanner['192.168.1.1']['tcp'].keys())
print(scanner['192.168.1.1'].keys())
for host in scanner.all_hosts():
    print('-------------------')
    print('Host:', host, "(", scanner[host].hostname(), ")")
    print('State:', scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('-------------------')
        lport = scanner[host][proto].keys()
        for port in lport:
            print('port:', port, "\tstate:", scanner[host][proto][port]['state'])    
#print(scanner.csv())


#IP za mobitel, kod će raditi samo ako je otključan i na mreži
"""print("\n")
scanner.scan('192.168.1.100', '0-24', '-sS')
print(scanner['192.168.1.100'].hostname())
print(scanner.command_line())
print(scanner.scaninfo())
print(scanner.all_hosts())
print(scanner['192.168.1.100'].all_protocols())
print(scanner['192.168.1.100']['tcp'].keys())
for host in scanner.all_hosts():
    print('-------------------')
    print('Host:', host, "(", scanner[host].hostname(), ")")
    print('State:', scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('---------')
        lport = scanner[host][proto].keys()
        for port in lport:
            print('port:', port, "\tstate:", scanner[host][proto][port]['state'])"""

"""print("\n")
scanner.scan('192.168.1.101', '0-443', '-sS')
print(scanner['192.168.1.101'].hostname())
print(scanner.command_line())
print(scanner.scaninfo())
print(scanner.all_hosts())
print(scanner['192.168.1.101'].all_protocols())
print(scanner['192.168.1.101']['tcp'].keys())
for host in scanner.all_hosts():
    print('-------------------')
    print('Host:', host, "(", scanner[host].hostname(), ")")
    print('State:', scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('---------')
        lport = scanner[host][proto].keys()
        for port in lport:
            print('port:', port, "\tstate:", scanner[host][proto][port]['state'])
#print(scanner.csv())

print("\n")
scanner.scan('192.168.1.107', '0-443', '-sS')
print(scanner['192.168.1.107'].hostname())
print(scanner.command_line())
print(scanner.scaninfo())
print(scanner.all_hosts())
print(scanner['192.168.1.107'].all_protocols())
print(scanner['192.168.1.107']['tcp'].keys())
for host in scanner.all_hosts():
    print('-------------------')
    print('Host:', host, "(", scanner[host].hostname(), ")")
    print('State:', scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('---------')
        lport = scanner[host][proto].keys()
        for port in lport:
            print('port:', port, "\tstate:", scanner[host][proto][port]['state'])

#print(scanner.csv())"""

print('\n')
scanner.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
print(hosts_list)

"""for host, status in hosts_list:
    print(([0][1]).host)"""