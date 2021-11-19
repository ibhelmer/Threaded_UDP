# Sample UDP Client - Multi threaded client !!!!

# imports
import socket
import threading

msgFromClient = "Hello Rover via UDP"
bytesToSend = str.encode(msgFromClient)

bufferSize = 1024

# Server IP address and Port number, change the IP address and port so it is acording to the servers

serverAddressPort = ("127.0.0.1", 7913)

# Connect2Server forms the thread - for each connection made to the server
def Connect2Server():
    # Create a socket instance - A datagram socket
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Send message to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    # Receive message from the server
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Rover {}".format(msgFromServer[0])
    print(msg)

# Example show that server can handle many connections  (ThreadCount is the number of connections)
# The following should be rewritten to the need of the application
print("Client - Main thread started")
ThreadList = []
ThreadCount = 20

for index in range(ThreadCount):
    ThreadInstance = threading.Thread(target=Connect2Server())
    ThreadList.append(ThreadInstance)
    ThreadInstance.start()

# Here we just wait to all connection threads are complete
for index in range(ThreadCount):
    ThreadList[index].join()