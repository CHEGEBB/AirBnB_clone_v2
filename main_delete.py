#!/usr/bin/python3
""" 
This is the main_delete module and it contains the test delete feature.
It tests the delete feature of the FileStorage class.
The delete method deletes an object from the __objects dictionary.
The delete method deletes an object from the file.json file.
"""
from models.state import State
from models.engine.file_storage import FileStorage

fs = FileStorage()

# Print all states
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State object with name "California"
new_state = State(name="California")
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# Print all states after adding "California"
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State object with name "Nevada"
another_state = State(name="Nevada")
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))

# Print all states after adding "Nevada"
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])        

# Delete the new State
fs.delete(new_state)

# Print all states after deletion
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])
