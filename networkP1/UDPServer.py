from socket import*
import time

hostname= gethostname()
port= 5566
server_socket=socket(AF_INET, SOCK_DGRAM)
server_socket.bind((hostname,port))
print("server ready to receive")
start_time=time.time()
counter=0
for counter in range(1000000):
    message, address = server_socket.recvfrom(1024)
    data=message.decode()
    if not data:
        # if data is not received break
        break  
    counter+=1
    print("from connectionSocketected user: " + str(data) + "\n")
#server_socket.close()
end_time=time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time of receiving = {elapsed_time * 1000} ms ")
print("number of messages: " +str(counter))