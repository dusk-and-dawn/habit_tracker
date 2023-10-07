from db import get_habit_data

def count_everything(db, habit):
    cur = db.cursor()
    cur.execute('SELECT count FROM habit WHERE name = ?', (habit,))
    result = cur.fetchone()
    return result[0] if result else 0

def print_database_contents(db):
    cur = db.cursor()

    # Retrieve and print data from the habit table
    cur.execute("SELECT * FROM habit")
    habits = cur.fetchall()
    print("Habit Table Contents:")
    for habit in habits:
        print("Name:", habit[0])
        print("Description:", habit[1])
        print("Period:", habit[2])
        print()

    # Retrieve and print data from the tracker table
    cur.execute("SELECT * FROM tracker")
    tracker_data = cur.fetchall()
    print("Tracker Table Contents:")
    for data in tracker_data:
        print("Date:", data[0])
        print("Habit Name:", data[1])
        print()

    #db.close()  # Close the database connection