import socket

def scanport(ipaddress,port):
	try:
		sock=socket.socket()
		sock.connect((ipaddress,port))
		print("Port Opened: "+str(port))
		sock.close()
	except:
		print("Port Closed: "+str(port))
ipaddress=input("Enter Your IPs to Scan: ")
port=int(input("Enter Port To Scan: "))
scanport(ipaddress,port)

