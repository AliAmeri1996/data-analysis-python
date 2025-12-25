import socket
import sys
import threading

def receive_messages(client_socket):
    """Continuously receive and display messages from server"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
                print("> ", end="", flush=True)  # Reprint the input prompt
        except:
            break

def main():
    if len(sys.argv) != 4:
        print("Usage: python client.py [username] [hostname] [port]")
        sys.exit(1)
    
    username = sys.argv[1]
    hostname = sys.argv[2]
    port = int(sys.argv[3])
    
    # Connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((hostname, port))
    
    # Send username
    client_socket.send(username.encode('utf-8'))
    
    # Receive welcome message
    welcome_message = client_socket.recv(1024).decode('utf-8')
    print(welcome_message)
    
    # Start thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()
    
    # Keep connection open (we'll add sending later)
    while True:
        message = input("> ")
        if message.lower() == "/quit":
            print("Leaving chat...")
            break
        # We'll handle sending messages later
    
    client_socket.close()

if __name__ == "__main__":
    main()