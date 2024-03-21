#!/usr/bin/python3

"""This is the console module
It is the entry point of the command interpreter
The console is a command interpreter to manage the HBnB data
"""

import json
import shlex
from datetime import datetime
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Place": Place, "Amenity": Amenity, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """This is the class HBNBCommand
    It is the command interpreter of the console
    It is the entry point of the command interpreter
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of a specified class with given parameters,
        saves it (to the JSON file), and prints the id"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        kwargs = {}
        for arg in args[1:]:
            try:
                key, value = arg.split('=')
                # Remove double quotes from value if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                # Replace underscores with spaces in the key
                key = key.replace('_', ' ')
                # Try to convert the value to int or float if possible
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                # Skip invalid arguments
                continue
            kwargs[key] = value
        instance = classes[class_name](**kwargs)
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = line.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 3:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        args = line.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 3:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = line.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in storage.all().items() if key.startswith(class_name + '.')])

    def do_update(self, line):
        """Updates an instance based on 
        the class name and id by adding or updating attribute
        (save the change into the JSON file)"""
        args = shlex.split(line)
        if len(args) < 3:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 4:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        setattr(all_objs[key], args[2], args[3])
        all_objs[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
