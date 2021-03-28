import socket

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketServer.bind(('127.0.0.1', 1234))

socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socketServer.listen(9)

while True:
  clientsocket, address = socketServer.accept()
  message = clientsocket.recv(1024)
  print(message.decode('UTF-8'))
  clientsocket.send('halo fram server'.encode('utf-8'))

socketServer.close()
