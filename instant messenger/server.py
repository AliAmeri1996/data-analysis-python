import socket
import threading
import sys

# Dictionary to store all connected clients
clients = {}  # Format: {username: client_socket}
clients_lock = threading.Lock()  # To prevent threading issues

def broadcast_message(message, exclude_username=None):
    """Send a message to all connected clients, optionally excluding one"""
    with clients_lock:
        for username, client_socket in clients.items():
            if username != exclude_username:  # Don't send to the excluded user
                try:
                    client_socket.send(message.encode('utf-8'))
                except:
                    pass  # If sending fails, skip this client

def remove_client(username):
    """Remove a client from the dictionary and broadcast they left"""
    with clients_lock:
        if username in clients:
            del clients[username]
    
    # Broadcast to all remaining clients
    leave_message = f"[{username}] has left"
    broadcast_message(leave_message)


def handle_client(client_socket, address):
    username = client_socket.recv(1024).decode('utf-8')
    print(f"{username} connected from {address[0]}:{address[1]}")

     # Add this client to the dictionary, the new client
    with clients_lock:
        clients[username] = client_socket

    welcome_message = f"Welcome to the group chat!{username}"
    client_socket.send(welcome_message.encode('utf-8'))

     # Broadcast to all OTHER clients that this user joined
    join_message = f"[{username}] has joined"
    broadcast_message(join_message, exclude_username=username)


    # Keep connection open (listen for messages/commands)
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:  # Client disconnected
                break
            # We'll handle commands here later
    except:
        pass  # Handle unexpected disconnect
    finally:
        # Client left (gracefully or unexpectedly)
        remove_client(username)
        client_socket.close()

    


def main():
    # Get port from command line
    if len(sys.argv) != 2:
        print("Usage: python server.py [port]")
        sys.exit(1)
    
    port = int(sys.argv[1])

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(50)
    
    print(f"Server listening on port {port}")
    
    # Accept clients in a loop
    while True:
        client_socket, address = server_socket.accept()#This line waits for a client to connect, then creates a connection with them.
        #This line creates a new thread so the server can handle one client without blocking others.
        #target=handle_client → the function that will run in that thread
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()


if __name__ == "__main__":
    main()