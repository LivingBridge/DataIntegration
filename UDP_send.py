import socket
# address info of target
ipaddr="192.168.54.02"
portnum=256
#build the packet data. should be a gps string. no need for .decode('hex'), right?
packetdata="This is a test string"
#initialize a socket. dgram specifies UDP
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#send the packet
s.sendto(bytes(packetdata, "utf-8"),(ipaddr,portnum))

