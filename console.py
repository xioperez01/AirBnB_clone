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
from models.user import User
classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City, "\
    Place": Place, "Review": Review, "State": State, "User": User}


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
        """\n Creates a new instance and prints the id
    -> Use: (hbnb ) create ClassName <-\n"""
        if len(arg) is 0:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """\n Prints the string representation of an instance
    -> Use: (hbnb ) show ClassName id <-\n"""
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
        """\n Deletes an instance based on the class name and id
    -> Use: (hbnb ) destroy ClassName id <-\n"""
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
        """\n Prints all string representation of all instances
    -> Use: (hbnb ) ClassName <-
                or
    -> Use: (hbnb ) all <-\n"""
        line = arg.split()
        if len(arg) is 0:
            for objs in storage.all().values():
                print(objs)
        elif line[0] not in classes:
            print("** class doesn't exist **")
        else:
            for k, objs in storage.all().items():
                if line[0] in k:
                    print(storage.all()[k])

    def do_update(self, arg):
        """\n Updates an instance based on the class name and
        id by adding or updating attribute\n-> Use: update ClassName \
id attribute_name attribute_value <-\n"""
        line = arg.split()
        check_id = "{}.{}".format(line[0], line[1])
        if len(arg) is 0:
            print("** class name missing **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            if check_id not in storage.all().keys():
                print("** no instance found **")
            elif len(line) == 2:
                print("** attribute name missing **")
            elif len(line) == 3:
                print("** value missing **")
            else:
                cast = type(eval(line[3]))
                arg_3 = line[3].strip('"')
                setattr(storage.all()[check_id], line[2], cast(arg_3))
                storage.all()[check_id].save()

    def do_count(self, arg):
        """\n Update the number of instances of a class\n"""
        count = 0
        for k, objs in storage.all().items():
            if arg in k:
                count += 1
            print(count)


if __name__ == '__main__':
    '''main loop for console'''
    HBNBCommand().cmdloop()
