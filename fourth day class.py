
'''
import ifaddr
adapters=ifaddr.get_adapters()
for adapter in adapters:
    print("IPs  of network adapter"+adapter.nice_name)
    for ip in adapter.ips:
        print("%s%s"%(ip.ip, ip.network_prefix))

'''
#if you wish to include interfaces that do not have a configured IP address ,pass the
#include_unconfigured parameters Adapaters with no configured IP address will have an zero-length
#ips property
'''



import ifaddr
adapters=ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("IPs  of network adapter"+adapter.nice_name)
    if adapter.ips:
        for ip in adapter.ips:
            print("%s%s" % (ip.ip, ip.network_prefix))
    else:
        print("No IPs configured")


import psutil
result01=psutil.cpu_times()
result02=psutil.disk_partitions()
result03=psutil.cpu_freq()
result04=psutil.cpu_stats()
result05=psutil.net_io_counters(pernic=True)
#result06=psutil.net_io_counters()
bytes_sent=getattr(network_stats,'bytes_sent')
print(result05)
print(result06)


import psutil
network_stats=psutil.net_io_counters(pernic=False)
bytes_sent=getattr(network_stats,'bytes_sent')
bytes_recv=getattr(network_stats,'bytes_recv')
print("bytes sent=",bytes_sent)
print("bytes recived=",bytes_recv)
print(type(bytes_sent))
res="Bytes sent={0} | Bytes Received ={1}".format(bytes_sent,bytes_recv)
print(res)
print(type(res))

import socket
import subprocess
import sys
from datetime import datetime
#Blank your screen
#subprocess.call('clear',shell=True)
#ask for input
remoteServer=input("enter a remote host to scan: ")#ipv4 address
remoteServerIP=socket.gethostbyname(remoteServer)
print("please wait ,scanning remote host",remoteServerIP)
print("_"*60)
#check the date and time the scan was started
t1=datetime.now()
print(t1)
#using the range function to specify ports
#also we will do error handling
try:
    for port in range(1,5000):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#connection meta parameter
        result=sock.connect_ex((remoteServerIP,port))#checking 1,port return t/f,then 2,port return t/f,
        if result==():
            print("Port {}:   Open".format(port))
            sock.close()
except KeyboardInterrupt:
    print("you pressed ctrl+c")
    sys.exit()
except socket.gaierror:
    print("hostname cloud not be reslove.Exiting")
    sys.exit()
except socket.error:
    print("Cloud not connect to server")
    sys.exit()


import scapy.all as scapy
request=scapy.ARP()

import scapy.all as scapy
request=scapy.ARP()
print(request.summary())
#local hostis generating address -self generating addresss


import scapy.all as scapy
request=scapy.ARP()
print(request.show())


from scapy.all import *
ip=IP()
print(ip)
print(ip.show())

'''





