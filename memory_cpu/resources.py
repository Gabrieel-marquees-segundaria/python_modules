from psutil import virtual_memory, cpu_percent, net_io_counters


def exemple():
	import psutil
	# Uso da CPU em %
	#print(f"Uso da CPU: {psutil.cpu_percent(interval=1)}%")
	
	# Uso da memória RAM
	mem = psutil.virtual_memory()
	print(f"Uso da RAM: {mem.percent}% ({mem.used / (1024 ** 3):.2f} GB usados)")

#	 Uso de Rede
	net = psutil.net_io_counters()
	print(f"Bytes enviados: {net.bytes_sent / (1024 ** 2):.2f} MB")
	print(f"Bytes recebidos: {net.bytes_recv / (1024 ** 2):.2f} MB")
	
	import os
	
	# Reduz a prioridade do processo (maior valor = menor prioridade)
	os.nice(10)

	from multiprocessing import Pool, cpu_count
	
	def trabalho(x):
	    return x * x
	
	with Pool(processes=cpu_count() // 2):  # Usa metade dos núcleos disponíveis
	    print("Executando com menos núcleos...")
	
	import resource
	
	# Define um limite de 500 MB de RAM
	resource.setrlimit(resource.RLIMIT_AS, (500 * 1024 * 1024, 500 * 1024 * 1024))	

	import socket
	# limita o trafego
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)  # Define um tempo máximo para conexões
	
	

class ResourceUsege:
	#net = net_io_counters()
	
	def ram(self):
		"""
		uso de memoria ram
		
		"""
		mem = virtual_memory()
		return 
	
	def cpu(self, interval=1):
		"""
		uso de cpu em porcentagem
		
		args:
			interval: intervalo de medida defalt: interval=1
		"""
		return cpu_percent(interval=interval)
		
	def bytes_send(self):
		"""
		bytes enviados
		
		"""
		return self.net.bytes_sent
	
	def bytes_recv(self):
		return self.net.bytes_recv
		

class Limites:
	import  os
	os = os
	def priority(self,num: int):
		"""
		redus a prioridade do processo
		
		args:
			num: quanto maior o valor de num menor a prioridade do procesdo
		"""
		self.os.nice(num)
		
				
						
		
