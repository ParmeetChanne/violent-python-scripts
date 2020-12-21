"""
In an attempt to provide seamless connectivity, your computer and phone often
keep a preferred network list, which contains the names of wireless networks you
have successfully connected to in the past. Either when your computer boots up
or after disconnecting from a network, your computer frequently sends 802.11
Probe Requests to search for each of the network names on that list.
"""

from scapy.all import *

interface = 'mon0'
probeReqs = []


def sniffProbe(p):
    if p.haslayer(Dot11ProbeReq):
        netName = p.getlayer(Dot11ProbeReq).info
        if netName not in probeReqs:
            probeReqs.append(netName)
            print('[+] Detected New Probe Request: ' + netName)


sniff(iface=interface, prn=sniffProbe)
