"""
Banner-grabbing script -> print the banner after
connecting to specific ip and port.
Then we use connect() method to make a network connection
to the IP and port.
"""


"""
Now we would like to know if the specific FTP server
is vulnerable to attack.
"""


import socket
socket.setdefaulttimeout(2)
s = socket.socket()
try:
    s.connect(("192.168.95.148", 21))
except Exception as e:
    print("[-] Error = " + str(e))

ans = s.recv(1024)
if ("Freefloat Ftp Server (Version 1.00)" in ans):
    print("[+] Freefloat FTP  server is vulnerable")
elif ("3Com 3CDaemon FTP Server Version 2.0" in banner):
    print("[+] 3CDaemon FTP Server is vulnerable.")
elif ("Ability Server 2.34" in banner):
    print("[+] Ability FTP Server is vulnerable.")
elif ("Sami FTP Server 2.0.2" in banner):
    print("[+] Sami FTP Server is vulnerable.")
else:
    print("[-] FTP Server is not vulnerable.")
