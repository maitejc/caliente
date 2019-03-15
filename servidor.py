import socket
import random
PORT = 8085
IP = "127.0.0.1"
numero_aleatorio =random.random()*99
numero_aleatorio = int(numero_aleatorio)
print (numero_aleatorio)
def process_client(clientsocket):
    print(clientsocket)
    condition = True
    while condition:
        numero = (clientsocket.recv(2048).decode("utf-8"))
        print("El número introducido es:", numero)
        numero = int(numero)
        if numero == numero_aleatorio:
            mensaje= 'Te has quemado¡, número correcto'
            send_bytes = str.encode(mensaje)
            clientsocket.send(send_bytes)
            condition = False
            clientsocket.close()

        elif numero_aleatorio - 10<= numero <= numero_aleatorio + 10:
            mensaje = "Caliente Caliente, andas cerca"
            send_bytes = str.encode(mensaje)
            clientsocket.send(send_bytes)
            condition = True

        elif numero >numero_aleatorio+10:
            mensaje = "Frío, introduce un número menor"
            send_bytes = str.encode(mensaje)
            clientsocket.send(send_bytes)
            condition = True

        elif numero <numero_aleatorio-10:
            mensaje = "Frío, introduce un número mayor"
            send_bytes = str.encode(mensaje)
            clientsocket.send(send_bytes)
            condition = True
    clientsocket.close()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(5)
    while True:
        print("Esperando conexiones")
        (clientsocket, address) = serversocket.accept()
        process_client(clientsocket)

except socket.error:
    print("Problemas de conexión")
except KeyboardInterrupt:
    print("La conexión se ha interrumpido")


