import socket
host='192.168.0.7'
port=65432
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect ((host,port))

cont=0
mensajes=3
permitidos=mensajes+1



print('Iniciamos cliente, en conexion con servidor IP= ', host,  'puerto de escucha= ', port)
print('usted tiene ', mensajes, ' mensajes a enviar para el servidor')
while True:
    
    
    enviar=input('cliente: ')

    
    
    if(len(enviar)>40):
        print('error,  maximo permitido son 40 caracteres')
        enviar=input ('escriba nuevamente su mensaje: ')

    cont+=1
    if cont==permitidos:
        print('mensaje no enviado, ha mandado el maximo de mensajes permitidos')
        s.close()





    s.send (enviar.encode(encoding='ascii'))
    recibido=s.recv(100)
    print('servidor', recibido.decode(encoding='ascii'))


s.close()