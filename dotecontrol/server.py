import socket

class MultiplayerServer:
    def __init__(self, ip):
        # Create a TCP server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server_socket.bind((ip, 8000))
        except:
            self.server_socket.bind((ip, 8001))  # Fallback port
        self.server_socket.listen(1)
        print("Server listening on port 8000...")
        # Accept a client connection
        self.client_socket, self.client_address = self.server_socket.accept()
        print(f"Connection from {self.client_address} has been established.")

    def cycle_send(self, data):
        # Send data to the client
        try:
            self.client_socket.send(data.encode())
        except Exception as e:
            print(f"Error sending data: {e}")

    def cycle_recv(self):
        # Receive data from the client
        try:
            return self.client_socket.recv(1024).decode()
        except Exception as e:
            print(f"Error receiving data: {e}")
            return ""

    def exit(self):
        # Close the server sockets
        self.client_socket.close()
        self.server_socket.close()
        print("Server closed.")

class MultiplayerClient:
    def __init__(self, ip):
        # Create a TCP client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((ip, 8000))
            print("Connected to the server.")
        except Exception as e:
            self.client_socket.connect((ip, 8001))  # Fallback port
            print(f"Error connecting to server: {e}")

    def cycle_send(self, data):
        # Send data to the server
        try:
            self.client_socket.send(data.encode())
        except Exception as e:
            print(f"Error sending data: {e}")

    def cycle_recv(self):
        # Receive data from the server
        try:
            return self.client_socket.recv(1024).decode()
        except Exception as e:
            print(f"Error receiving data: {e}")
            return ""

    def exit(self):
        # Close the client socket
        self.client_socket.close()
        print("Client closed.")