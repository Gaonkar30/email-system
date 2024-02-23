import sqlite3
import ssl
import socket

def create_tables(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (email TEXT PRIMARY KEY, password TEXT, logged_in INTEGER DEFAULT 0)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS emails
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, sender TEXT, recipient TEXT, subject TEXT, body TEXT)''')

def insert_user(cursor, email, password):
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        print(f"User with email '{email}' registered successfully.")
        return True
    except sqlite3.IntegrityError:
        print(f"User with email '{email}' already exists.")
        return False

def display_users(cursor):
    cursor.execute("SELECT email, logged_in FROM users")
    users = cursor.fetchall()
    print("Users:")
    for user in users:
        login_status = "Logged in" if user[1] == 1 else "Logged out"
        print(f"Email: {user[0]}, Status: {login_status}")
def main():
    
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

    
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    
    server_ip = '192.168.143.8'  
    server_port = 5000  

    with socket.create_connection((server_ip, server_port)) as sock:
        with ssl_context.wrap_socket(sock, server_hostname=server_ip) as ssock:
            cursor = ssock.makefile('rwb')
            cursor = sqlite3.connect('users.db').cursor()

            create_tables(cursor)
            display_users(cursor)

   
            email = input("Enter email address: ")
            password = input("Enter password: ")


            insert_user(cursor, email, password)

            cursor.connection.commit()
            cursor.connection.close()

if __name__ == "__main__":
    main()
