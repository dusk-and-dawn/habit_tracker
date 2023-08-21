from db import add_habit, increment_habit

class Habit: 
    def __init__(self, name:str, description:str, period:str):
        self.name = name 
        self.description = description
        self.period = period 
        self.count = 0

    def increment(self):
        self.count += 1 

    def reset(self):
        self.count = 0

    def __str__(self):
        return f'{self.name}: {self.count}'

    def store(self, db): 
        add_habit(db, self.name, self.description, self.period)

    def add_event(self, db, date:str=None):
        increment_habit(db, self.name, date)

