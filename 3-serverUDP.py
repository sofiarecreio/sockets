from socket import *  # Importa todas as funções da biblioteca socket (API de rede padrão em Python)

meuHost = ''  # O host em branco indica que o servidor aceitará conexões de qualquer endereço IP
minhaPorta = 5000  # Define a porta onde o servidor irá escutar as mensagens

# Cria o socket UDP (SOCK_DGRAM). AF_INET = IPv4
sockobj = socket(AF_INET, SOCK_DGRAM)

orig = (meuHost, minhaPorta)  # Endereço do servidor (host, porta)

sockobj.bind(orig)  # Associa (vincula) o socket ao endereço e porta especificados

# Loop principal do servidor
while True:
    recvMsg, cliente = sockobj.recvfrom(1024)  # Espera (bloqueia) até receber uma mensagem de até 1024 bytes
    if recvMsg == b'\x18' or not recvMsg:  # Se a mensagem for Ctrl+X (byte 0x18) ou vazia, interrompe
        break
    print(cliente, recvMsg.decode())  # Imprime o endereço do cliente e a mensagem recebida (convertida de bytes para string)

sockobj.close()  # Fecha o socket e encerra o servidor