"""
Function to perform connecting to FTP serer and returning
the banner
"""
import socket
import os
import sys


def returnBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

# reading lines from "vuln_banners.txt" file.
# striping lines 1 by 1 to check them.


def checkVulns(banner):
    f = open("vuln_banners.txt", 'r')
    for line in f.readlines():
        if line.strip("\n") in banner:
            print("[+] Server is vulnerable: " + banner.strip('\n'))


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("[-] " + filename + ' does not exist')
            exit(0)
        else:
            print("[-] Usage: " + str(sys.argv[0]) + '<vuln filename>')
            exit(0)
            portList = [21, 22, 25, 80, 110, 443]
            for x in range(147, 150):
                ip = '192.168.95.' + str(x)
                for port in portList:
                    banner = retBanner(ip, port)
                    if banner:
                        print('[+] ' + ip + ': ' + banner)
                        checkVulns(banner, filename)


if __name__ == "_main_":
    main()
