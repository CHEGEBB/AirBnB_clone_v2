#!/usr/bin/python3

"""This is the console module
It is the entry point of the command interpreter
The console is a command interpreter to manage the HBnB data
"""

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from datetime import datetime
import cmd
import shlex
import json
import models

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
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        args = line.split()
        all_objs = storage.all()
        if len(args) == 0:
            print([str(all_objs[obj]) for obj in all_objs])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            print([str(all_objs[obj]) for obj in all_objs if obj.split(".")[0] == args[0]])
    
    def do_update(self, arg):
        """This function updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file)
        If the instance doesn't exist, prints ** no instance found **
        If the attribute name doesn't exist, prints ** no instance found **
        """
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
