from socket import socket, AF_INET, SOCK_DGRAM, timeout

IP_Servidor = '127.0.0.1' 
# Endereco IP do Servidor
             
PORTA_Servidor = 5000                  
# Porta em que o servidor estara ouvindo

MEU_IP = ''                                
# Endereco IP '' = significa que ouvira em todas as interfaces

MINHA_PORTA = 7000
# Porta que o cliente1 vai ouvir

cliente1 = socket(AF_INET, SOCK_DGRAM)
#  socket.SOCK_DGRAM=usaremos UDP

cliente1_serv = (MEU_IP, MINHA_PORTA) 
cliente1.bind(cliente1_serv)
print("O cliente1 está ligado!")

DESTINO = (IP_Servidor, PORTA_Servidor) 
#destino(IP + porta) do Servidor

seq = 0

while(True):
    Mensagem = input("Digite a mensagem: ")   
    # Mensagem recebera dados do teclado           

    cliente1.sendto (str(seq).encode() + Mensagem.encode(), DESTINO)
    # enviar a mensgem para o destino(IP + porta)
    #bytes(Mensagem,"utf8") = converte tipo  str para byte
    
    if(Mensagem == "quit"):
        print("Encerrando comunicação...")
        break

    Mensagem_Recebida, END_cliente = cliente1.recvfrom(1024)
    mensagem = Mensagem_Recebida.decode("utf-8")
    seq_r = mensagem[:1]
    mensagem = mensagem[1:]
    
    if len(Mensagem_Recebida) is not None:
        print ("Recebi =", mensagem,", do cliente", END_cliente, "numero de sequencia = ", seq_r, "\n")
        # endereco eh o endereco do socket que enviou os dados.      

cliente1.close()
# fim socket
