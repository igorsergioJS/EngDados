# â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—   DEPTO DE ENGENHARIA DE
# â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—  COMPUTACAO E AUTOMACAO
# â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘  UFRN, NATAL-RN, BRASIL
# â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘   
# â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘  PROF CARLOS M D VIEGAS
# â•šâ•â•â•â•â•â•  â•šâ•â•â•â•â•â•â•šâ•â•  â•šâ•â•  viegas '@' dca.ufrn.br
#
# SCRIPT CLIENTE TCP (python3)
#
# COMO EXECUTAR?
# ?> python clienteTCP.py <endereco-ip-do-servidor>
#

# importacao das bibliotecas
from socket import *
import sys
import time

# definicao das variaveis
serverName = str(sys.argv[1])
serverPort = 30000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

sentence = 'hostname: ' + gethostname() + ' ip: ' + gethostbyname(gethostname())
print ('> enviando para o servidor -> %s' % sentence)
clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor
time.sleep(2)
clientSocket.close() # encerramento o socket do cliente
