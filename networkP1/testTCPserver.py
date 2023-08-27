from socket import *
serverPort = 700
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    ip = addr[0]
    port = addr[1]
    print('Got connection from',"IP: " + ip + ", Port: " + str(port))
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
    connectionSocket.send('Content-Type: text/html \r\n'.encode())
    connectionSocket.send('\r\n'.encode())
    #testF = open(r"C:\Users\Microsoft\Desktop\networkP1\birzeit.png","rb")
    s=("""<!DOCTYPE html>
<html>
<body>

<h1>HTML Links</h1>

<p><a href="https://www.w3schools.com/">Visit W3Schools.com!</a></p>

</body>
</html>""")

    connectionSocket.send(s.encode())
    #connectionSocket.close()
	