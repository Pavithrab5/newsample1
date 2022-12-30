'''
#packet transfer
from scapy.all import*
my_frame=Ether()/TCP()
print(my_frame)
print(my_frame.show())


from scapy.all import*
s=IP(dst="google.com")/ICMP()
print(s.show())
'''
from scapy.all import *
a=IP(ttl=10)
print(a)
print(a.src)

'''
a.dst="192.168.1.1"
print(a)
print(a.src)#default gateway


del(a.tt1)
print(a.show())

b=IP()
print(b.show())



c=IP()/TCP()
print(c.show())

d=Ether()/IP()/TCP()
print(d.show())

e=IP()/TCP()/"GET/HTTP/1.0\r\n\r\n"#adding body of the packet 
print(e.show())


j=a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET / index.html HTTP/1.0\n\n"
print(hexdump(j))


k=IP(dst="www.slashdot.org/30")
dst=Net('www.slashdot.org/30')
print([p for p in k])
'''
#4 different packets are coming
import pexpect
print(pexpect.run('echo run'))
