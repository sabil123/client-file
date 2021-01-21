import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONECT_MSG = "Disconected"
SERVER = "192.168.29.183"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b"" * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

m = input("type ur msg")
send(m)
