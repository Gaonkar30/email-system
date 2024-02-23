
import socket
import ssl

SERVER_HOST = '192.168.143.8'
SERVER_PORT = 5000
CERTFILE = 'C:\Users\Akash G Gaonkar\Desktop\email\Email-Systems\cert.pem'
KEYFILE = 'C:\Users\Akash G Gaonkar\Desktop\email\Email-Systems\key.pem'

def main():
    try:
        
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        with socket.create_connection((SERVER_HOST, SERVER_PORT)) as client_socket:
            with context.wrap_socket(client_socket, server_hostname=SERVER_HOST) as ssl_socket:
                print("[*] Connected to server.")

                email = input("Enter email: ")
                password = input("Enter password: ")

                auth_data = f"{email}|{password}"
                ssl_socket.sendall(auth_data.encode())

                response = ssl_socket.recv(1024).decode()
                print(response)

                if response != "Authentication successful. You are logged in.":
                    return

                while True:
                    print_menu()
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        send_email(ssl_socket)
                    elif choice == "2":
                        read_emails(ssl_socket)
                    elif choice == "3":
                        ssl_socket.sendall(b"QUIT")
                        return
                    else:
                        print("Invalid choice. Please try again.")

    except Exception as e:
        print("An error occurred:", e)

def print_menu():
    print("1. Send Email")
    print("2. Read Emails")
    print("3. Quit")

def send_email(ssl_socket):
    sender = input("Enter sender's email: ")
    recipient = input("Enter recipient's email: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    email_data = f"{sender}|{recipient}|{subject}|{body}"
    ssl_socket.sendall(b"SEND_EMAIL")
    ssl_socket.sendall(email_data.encode())

    response = ssl_socket.recv(1024).decode()
    print(response)

def read_emails(ssl_socket):
    ssl_socket.sendall(b"READ_EMAILS")
    response = ssl_socket.recv(1024).decode()
    print(response)

    email_list = ssl_socket.recv(4096).decode()
    print(email_list)

if __name__ == "__main__":
    main()
