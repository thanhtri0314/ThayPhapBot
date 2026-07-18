import sqlite3

def init_db():
    conn = sqlite3.connect("thayphap.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS players 
                      (user_id INTEGER PRIMARY KEY, linh_luc INTEGER)''')
    conn.commit()
    conn.close()
