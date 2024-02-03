import socket

s = socket.socket()
s.bind(('localhost', 3030))
s.listen(1)
conn, addr = s.accept()
print(addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall("WELCOME AND CAREFULY!") 
    print(data.decode('utf-8'))
conn.close()