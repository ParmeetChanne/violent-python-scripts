from bluetooth import *


def rfcommCon(addr, port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((addr, port))
        print('[+] RFCOMM Port ' + str(port) + ' open')
        sock.close
    except Exception as e:
        print('[-] RFCOMM Port ' + str(port) + ' closed')


for port in range(1, 30):
    rfcommCon('20:AD:56:61:F7:F2', port)
