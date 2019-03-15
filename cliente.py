import socket

IP = "127.0.0.1"
PORT = 8085
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientsocket.connect((IP, PORT))
    print("Conexión establecida")
    send_message = input("Introduzca un numero: ")
    send_bytes = str.encode(send_message)
    clientsocket.send(send_bytes)
    print("mensaje enviado")
    condition = True
    while condition:
        respuesta = clientsocket.recv(2048).decode("utf-8")
        print (respuesta)
        if respuesta == 'Te has quemado¡, número correcto':
            condition = False
            clientsocket.close()
        else:
            mensaje = input('Vuelve a intentarlo: ')
            send_bytes = str.encode(mensaje)
            clientsocket.send(send_bytes)

except OSError:
    print("Ha habido un problema con la conexión")
    clientsocket.close()
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((IP, PORT))
except KeyboardInterrupt:
    print("La conexión se ha interrumpido")
