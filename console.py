#!/usr/bin/python3

"""This module is the console of the AirBnB clone project"""

import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This class is the console of the AirBnB clone project"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif line not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):

        """Prints all string representation of all instances based or not on the
        class name"""

        args = line.split()
        if not line:
            print([str(value) for value in models.storage.all().values()])
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in models.storage.all().items()
                   if key.split('.')[0] == args[0]])
            
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in models.storage.all():
                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.all()[key].save()
            else:
                print("** no instance found **")

    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for key in models.storage.all():
                if key.split('.')[0] == args[0]:
                    count += 1
            print(count)

    def default(self, line):
        """Default method"""
        args = line.split('.')
        if len(args) == 2:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.do_count(args[0])
            elif args[1][0:4] == "show":
                self.do_show(args[0] + " " + args[1][6:-2])
            elif args[1][0:7] == "destroy":
                self.do_destroy(args[0] + " " + args[1][9:-2])
            elif args[1][0:6] == "update":
                args2 = args[1][7:-2].split(', ')
                self.do_update(args[0] + " " + args2[0][1:-1] + " " + args2[1][1:-1] + " " + args2[2][1:-1])
        else:
            print("*** Unknown syntax: " + line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    