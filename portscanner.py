#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

ip    = raw_input("Enter host ")
ip_addr  = socket.gethostbyname(ip)

print "-" * 60
print "Wait"
print "-" * 60

t1 = datetime.now()

try:
    for port in range(1,1024):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip_addr, port))
		
        if result == 0:
            print "Port {}: 	 Open".format(port)
            #print sock.recv(1024)
	sock.close()

except KeyboardInterrupt:
    print "Exit"
    sys.exit()

t2 = datetime.now()
total =  t2 - t1
print 'Scan time: ', total

