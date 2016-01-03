__author__ = 'MFlores1'


class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self):



billy_cyrus = Parent('Cyrus', 'blue')
