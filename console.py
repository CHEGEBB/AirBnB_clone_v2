#!/usr/bin/python3
"""This module entails the HBNB console that is used to manage the AirBnB"""

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This class is the console for the AirBnB project"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance with given parameters"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return

        # Extracting key-value pairs from arguments
        kwargs = {}
        for arg in args[1:]:
            if "=" not in arg:
                print("** invalid syntax: {} **".format(arg))
                return
            key, value = arg.split("=")
            key = key.strip()
            value = value.strip()

            # Handling value types
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
                value = value.replace('_', ' ')
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    print("** invalid value for float type: {} **".format(value))
                    return
            else:
                try:
                    value = int(value)
                except ValueError:
                    print("** invalid value for integer type: {} **".format(value))
                    return

            kwargs[key] = value

        # Creating a new instance and setting attributes
        new_instance = eval(class_name)(**kwargs)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel", "User", "State", "City", "Place",
                               "Amenity", "Review"]:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel", "User", "State", "City", "Place",
                               "Amenity", "Review"]:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the
        class name"""
        args = arg.split()
        if not arg:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in ["BaseModel", "User", "State", "City", "Place",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items()
                   if args[0] in key])
            
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City", "Place",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        count = 0
        for key in storage.all():
            if arg in key:
                count += 1
        print(count)

    def default(self, arg):
        """Default method"""
        args = arg.split(".")
        if len(args) > 1:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.do_count(args[0])
            elif args[1][0:4] == "show":
                self.do_show(args[0] + " " + args[1][6:-2])
            elif args[1][0:7] == "destroy":
                self.do_destroy(args[0] + " " + args[1][9:-2])
            elif args[1][0:6] == "update":
                args2 = args[1][8:-2].split(", ")
                self.do_update(args[0] + " " + args2[0][1:-1] + " " +
                               args2[1][1:-1] + " " + args2[2][1:-1])
            else:
                print("*** Unknown syntax: {}".format(arg))
        else:
            print("*** Unknown syntax: {}".format(arg))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
