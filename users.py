import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a table to store users (if not exists)
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                (email TEXT PRIMARY KEY, password TEXT)''')

# Insert two random user entries
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ('user1@example.com', 'password1'))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ('user2@example.com', 'password2'))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database 'users.db' with 2 random entries created successfully.")
