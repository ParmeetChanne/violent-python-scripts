import optparse
import socket
from socket import *
from threading import *

"""
The portScan function
takes the hostname and target ports as arguments. It will first attempt to
resolve an IP address to a friendly hostname using the gethostbyname() function.
Next, it will print the hostname (or IP address) and enumerate through
each individual port attempting to connect using the connScan function.
The connScan function will take two arguments: tgtHost and tgtPort and attempt
to create a connection to the target host and port. If it is successful, connScan
will print an open port message. If unsuccessful, it will print the closed port
message
"""

screenLock = Semaphore(value=1)


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socekt(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print("[+] %d/tcp open" % tgtPort)
        print("[+] " + str(results))
    except:
        screenLock.acquire()
        print("[-] %d/tcp closed" % tgtPort)
    finally:
        screenLock.acquire()
        connSkt.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve %s : Unknown Host" % tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)
    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print("Scanning port" + tgtPort)
        connScan(tgtHost, int(tgtPort))


def main():
    parser = optparse.OptionParser(
        "usage%prog " + "-H <target host> -p <target port>")
    parser.add_option(option('-H', dest='tgtHost',
                             type='string', help='specify target host'))
    parser.add_option('-p', dest='tgtPort', type='string',
                      help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(', ')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()
