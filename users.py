import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a table to store users (if not exists)
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                (email TEXT PRIMARY KEY, password TEXT, logged_in INTEGER DEFAULT 0)''')

# Insert two random user entries
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ('user1@example.com', 'password1'))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ('user2@example.com', 'password2'))

# Commit changes
conn.commit()

def display_users():
    cursor.execute("SELECT email, logged_in FROM users")
    users = cursor.fetchall()
    print("Users:")
    for user in users:
        login_status = "Logged in" if user[1] == 1 else "Logged out"
        print(f"Email: {user[0]}, Status: {login_status}")

display_users()

# Close the connection
conn.close()

print("Database 'users.db' with 2 random entries created successfully.")
