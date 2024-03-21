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

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file)"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key in all_objs:
                setattr(all_objs[key], args[2], args[3])
                all_objs[key].save()
            else:
                print("** no instance found **")

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        print("Received command:", line)
        args = line.split(".")
        print("Split arguments:", args)
        if len(args) == 2:
            if args[0] in classes:
                if args[1] == "all()":
                    print("Executing do_all with class:", args[0])
                    self.do_all(args[0])
                elif args[1] == "count()":
                    print("Executing count() with class:", args[0])
                    count = 0
                    all_objs = storage.all()
                    for obj in all_objs:
                        if obj.split(".")[0] == args[0]:
                            count += 1
                    print(count)
                elif args[1].startswith("show(") and args[1].endswith(")"):
                    id = args[1][args[1].find("(")+1:args[1].find(")")]
                    print("Executing show() with class:", args[0], "and id:", id)
                    self.do_show(args[0] + " " + id)
                elif args[1].startswith("destroy(") and args[1].endswith(")"):
                    id = args[1][args[1].find("(")+1:args[1].find(")")]
                    print("Executing destroy() with class:", args[0], "and id:", id)
                    self.do_destroy(args[0] + " " + id)
                elif args[1].startswith("update(") and args[1].endswith(")"):
                    id = args[1][args[1].find("(")+1:args[1].find(")")]
                    args = args[1][args[1].find(")")+2:]
                    args = args.replace(",", "")
                    print("Executing update() with class:", args[0], "and id:", id, "and args:", args)
                    self.do_update(args[0] + " " + id + " " + args)
                else:
                    print("*** Unknown syntax: {}".format(line))
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
