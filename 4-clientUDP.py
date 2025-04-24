from socket import *  # Importa funções da biblioteca socket

meuHost = '127.0.0.1'  # Endereço IP do servidor (localhost)
minhaPorta = 5000  # Porta onde o servidor está escutando

sockobj = socket(AF_INET, SOCK_DGRAM)  # Cria um socket UDP

dest = (meuHost, minhaPorta)  # Define o endereço de destino (host, porta)

print('Para sair use CTRL+X\n')  # Mensagem para o usuário
msg = ''  # Inicializa a variável da mensagem

# Loop principal do cliente
while msg != '\x18':  # Envia mensagens até o usuário digitar Ctrl+X
    msg = input()  # Lê entrada do usuário
    sockobj.sendto(msg.encode(), dest)  # Envia a mensagem codificada (em bytes) para o servidor

sockobj.close()  # Fecha o socket e encerra o cliente