import socket as sc

#porta e host
host = 'localhost'
port = 8585

#objeto do tipo socket IPV4 - UDP
udp_client = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

udp_client.sendto("Ola servidor!".encode(), (host, port))

while True:
    msg = input("Informe a msg a ser enviada para o servidor: ")
    udp_client.sendto(msg.encode(), (host, port))

    print("Informação devolvida do servidor: ")
    msg_recebida, addr = udp_client.recvfrom(1024)
    print(msg_recebida.decode())
    
