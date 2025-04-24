from socket import *  # Importa as funções da biblioteca socket

meuHost = ''  # Aceita conexões de qualquer IP
minhaPorta = 5001  # Porta do servidor

sockobj = socket(AF_INET, SOCK_STREAM)  # Cria um socket TCP
orig = (meuHost, minhaPorta)
sockobj.bind(orig)  # Associa o socket ao endereço e porta
sockobj.listen(1)  # Escuta até 1 conexão pendente

while True:
    conn, cliente = sockobj.accept()  # Aceita uma nova conexão
    print('Conectado por:', cliente)

    while True:
        recvMsg = conn.recv(1024)  # Recebe até 1024 bytes de dados
        if recvMsg == b'\x18' or not recvMsg:  # Encerra com Ctrl+X
            break
        print(cliente, recvMsg.decode())  # Imprime remetente + mensagem
    break

print('Finalizando conexão do cliente', cliente)
conn.close()  # Fecha a conexão TCP com o cliente