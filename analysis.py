from db import get_habit_data

def count_everything(db, habit):
    data = get_habit_data(db, habit)
    return len(data)