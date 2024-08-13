import sqlite3

def init_db():
    conn = sqlite3.connect('daily_word.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS daily_words (
        word_id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        meaning TEXT NOT NULL,
        example TEXT NOT NULL,
        sent INTEGER DEFAULT 0)''')

    c.execute('''CREATE TABLE IF NOT EXISTS emails (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE)''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
