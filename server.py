import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', 13573))
print ('[+] Ожидания соединения')
sock.listen(0)
conn, addr = sock.accept()
print ('[+] Соединение установлено!:', addr)
conn.close()