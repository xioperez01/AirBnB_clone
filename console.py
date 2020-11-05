#!/usr/bin/python3
"""
Contains the entry point
of the command interpreter
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City, "\
    Place": Place, "Review": Review, "State": State}


class HBNBCommand(cmd.Cmd):
    """ Entry point
    of the command interpreter """
    file = None
    if sys.stdin.isatty():
        intro = "*****************************\n*\
                           *\n*       Welcome :)          *\n*\
                           *\n*****************************\n"
        prompt = "(hbnb) "
    else:
        prompt = "(hbnb) \n"

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program with  Ctrl+D\n"""
        print()
        return True

    def emptyline(self):
        """Do not execute anything\n"""
        pass

    def do_create(self, arg):
        """Creates a new instance\n"""
        if len(arg) is 0:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance\n"""
        line = arg.split()
        if len(arg) is 0:
            print("** class name missing **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        elif len(line) != 2:
            print("** instance id missing **")
        else:
            name = "{}.{}".format(line[0], line[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[name])

    def do_destroy(self, arg):
        """Deletes an instance\n"""
        line = arg.split()
        if len(arg) is 0:
            print("** class name missing **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        elif len(line) != 2:
            print("** instance id missing **")
        else:
            name = "{}.{}".format(line[0], line[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[name]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances\n"""
        line = arg.split()
        objects_list = []
        if len(arg) is 0:
            for objs in storage.all().values():
                objects_list.append(objs)
            print(objects_list)
        elif line[0] not in classes:
            print("** class doesn't exist **")
        else:
            for k, objs in storage.all().items():
                if line[0] in k:
                    objects_list.append(objs)
            print(objects_list)

    def do_count(self, arg):
        """Update the number of instances of a class\n"""
        count = 0
        for key, objs in storage.all().items():
            if arg in key:
                count += 1
            print(count)


if __name__ == '__main__':
    '''main loop for console'''
    HBNBCommand().cmdloop()
