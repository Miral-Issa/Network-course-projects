from socket import*
import time

hostname= gethostname()
port= 5566
server_socket=socket()
server_socket.bind((hostname,port))
server_socket.listen(2)
connectionSocket, address = server_socket.accept()
print("connectionSocketection from: " + str(address))
start_time=time.time()
counter=0
while True:
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = connectionSocket.recv(1024).decode()
    if not data:
        # if data is not received break
        break  
    counter+=1
    print("from connectionSocketected user: " + str(data) + "\n")
connectionSocket.close()
end_time=time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time of receiving = {elapsed_time * 1000} ms ")
print("number of messages: " +str(counter))