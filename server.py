#modulo
import socket as sc

#definindo a tupla (endereço; porta)
host = 'localhost'
port = 8585

#definindo o soquete - tipo IPV4 e UDP
udp = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

udp.bind( (host, port) )

msg = "Conexao bem sucedida!"
msg2 = "Retorno do servidor!"

msg_recebida, addrs = udp.recvfrom(1024)
udp.sendto(msg.encode(), addrs)

while True:
    msg_recebida, addrs = udp.recvfrom(1024)
    
    print(msg_recebida.decode())

    udp.sendto(msg2.encode(), addrs)
    