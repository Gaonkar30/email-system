# Email System with SSL Implementation

This is a basic implementation of an email system using Python with SSL encryption. The system consists of three main components: `client.py`, `server.py`, and `users.py`. Additionally, it requires SSL certificates (`cert.pem` and `key.pem`) for encryption and a database file (`users.db`) to store user information.

## Components:

### 1. `client.py`:
This file contains the implementation of the client-side of the email system. It establishes a secure connection with the server using SSL and allows users to send and receive emails.

### 2. `server.py`:
The `server.py` file implements the server-side functionality of the email system. It listens for incoming connections from clients, handles incoming emails, and delivers them to the appropriate recipients.

### 3. `users.py`:
This file provides user authentication functionality. It handles user registration, login, and authentication. User information is stored and managed in the `users.db` database file.

### 4. `cert.pem` and `key.pem`:
These files contain SSL certificates and private keys respectively, necessary for establishing secure connections between the client and server.

### 5. `users.db`:
This SQLite database file stores user information such as usernames, passwords, and email addresses.

## Usage:

1. Ensure Python is installed on your system.
2. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
3. Run the server using the following command:
   ```
   python server.py
   ```
4. Run the client using the following command:
   ```
   python client.py
   ```
5. Follow the prompts on the client-side to register/login and send/receive emails.

## Configuration:

- Modify `config.py` to adjust server settings such as host, port, etc.
- Ensure `cert.pem` and `key.pem` are properly generated and configured for SSL encryption.

## Dependencies:
- Python (>=3.6)
- Additional dependencies are listed in `requirements.txt` and can be installed via pip.

## Notes:

- This is a basic implementation and may lack features present in commercial email systems.
- Security considerations should be taken into account when deploying in a production environment.
- Always handle sensitive information such as passwords and private keys securely.

## License:
This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per the terms of the license.
