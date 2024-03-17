#!/usr/bin/env python
"""This module defines the HBNBCommand class"""

import cmd
import re
import sys
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""

    # determine prompt for interactive and non-interactive mode
    prompt = "(hbnb) " if sys.__stdin__.isatty() else ""

    # preloop for non-interactive mode
    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ')

    # postcmd for non-interactive mode
    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ')
        return stop

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()  # Print a new line before exiting
        return True

    # aliasing
    do_EOF = do_quit

    # help quit
    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass

    # help emptyline
    # def help_emptyline(self):
    #     print("Empty line + ENTER shouldn’t execute anything\n")

    def do_create(self, arg):
        """Creates a new instance of a class, saves it (to the JSON file)
        and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "User",
                         "Amenity", "City", "Place", "Review", "State"]:
            print("** class doesn't exist **")
        else:
            my_classes = {"BaseModel": BaseModel, "User": User,
                          "Amenity": Amenity, "City": City,
                          "Place": Place, "Review": Review, "State": State}
            try:
                new_instance = my_classes[arg]()
                storage.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    # help create
    def help_create(self):
        print("Creates a new instance of a class, saves it (to the JSON "
              "file) and prints the id\n")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel", "User",
                               "Amenity", "City", "Place", "Review", "State"]:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif args[0] + "." + args[1] not in storage.all():
                print("** no instance found **")
            else:
                try:
                    instance_id = args[0] + "." + args[1]
                    if instance_id not in storage.all():
                        print("** no instance found **")
                        return
                    print(storage.all()[instance_id])
                except NameError:
                    print("** no instance found **")

    # help show
    def help_show(self):
        print("Prints the string representation of an instance based on the "
              "class name and id\n")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel", "User",
                               "Amenity", "City", "Place", "Review", "State"]:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                try:
                    instance_id = args[0] + "." + args[1]
                    if instance_id not in storage.all():
                        print("** no instance found **")
                        return

                    del storage.all()[instance_id]
                    storage.save()
                except NameError:
                    print("** no instance found **")

    # help destroy
    def help_destroy(self):
        print("Deletes an instance based on the class name and id\n")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in ["BaseModel", "User",
                               "Amenity", "City", "Place", "Review", "State"]:
                print("** class doesn't exist **")
            else:
                try:
                    my_list = []
                    new_instance = storage.all()
                    for k, v in new_instance.items():
                        my_list.append(str(storage.all()[k]))
                    print(my_list)
                except NameError:
                    print("** no instance found **")

    # help all
    def help_all(self):
        print("Prints all string representation of all instances based or not "
              "on the class name\n")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute"""
        if not arg:
            print("** class name missing **")
        else:
            arg_s = arg.split()
            args = []
            for item in arg_s:
                if isinstance(item, str):
                    cleaned_item = re.sub(r'[^a-zA-Z0-9\s@_-]', '', item)
                    args.append(cleaned_item)
                else:
                    args.append(item)

            if args[0] not in ["BaseModel", "User",
                               "Amenity", "City", "Place", "Review", "State"]:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                try:
                    instance_id = args[0] + "." + args[1]
                    if instance_id not in storage.all():
                        print("** no instance found **")
                        return

                    updated_instance = storage.all()[instance_id]
                    setattr(updated_instance, args[2], args[3])
                    storage.save()
                except NameError:
                    print("** no instance found **")

    # help update
    def help_update(self):
        print("Updates an instance based on the class name and id by adding "
              "or updating attribute\n")

    def default(self, arg):
        """Method called on an input line when the command prefix is not
        recognized"""
        args = arg.split(".")
        if len(args) == 2:
            if args[0] not in ["BaseModel", "User",
                               "Amenity", "City", "Place", "Review", "State"]:
                print("** class doesn't exist **")
                return
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                count = 0
                for k, v in storage.all().items():
                    if args[0] in k:
                        count += 1
                print(count)
            elif "show(" in args[1]:
                match = re.search(r'\((.*?)\)', args[1])
                if match:
                    instance_id = match.group(1).strip('\'"')
                    if args[0] not in ["BaseModel", "User", "Amenity",
                                       "City", "Place", "Review", "State"]:
                        print("** class doesn't exist **")
                    else:
                        self.do_show(args[0] + " " + instance_id)
                else:
                    print("** invalid command format **")

            elif "destroy(" in args[1]:
                match = re.search(r'\((.*?)\)', args[1])
                if match:
                    instance_id = match.group(1).strip('\'"')
                    if args[0] not in ["BaseModel", "User", "Amenity", "City",
                                       "Place", "Review", "State"]:
                        print("** class doesn't exist **")
                    else:
                        self.do_destroy(args[0] + " " + instance_id)
                else:
                    print("** invalid command format **")

            elif "update(" in args[1]:
                if "{" in args[1]:
                    new_instance = re.search(r'\((.*?)\)', args[1]).group(1)

                    data = [
                        new_instance
                    ]

                    cleaned_data = []

                    for item in data:
                        if isinstance(item, str):
                            cleaned_item = re.sub(r'[^a-zA-Z0-9\s@_-]',
                                                  '', item)
                            cleaned_data.append(cleaned_item)
                        else:
                            cleaned_data.append(item)

                    my_list = cleaned_data[0].split(" ")
                    instance_id = my_list.pop(0)
                    my_dict = {}
                    for i in range(0, len(my_list), 2):
                        my_dict[my_list[i]] = my_list[i + 1]
                    for k, v in my_dict.items():
                        self.do_update(args[0] + " " +
                                       instance_id + " " + k + " " + v)

                else:
                    new_instance = re.search(r'\((.*?)\)', args[1]).group(1)

                    data = [
                        new_instance
                    ]

                    cleaned_data = []

                    for item in data:
                        if isinstance(item, str):
                            cleaned_item = re.sub(r'[^a-zA-Z0-9\s@_-]',
                                                  '', item)
                            cleaned_data.append(cleaned_item)
                        else:
                            cleaned_data.append(item)

                    self.do_update(args[0] + " " + cleaned_data[0])
        else:
            print("*** Unknown syntax:", arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
