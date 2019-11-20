
import socket 
import webbrowser 


host = '' 
port = 7000 
addr = (host, port) 

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serv_socket.bind(addr) 

while 1: 
    serv_socket.listen(10) 
    print ('aguardando conexao' )
    con, cliente = serv_socket.accept() 
    print ('conectado com: ' )
    print (cliente)
    print ("aguardando mensagem" )
    recebe = con.recv(1024) 
    print('recebido: '+recebe.decode('utf-8'))
    #webbrowser.open_new(recebe)
serv_socket.close() 