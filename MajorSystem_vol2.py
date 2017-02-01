import numpy as np
import pickle

class num():

    def __init__(self, number):
        self.number = number

    def add_entry(self):
        add = input('Input a new number code: ')
        self.entries.append(add)

    def init_number(self):
        self.entries = []

    def print_num(self):
        for code in enumerate(self.entries):
            print(code[0] + 1, '-', code[1])

def save_num(object, file_name):
    file = open(file_name, 'wb')
    pickle.dump(object, file)

def read_num(object):
    try:
        file = open(object, 'rb')
        return pickle.load(file)
    except:
        print('The number doesn\' exist.')



n001 = num('001')
n001.init_number()
while True:
    n001.add_entry()
    n001.print_num()