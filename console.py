#!/usr/bin/python3
"""This module contains the console for the HBnB project
It is the console for the HBnB project
It is a command interpreter for the HBnB project
It does the following:
    create: creates a new instance of BaseModel, saves it to JSON file, and prints the id
    show: prints the string representation of an instance based on the class name and id
    destroy: deletes an instance based on the class name and id
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import cmd
import shlex

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ This is the HBNBCommand class, a subclass
    of cmd.Cmd
    It is the console for the HBnB project
    It is a command interpreter for the HBnB project
    """
    prompt = '(hbnb) '

    def _key_value_parser(self, args):
        """This creates a dictionary from a list of strings
        It creates a dictionary from a list of strings
        A dictionary is created from a list of strings
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
        After the user types EOF, the console exits
        The console exits after the user types EOF
        """
        return True

    def emptyline(self):
        """This overwrites the emptyline method
        This overwrites the emptyline method
        The emptyline method is overwritten"""
        return False

    def do_quit(self, arg):
        """this quits the console
        after the user types quit, the console quits
        the console quits after the user types quit"""

        return True

    def do_create(self, arg):
        """Creates a new instance of a class, saves it to JSON file, and prints the id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        class_obj = classes[class_name]
        if len(args) == 1:
            # No attributes provided, create an instance without any additional arguments
            instance = class_obj()
        else:
            # Attributes provided, parse them and create an instance
            new_dict = self._key_value_parser(args[1:])
            instance = class_obj(**new_dict)
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """This prints an instance as a string based on the class and id
        The show method prints an instance as a string
        It is based on the class and id of the instance
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

    def do_destroy(self, arg):
        """this deletes an instance based on the class and id
        The destroy method deletes an instance
        It is based on the class and id of the instance
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
        """Prints string representations of instances
        The all method prints string representations of instances
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

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        The update method updates an instance
        It is based on the class name and id of the instance
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
