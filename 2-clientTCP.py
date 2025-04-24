from socket import *

meuHost = '127.0.0.1'  # Endereço IP local
minhaPorta = 5001  # Porta do servidor

sockobj = socket(AF_INET, SOCK_STREAM)  # Cria socket TCP
dest = (meuHost, minhaPorta)
sockobj.connect(dest)  # Estabelece conexão TCP com o servidor

print('Para sair use CTRL+X\n')
msg = ''
while msg != '\x18':  # Enquanto a mensagem não for Ctrl+X
    msg = input()  # Lê entrada do usuário
    sockobj.send(msg.encode())  # Envia a mensagem ao servidor

sockobj.close()  # Fecha a conexão