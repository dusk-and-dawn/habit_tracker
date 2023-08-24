from habits import Habit
from db import get_db, add_habit, increment_habit
import os

class TestHabit: 

    def setup_method(self):
        self.db = get_db('test.db')

        add_habit(self.db, 'legend says this is a test_habit','Jo this be a fake habit')
        increment_habit(self.db, 'legend says this is a test_habit', '2023-01-13')
        increment_habit(self.db, 'legend says this is a test_habit', '2023-01-14')

        increment_habit(self.db, 'legend says this is a test_habit', '2023-01-15')
        increment_habit(self.db, 'legend says this is a test_habit', '2023-01-16')

    def test_habit(self):
        habit = Habit('test_habit_da_legend', 'test_description_of_a_legend')

        habit.increment()
        habit.reset()
        habit.increment()

    def teardown_method(self):
        os.remove('test.db')