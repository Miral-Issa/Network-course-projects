from socket import*

#server_name = gethostname()
server_port = 7788
server_socket=socket(AF_INET, SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)
print("The server is ready to receive")

while True:
    connection_socket, address=server_socket.accept()
    ip=address[0]
    port=address[1]
    #print("connectionSocketection from: " + str(address))
    message=connection_socket.recv(2048).decode()
    requered=""
    try:#sometime an errore:index out of range accured so I put the split in a try 
        requered=message.split(' ')[1]
        print("what the client requered: " + requered)
        connection_socket.send(f"HTTP/1.1 200 OK\r\n".encode())
    except Exception as x:
        connection_socket.send("try again please".encode())
        

    send_back="received\n"
    #connection_socket.send(send_back.encode())
    
    try:
        if requered == '/' or requered == '/main_en.html' or requered == '/en':
            send_back="send back main_en.html\n"
            #connection_socket.send(send_back.encode())
            print(send_back)
            send_backf=open(r"C:\Users\Microsoft\Desktop\networkP1\index.html","rb")
            ST = send_backf.read()
            send_backf.close()
            connection_socket.send(f"\r\n".encode())
            connection_socket.send(ST) 
            
        elif requered == '/style.css':
            send_backf=open(r"C:\Users\Microsoft\Desktop\networkP1\style.css","rb")
            ST = send_backf.read()
            #connection_socket.senf(f"\r\n".encode())
            connection_socket.send(ST)
            print("send style.css file too")
            
        elif requered == '/10.jpg':
            #connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
            #connection_socket.send('Content-Type: image/jpeg \r\n'.encode())
            connection_socket.send('\r\n'.encode())
            imagef=open(r"C:\Users\Microsoft\Desktop\networkP1\10.jpg","rb")
            image_data=imagef.read(2048)
            while image_data:
                connection_socket.send(image_data)
                image_data=imagef.read(2048)
                
        elif requered == '/2.png':
            #connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
            #connection_socket.send('Content-Type: image/png \r\n'.encode())
            connection_socket.send('\r\n'.encode())
            imagef=open(r"C:\Users\Microsoft\Desktop\networkP1\2.png","rb")
            connection_socket.send(imagef.read())
        
        elif requered == '/3.jpg':
            #connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
            #connection_socket.send('Content-Type: image/jpeg \r\n'.encode())
            connection_socket.send('\r\n'.encode())
            imagef=open(r"C:\Users\Microsoft\Desktop\networkP1\3.jpg","rb")
            image_data=imagef.read(2048)
            while image_data:
                connection_socket.send(image_data)
                image_data=imagef.read(2048)
        elif requered == '/text2.css':
            send_backf=open(r"C:\Users\Microsoft\Desktop\networkP1\text2.css","rb")
            ST = send_backf.read()
            #connection_socket.senf(f"\r\n".encode())
            connection_socket.send(ST)
            print("send text2.css file too")
        
            
        elif requered == '/ar':
            send_back = "send back main_ar.html\n"
            #connection_socket.send(send_back.encode())
            print(send_back)
            send_backf=open(r"C:\Users\Microsoft\Desktop\networkP1\index2.html","rb")
            ST = send_backf.read()
            send_backf.close()
            connection_socket.send(f"\r\n".encode())
            connection_socket.send(ST) 
        
        elif requered.endswith('.html') :
            send_back= "send IDs html file\n"
            #connection_socket.send(send_back.encode())
            print(send_back)
            send_backf=open(r"C:\Users\Microsoft\Desktop\networkP1\text.html","rb")
            ST = send_backf.read()
            send_backf.close()
            connection_socket.send(f"\r\n".encode())
            connection_socket.send(ST) 
        
        elif requered.endswith('.css'):
            send_back="send network css file\n"
            #connection_socket.send(send_back.encode())
            print(send_back)
            send_backf=open(r"C:\Users\Microsoft\Desktop\networkP1\linktest2.html","rb")
            ST = send_backf.read()
            send_backf.close()
            connection_socket.send(f"\r\n".encode())
            connection_socket.send(ST) 
        
        elif requered == '/birzeit.png':
            #send_back = "send back birziet image\n"
            #connection_socket.send(send_back.encode)
            #print(send_back)
            connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
            connection_socket.send('Content-Type: image/png \r\n'.encode())
            connection_socket.send('\r\n'.encode())
            imagef=open(r"C:\Users\Microsoft\Desktop\networkP1\birzeit.png","rb")
            connection_socket.send(imagef.read())
        
        elif requered == '/image.jpg':
            #send_back = "send back a jpg image\n"
            #connection_socket.send(send_back.encode())
            #print(send_back)
            connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
            connection_socket.send('Content-Type: image/jpeg \r\n'.encode())
            connection_socket.send('\r\n'.encode())
            imagef=open(r"C:\Users\Microsoft\Desktop\networkP1\My project(1).jpg","rb")
            image_data=imagef.read(2048)
            while image_data:
                connection_socket.send(image_data)
                image_data=imagef.read(2048)
            
        elif requered == "/go" or requered == "/so" or requered == "/bzu":
            if requered == "/go":
                s="location: https://www.google.com\r\n"
                connection_socket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
                connection_socket.send('\r\n'.encode())
   
                connection_socket.send(s.encode())
                print(s);
                connection_socket.send('\r\n'.encode())
            elif requered == "/so":
                connection_socket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
                connection_socket.send('\r\n'.encode())
                s=("""
                <html>
                <body>
                <p><a href="https://stackoverflow.com">Visit stackoverflow.com!</a></p>
                </body>
                </html>""")
                connection_socket.send(s.encode())
            elif requered == "/bzu":
                connection_socket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
                connection_socket.send('\r\n'.encode())
                s=("""
                <html>
                <body>
                <p><a href="https://www.birzeit.edu/en">Visit ritaj.edu!</a></p>
                </body>
                </html>""")
                connection_socket.send(s.encode())
                
        
        else:
            
            print("error")

        
    except Exception as e:
        pass
        connection_socket.send('HTTP/1.1 404 Not Found\n\n'.encode())
        #connection_socket.send('Content-Type: text/html \r\n'.encode())
        #connection_socket.send("\r\n".encode())
        ST = ('<!DOCTYPE html>'
'<html lang="en">'
'<head>'
    '<meta charset="UTF-8">'
    '<meta http-equiv="X-UA-Compatible" content="IE=edge">'
   ' <meta name="viewport" content="width=device-width, initial-scale=1.0">'
   ' <title>Erorr</title>'
   
'</head>'
'<body>'
    '<center><h1>Error 404: Not found</h1>'

        '<font color="#FF0000"> <center><b>The file is not found </b> </center> </font>'

    '<hr><p style= "font-weight: bold;">Miral issa- 1200527</p><p style= '
        '"font-weight: bold;">Rawa Hajaj - 1191497</p><hr><h2>IP:' + str(
            ip) + ', Port: ' + str(port) +  '</h2></center></body></html>'') ' 

         
    
'</body>'
'</html>')
        connection_socket.send(ST.encode())
        print("error")
    connection_socket.close()