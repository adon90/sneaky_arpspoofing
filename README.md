# sneaky_arpspoofing
This is an arpspoofing tool based on arp requests that knows when to send the arp request not to cause noise in the LAN.
The arp request is sent when the target ARP tables changes, that involves 2 cases:
- When there is an arp replay comming from the IP to be spoofed.
- Where there is an arp request to our target that doesn't come from us.

This requires scapy
