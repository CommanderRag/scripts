import socket 

test = socket.socket()

test.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

test.connect(('127.0.0.1', 1234))

message = input("Enter Message:")

test.send(message.encode('UTF-8'))

while True:
  mes = test.recv(1024)
  if(mes.decode('utf-8') != ''):
    print(mes.decode('utf-8')) 
test.close()
