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
            print("** class doesn't exist **")

    def do_update(self, arg):
        """This updates an instance based on the class and id
        It is a command to update an instance
        The command syntax is update <Class name> <id> <attribute name> <attribute value>
        It updates an instance based on the class
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(models.storage.all()[key], args[2], args[3])
                            models.storage.all()[key].save()
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
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """This prints all instances of a class
        It is a command to print all instances of a class
        The command syntax is all <Class name>
        It prints all instances of a class
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print([str(value) for value in models.storage.all().values()])
        elif args[0] in classes:
            print([str(value) for key, value in models.storage.all().items()
                   if args[0] in key])
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """This counts the number of instances of a class
        It is a command to count the number of instances of a class
        The command syntax is count <Class name>
        It counts the number of instances of a class
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print(len(models.storage.all()))
        elif args[0] in classes:
            print(len([value for key, value in models.storage.all().items()
                       if args[0] in key]))
        else:
            print("** class doesn't exist **")

    def do_help(self, arg):
        """This prints the help message
        It is a command to print the help message
        The command syntax is help <command>
        It prints the help message
        """
        cmd.Cmd.do_help(self, arg)

    def default(self, arg):
        """This is the default method for the command interpreter
        It is a method that is called when an invalid command is entered
        It prints an error message
        """
        print("*** Unknown syntax: {}".format(arg))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
