import socket

# Define server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))
print("[*] Connected to server.")

# Get user input for authentication
email = input("Enter email: ")
password = input("Enter password: ")

# Send authentication data to server
auth_data = f"{email}|{password}"
client_socket.sendall(auth_data.encode())

# Receive authentication response from server
auth_response = client_socket.recv(1024)
print(auth_response.decode())

# Get user input for the email
if auth_response == b"Authentication successful. You are logged in.":
    sender = input("Enter sender: ")
    recipient = email  # Assuming recipient is the logged-in user
    subject = input("Enter subject: ")
    body = input("Enter body: ")
    
    # Format email data
    email_data = f"{sender}|{recipient}|{subject}|{body}"
    
    # Send email data to server
    client_socket.sendall(email_data.encode())
    
    # Receive response from server
    response = client_socket.recv(1024)
    print(response.decode())

# Close the connection
client_socket.close()
