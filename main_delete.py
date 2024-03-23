#!/usr/bin/python3
""" This is the main_delete module and it contains the test delete feature
It tests the delete feature of the FileStorage class
The delete method deletes an object from the __objects dictionary
The delete method deletes an object from the file.json file
"""
from models.state import State
from models.engine.file_storage import FileStorage


fs = FileStorage()

all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

"""Create a new State
The new method sets in __objects the obj with key <obj class name>.id
"""
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

"""All States"""
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

"""Create another State
The new method sets in __objects the obj with key <obj class name>.id
"""
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))

"""All States"""
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])        

"""Delete the new State
The delete method deletes an object from the __objects dictionary
"""
fs.delete(new_state)

"""All States
The delete method deletes an object from the file.json file
"""
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])
