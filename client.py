import socket
import sqlite3

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

def authenticate(email, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def send_email(client_socket, email, password):
    sender = email
    recipient = input("Enter recipient: ")
    subject = input("Enter subject: ")
    body = input("Enter body: ")

    # Format email data
    email_data = f"{sender}|{recipient}|{subject}|{body}"

    try:
        # Send operation to server
        client_socket.sendall(b"SEND_EMAIL")

        # Send email data to server
        client_socket.sendall(email_data.encode())

        # Receive response from server
        response = client_socket.recv(1024)
        print(response.decode())
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the socket
        client_socket.close()

def read_emails(client_socket, email, password):
    client_socket.sendall(b"READ_EMAILS")

    # Receive response from server
    emails = client_socket.recv(4096).decode()
    print(emails)

def main():
    # Get user input for authentication
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Perform authentication
    if not authenticate(email, password):
        print("Authentication failed. Please check your email and password.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("[*] Connected to server.")

    try:
        # Send authentication data to the server
        auth_data = f"{email}|{password}"
        client_socket.sendall(auth_data.encode())

        # Check if server sent back a response indicating successful authentication
        response = client_socket.recv(1024).decode()
        if response != "Authentication successful. You are logged in.":
            print(response)
            return

        while True:
            print("1. Send Email")
            print("2. Read Emails")
            print("3. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                send_email(client_socket, email, password)
            elif choice == "2":
                read_emails(client_socket, email, password)
            elif choice == "3":
                client_socket.sendall(b"QUIT")
                client_socket.close()
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
