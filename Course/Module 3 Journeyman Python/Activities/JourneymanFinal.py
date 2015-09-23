import socket
'''
1.5) Python Journeyman: Write a Python server which:
	receives a connection from the included client (JourneymanFinal.py)
	stores received data in a file, then adds the file to a list
	returns the data from the file when requested
	deals with errors and missing files
'''

def main():
	HOST = ''
	PORT = 50001
	MAX_CONNECTIONS = 5
	BUFFER_SIZE = 512
	FILE_NAME = 'server.txt'

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	print 'Server listen'
	conn, addr = s.accept()
	print 'Server accept'
	str = conn.recv(BUFFER_SIZE)
	print str
	f = open(FILE_NAME,  'w+')



	# while str != 'close':
	f.write(str+'\n')
	str = conn.recv(128)
	print str
	print len(str)

	f.close()
	conn.close()
	s.close()
	return


main()
