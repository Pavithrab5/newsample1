
'''
import os, ipaddress
os.system('cls')#os.system will clear the console at the start of the exceution
while True:
    ip= input('enter ip address')
    try:
        print(ipaddress.ip_address(ip))
        print('IP Valid')
    except:
        print('-'*50)
        print('IP is not valid')
    finally:
        if ip=='mango':
            print('Script Finished')
            break

import  os
print(os.system("ipconfig"))


import socket
s=socket.socket()
print("socket successfully created")
port=4067
s.bind(('',port))
print("socket bindedto %s "%(port))
s.listen(5)
print("socket is listening")
while True:
    c,addr=s.accept()#single line,multivariable assignment
   # print("Got connection from",addr)
    c.send(b'Thank you for connecting')#to client
    c.close()



import socket
#s.blind()::2 args::[IP/host/connection +port]
port=" "
connection is intailized by 

'''


from netmiko import ConnectHandler
#first create the device object using a dictionary
CSR={
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxc-latest-1.cisco.com",
    "username":"developer",
    "password":""
               "C1sco12345"
}
net_connect= ConnectHandler(**CSR)
output_runhost=net_connect.send_command('show run | host')
print(output_runhost)





























