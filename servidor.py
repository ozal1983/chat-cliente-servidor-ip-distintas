import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind (('',65432))
s.listen(5)
print ("servidor en espera de conexion con cliente")
print("PARA SALIR DEL CHAT TECLE 'ESC' ")
conexion, addr=s.accept()

while True:
    recibido=conexion.recv(100)
    print("cliente: ", recibido.decode(encoding='ascii'))

    enviar=input("server: ")
    if (len(enviar)>40):
        print('error, el maximo permitido de caracteres son 40')
        enviar=input('escriba nuevamente su mensaje: ')

    if enviar=='ESC':
        enviar=("EL SERVIDOR SE HA DESCONECTADO, TERMINA CONEXION")
        conexion.send(enviar.encode(encoding="ascii"))
        conexion.close()
    
    conexion.send(enviar.encode(encoding="ascii"))

conexion.close()

