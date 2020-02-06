from socket import *
import io

def main():
	serverSocket = socket(AF_INET, SOCK_STREAM) # TCP SERVER SOCKET
	serverhost='localhost'
	rbuffer=1024
	serverport=1234
	
	serverSocket.bind(('',serverport))
	serverSocket.listen(5)
	
	while True:
		print ("server is ready")
		connectionSocket,addr=serverSocket.accept()
	
		try:
			message=connectionSocket.recv(1024)
		
			filename=message.split()[1]
			f=open(filename[1:])
			outputdata=f.read()
			connectionSocket.send(('\nHTTP/1.1 200 OK\n\n').encode())
		
			for i in range(0,len(outputdata)):
				connectionSocket.send(outputdata[i].encode())
			connectionSocket.close()
		except IOError:
			serverSocket.close()
	pass


main()
