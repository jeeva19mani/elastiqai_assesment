import datetime


class FootprintHelper:

    def __init__(self):
        self.now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def info(self, message):
        print(f'\n{self.now}--INFO-----\t{message}', end="\n")

    def step(self, message):
        print(f'\n{self.now}--STEP-----\t{message}', end="\n")