import sqlite3 as sql
from datetime import date


def get_db(name='main.db'):
    db = sql.connect(name)
    create_table(db)
    return db

def create_table(db):
    cur = db.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS habit (
        name TEXT PRIMARY KEY, 
        description TEXT,
        period TEXT)''')
                
    cur.execute('''CREATE TABLE IF NOT EXISTS tracker (
        date TEXT, 
        habitName TEXT,
        FOREIGN KEY (habitName) REFERENCES habit(name)) ''')
    
    db.commit()

def add_habit(db, name, description, period):
    cur = db.cursor()
    cur.execute('INSERT INTO habit VALUES (?, ?, ?)', (name, description, period))
    db.commit()

def increment_habit(db, name, event_date):
    cur = db.cursor()
    if not event_date:
        event_date = str(date.today())
    cur.execute('INSERT INTO tracker VALUES (?, ?)', (event_date, name))
    db.commit()

def get_habit_data(db, name):
    cur = db.cursor()
    cur.execute('SELECT * FROM tracker WHERE habitName=?', (name,))
    return cur.fetchall()

db = get_db()
create_table(db)
