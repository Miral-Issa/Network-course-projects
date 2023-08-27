from socket import*
import time

hostname= "DESKTOP-K3935TM"
port=5566
client_socket=socket()
client_socket.connect((hostname,port))
message=0
start_time=time.time()
while message != '1000001':
    client_socket.send(str(message).encode())
    temp=int(message) + 1
    message= str(temp)    
end_time=time.time()
elapsed_time = end_time - start_time  # Response time
print(f"Elapsed time of sending = {elapsed_time * 1000} ms ")
client_socket.close()