
import socket


if __name__ == "__main__":

	HOST = 'localhost'
	PORT = 12345
	MAXDATA = 2048

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.send('this is oitate')
	data = s.recv(MAXDATA)
	s.close()
	print 'Received : ', repr(data)

	
