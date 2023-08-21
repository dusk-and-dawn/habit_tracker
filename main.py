from db import *
from habits import Habit
from analysis import *
import questionary

def cli():
    db = get_db() 
    questionary.confirm('Welcome to David\'s Habit Tracker, are you ready to proceed?').ask()
    stop = False

    while not stop:
        choice = questionary.select('How can I be helpful?', 
        choices=['create', 'record habit', 'analyse', 'show me all you\'ve got', 'exit']).ask()

        if choice == 'create':
            name = questionary.text('what new habit would you like to create?').ask()
            description = questionary.text('please do describe your new habit: ').ask()
            period = questionary.text('please choose between daily and weekly').ask()
            habit = Habit(name, description, period)
            habit.store(db)
        elif choice == 'record habit':
            pick_habit = questionary.text('please do choose one of the following habits to record:').ask()
            description2 = '\'sup this is filler text'
            period = 'more filler text'
            habit = Habit(pick_habit, description2, period)
            habit.increment()
            habit.add_event(db)
        elif choice == 'analyse': 
            if 'name' not in locals():
                name = questionary.text('Enter the name of the habit you want to analyze: ').ask()
            count = count_everything(db, name)
            print(f'{name} has been recorded {count} times.')
        elif choice == 'show me all you\'ve got':
            print_database_contents(db)
        else: 
            print('I really hope I did a good job, thank you for using my functionalities.')
            stop = True

if __name__ == '__main__':
    cli()




