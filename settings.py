#ako budeš vrtio kod, vjerojatno ćeš morati mijenjati NET_ADDR u svoj IP, inače kontam da ti neće raditi
NET_ADDR = '192.168.1.0/24'
NMAP_ARGS = '-O -F -sN -PE -PA21,22,23,80,3389'
NMAP_ARGS2 = '-O -F -sS -PE -PA21,22,23,80,3389'
EXCLUDE_IPS = '192.168.1.107' #ovdje stavi IP svog kompa jer inače neće raditi