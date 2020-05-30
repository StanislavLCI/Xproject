import socket
import pickle

spis = ['stas','pass']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1000))
s.listen(1)

while True:
	client, addr = s.accept()
	print(client)
	print("Запрос на соединение от %s" % str(addr))
	all_data = bytearray()
	data = client.recv(10000000)
	print(data)
	all_data += data
	try:
		decode = pickle.loads(all_data)
		print(decode)
		if decode == spis:
			client.sendall(pickle.dumps(['Данные верны...', '1']))
		else:
			client.sendall(pickle.dumps(['Данные не верны...', '0']))
	except:
		pass
	client.close()