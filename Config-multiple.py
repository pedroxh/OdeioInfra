import getpass
import sys
import telnetlib

HOST = "localhost"
#IRÁ ACESSAR ALGO QUE ESTÁ DENTRO DA MAQUINA ONDE O PYTHON ESTÁ#
user = input("Digite o seu usuario: ")
password = getpass.getpass()

lista_routers = open ('Routers-ip')
#ESSA VARIAVEL VAI ABRIR O ARQUIVO QUE CRIAMOS COM O IP DOS ROUTERS QUE CHAMAMOS DE "ROUTERS-IP"#

for ip in lista_routers:
    #ESSE FOR (LOOP) IRÁ REALIZAR A CONEXÃO EM TODOS OS IPS DA LISTA#
    ip = ip.strip()
    #IRÁ REMOVER QUALQUER ESPAÇO EM VAZIO DA VARIAVEL IP#
    print ('Estamos configurando o router' + (ip))
    HOST = ip
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
       tn.write(b"conf t\n")
    for interface_loopback in range (4):
        tn.write (b"interface loopback" + str (interface_loopback) . encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))