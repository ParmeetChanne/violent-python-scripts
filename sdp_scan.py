# The Bluetooth Service Discovery Protocol (SDP)

# Potentially tells the host, name, description,provider, protocol,
# port, service-class, profiles, and service ID for each
# available service on the Bluetooth target

from bluetooth import *


def sdpBrowse(addr):
    services = find_service(address=addr)
    for service in services:
        name = service['name']
        proto = service['protocol']
        port = str(service['port'])
        print('[+] Found ' + str(name)+' on ' +
              str(proto) + ':'+port)


sdpBrowse('60:8E:08:A1:3D:AA')
