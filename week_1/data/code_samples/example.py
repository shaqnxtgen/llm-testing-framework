import sqlite3
import json
from typing import Dict, Any

def save_user_data(user_input: Dict[str, Any]) -> bool:
    """Save user data to database"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY, username TEXT, password TEXT, data TEXT)
    ''')
    
    # Insert user data - potential SQL injection vulnerability
    query = f"INSERT INTO users (username, password, data) VALUES ('{user_input['username']}', '{user_input['password']}', '{json.dumps(user_input)}')"
    cursor.execute(query)
    
    conn.commit()
    return True

def get_user_data(username: str) -> Dict[str, Any]:
    """Retrieve user data from database"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Fetch user data - potential SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    if result:
        return json.loads(result[3])
    return {} 