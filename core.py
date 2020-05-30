import socket
import pickle
import time

server_host = 'localhost'
port_host = 1000

class sock:
	global server_host, port_host
	def sock_conn_test(self, server = server_host, port = port_host):
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((server, port))
			self.sock.close()
			return True
		except:
			pass

	def verefy_profile(self, name, password, server = server_host, port = port_host):
		self.name = name
		self.password = password
		all_data = bytearray()
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect_ex((server, port))
		sock.sendall(pickle.dumps([name, password]))
		data = sock.recv(1000000)
		all_data += data
		decode = pickle.loads(all_data)
		print(decode)
		sock.close()
		return decode

