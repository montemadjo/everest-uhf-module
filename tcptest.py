#jajara
import socket

TCP_IP = '192.168.1.200'
TCP_PORT = 100
BUFFER_SIZE = 1024
# MESSAGE = bytes.fromhex('0aff0222d3')
MESSAGE = bytes.fromhex('0aff0244b1')
# MESSAGE = bytes.fromhex('0aff03800074')
# MESSAGE = bytes.fromhex('0aff034110a3')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
print("received data:" + str(data))
