import socket
import time
import threading

class httpthread(threading.Thread):    
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.conn = conn

	def run(self):
		data = conn.recv(1024)
		conn.send(data)
		conn.close()
        
if __name__ == "__main__":

	HOST = 'localhost'
	PORT = 12345

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(5)

	while True:
		conn, addr = s.accept()
		print 'Connected by ', addr 
		st = httpthread(conn)
		st.start()
    
	s.close()



