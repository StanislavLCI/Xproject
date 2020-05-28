import socket
import pickle

spis = ['stas','pass']

wn = '1'
n = '0'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1000))
s.listen(1)

while True:
	client, addr = s.accept()
	print(client)
	print("Запрос на соединение от %s" % str(addr))
	all_data = bytearray()
	data = client.recv(10000000)
	all_data += data
	try:
		decode = pickle.loads(all_data)
		print(decode)
		if decode == spis:
			client.send(wn.encode('utf-8'))
		else:
			client.send(n.encode('utf-8'))
	except:
		pass
	client.close()