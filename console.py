#!/usr/bin/python3

"""This module contains the console 
It is the entry point of the command interpreter
The console is a command interpreter to manage the HBnB data
It is the class HBNBCommand
It is the command interpreter of the console
It is the entry point of the command interpreter
"""

from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel
from models.city import City
import cmd
import shlex
import models
from models.amenity import Amenity
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """This class is the console of the HBnB project
    It is the command interpreter of the console
    It is the entry point of the command interpreter
    """
    prompt = '(hbnb) '
    def _key_value_parser(self, args):
        """This creates a dictionary from a list of strings
        It is a helper function for the create command
        The dictionary is created from a list of strings
        """
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_EOF(self, arg):
        """This exits the console
        It is a command to exit the program
        """
        return True

    def emptyline(self):
        """This overwrites the emptyline method
        It is a method that does nothing when an empty line is entered
        to prevent the default behavior of repeating the last command
        """
        return False

    def do_quit(self, arg):
        """This quits the console and exits the program
        It is a command to exit the program
        """
        return True

    def do_create(self, arg):
        """This creates an object with given parameters
        It is a command to create an object
        The command syntax is create <Class name> <param 1> <param 2> <param 3>...
        It creates an object with the given parameters
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """This prints an instance as a string based on the class and id
        It is a command to print an instance as a string
        The command syntax is show <Class name> <id>
        It prints an instance as a string based on the class and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


    def do_update(self, arg):
        """This updates an instance based on the class and id
        It is a command to update an instance
        The command syntax is update <Class name> <id> <attribute name> <attribute value>
        It updates an instance based on the class and id
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
    def do_destroy(self, arg):
        """This deletes an instance based on the class and id
        It is a command to delete an instance
        The command syntax is destroy <Class name> <id>
        It deletes an instance based on the class and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """This prints string representations of instances
        It is a command to print string representations of instances
        The command syntax is all <Class name>
        It prints string representations of instances
        it prints all instances of a class if a class name is given
        """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
