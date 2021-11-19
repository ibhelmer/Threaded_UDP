# Sample UDP Server - Multi threaded

# Import the necessary python modules
import socketserver
import threading

# Change this to the correct ip address for server
ServerAddress = ("127.0.0.1", 7913)

# Subclass the DatagramRequestHandler
class MyUDPRequestHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        # Receive and print the datagram received from client
        print("Recieved one request from {}".format(self.client_address[0]))
        datagram = self.rfile.readline().strip()
        print("Datagram Recieved from client is:".format(datagram))
        print(datagram)
        # Print the name of the thread
        print("Thread Name:{}".format(threading.current_thread().name))
        # Send a message to the client
        self.wfile.write("Message from Rover! Hello Client".encode())

# Create a Server Instance
UDPServerObject = socketserver.ThreadingUDPServer(ServerAddress, MyUDPRequestHandler)

# Make the server wait forever serving connections
UDPServerObject.serve_forever()