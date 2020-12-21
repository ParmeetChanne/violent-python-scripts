"""
While most networks advertise their network name (BSSID), some wireless
networks use a hidden SSID to protect discovery of the network name. The Info
field in the 802.11 Beacon Frame typically contains the name of the network.
In hidden networks, the access point leaves this field blank. Detecting a hidden
network proves rather easy, then, because we can just search for 802.11 Beacon
frames with blank info fields. In the following example, we will search for these
frames and print out the MAC address of the wireless access point.
"""


import sys
from scapy.all import *

interface = 'wlan0'
hiddenNets = []
unhiddenNets = []


def sniffDot11(p):
    if p.haslayer(Dot11ProbeResp):
        addr2 = p.getlayer(Dot11).addr2
        if (addr2 in hiddenNets) & (addr2 not in unhiddenNets):
            netName = p.getlayer(Dot11ProbeResp).info
            print('[+] Decloaked Hidden SSID: ' +
                  netName + ' for MAC: ' + addr2)
            unhiddenNets.append(addr2)
    if p.haslayer(Dot11Beacon):
        if p.getlayer(Dot11Beacon).info == '':
            addr2 = p.getlayer(Dot11).addr2
            if addr2 not in hiddenNets:
                print('[-] Detected Hidden SSID: ' +
                      'with MAC:' + addr2)
            hiddenNets.append(addr2)


sniff(iface=interface, prn=sniffDot11)
