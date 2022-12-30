from netmiko import ConnectHandler
'''
CSR={
    #"device_type":"cisco_ios",
    "ip":"sandbox-iosxe-latest-1.cisco.com",
    "username":"developer",
    "password":"C1sco12345"
}
net_connect=ConnectHandler(**CSR)
output=net_connect.send_command('show ip int brief')
print(output)
net_connect.disconnect()


with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            "device_type": "cisco_ios",
            "ip": "sandbox-iosxe-latest-1.cisco.com",
            "username": "developer",
            "password": "C1sco12345"
        }
        net_connect = ConnectHandler(**Router)

        print('connecting to ' + IP)
        print('-' * 79)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-' * 79)

net_connect.disconnect()




with open('devices.txt') as routers:
    for IP in routers:
        CSR = {
            "device_type": "cisco_ios",
            "ip": "sandbox-iosxe-latest-1.cisco.com",
            "username": "developer",
            "password": "C1sco12345"
        }
net_connect=ConnectHandler(**CSR)
#output=net_connect.send_command('show ip int brief')
#print(output)
#net_connect.disconnect()
#Discover the host name from the prompt
hostname=net_connect.send_command('show run | i host')
#hostname=net_connect.send_command('show clock')
hostname.split(" ")
hostname,device,*rest=hostname.split(" ")
#*rest
print("Backing up"+device)
filename="C:/Users/user696/PycharmProjects/pythonProject3/devices04.txt"
showrun=net_connect.send_command('show run')
showvlan=net_connect.send_command('show vlan')
showver=net_connect.send_command('show ver')
log_file=open(filename,"a")#in append mode
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")
net_connect.disconnect()
'''
'''

#method name is join by using after 2 hexa decimal places -regularexpression
from getmac import get_mac_address as gma
print(gma())
C:\Users\user696\Pythoncode>python rupa4.py
00:50:56:bc:76:3f

#printing the value of undiue MAC 
#address using uuid and getnode() function

import uuid
print(hex(uuid.getnode()))
C:\Users\user696\Pythoncode>python rupa4.py
0x5056bc763f


import uuid
print("The MAC address in formated way is:",end="")
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)]))

#The MAC address in formated way is:3f:76:bc:56:50:00
import uuid
print("The MAC address in formated way is:",end="")
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))
#The MAC address in formated way is:00:50:56:bc:76:3f-Negatvie indexing

'''

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)























