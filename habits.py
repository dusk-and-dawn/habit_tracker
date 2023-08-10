

class habit: 
    def __init__(self, name:str, description:str, period='daily'):
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


