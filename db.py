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
    connect = get_db()
    cur = db.cursor()
    cur.execute('INSERT INTO habit VALUES (?, ?, ?)', (name, description, period))
    connect.commit()

def increment_habit(db, name, event_date):
    connect = get_db()
    cur = db.cursor()
    if not event_date:
        event_date = date.today()
    cur.execute('INSERT INTO tracker VALUES (?, ?)', (event_date, name))
    connect.commit()

def get_habit_data(db, name):
    connect = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM habit WHERE name=?", (name,))
    return cur.fetchall()

db = get_db()
create_table(db)