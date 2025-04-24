from socket import *

meuHost = '127.0.0.1'
minhaPorta = 5001

sockobj = socket(AF_INET, SOCK_STREAM)
dest = (meuHost, minhaPorta)
sockobj.connect(dest) # Conecta ao servidor TCP

print('Para sair use CTRL+X\n')
msg = ''
while msg != '\x18':
    msg = input() # Usuário digita mensagem
    sockobj.send(msg.encode())  # Envia ao servidor
    
    recvMsg = sockobj.recv(1024) # Espera a resposta
    print('Resposta: ', recvMsg.decode()) # Exibe a resposta (eco)

sockobj.close() # Fecha conexão
