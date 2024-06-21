import socket

ports = [20, 21, 22, 23, 25, 53, 80, 110, 123, 143, 161, 443, 465, 587, 636, 993, 995, 1080, 1433, 1521, 3306, 3389, 5432, 5900, 6379, 6443, 8000, 8080, 8443, 8888]

for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	client.settimeout(0.1)
	code = client.connect_ex(("bancocn.com", port))
	if code == 0:
		print(port, "OPEN")
	else: 
		pass
	client.close()
