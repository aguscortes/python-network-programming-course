#!/bin/python
import scapy.all as scapy
import optparse


def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option('-i', '--ip', dest='ip', help='IP target')
	(options, arguments) = parser.parse_args()
	if not options.ip:
		parser.error('Please specify an ip, use --help form more info')
	return options


def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

	print('IP\t\t\tMAC Address\n---------------------------------------')
	for element in answered_list:
		print(element[1].psrc + '\t\t' + element[1].hwsrc)


options = get_arguments()
scan(options.ip)