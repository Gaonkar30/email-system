import socket
import sqlite3

# Define server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a table to store users (if not exists)
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                (email TEXT PRIMARY KEY, password TEXT)''')

# Bind the socket to the server address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

def authenticate(email, password):
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    return user is not None

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

    # Receive data from client (authentication)
    auth_data = client_socket.recv(1024).decode()
    email, password = auth_data.split("|")

    # Authenticate user
    if authenticate(email, password):
        client_socket.sendall(b"Authentication successful. You are logged in.")
        
        # Receive data from client (email)
        email_data = client_socket.recv(1024).decode()
        sender, recipient, subject, body = email_data.split("|")
        
        # Process received data (assuming it's an email)
        # Store the email in the database or send to recipient's inbox (in a real system)
        print(f"Received email from {sender} to {recipient}")
        client_socket.sendall(b"Email received by the server. Thank you!")
    else:
        client_socket.sendall(b"Authentication failed. Please check your email and password.")
    
    # Close the connection
    client_socket.close()
