#!/usr/bin/python3
"""
Contains the entry point
of the command interpreter
"""
import cmd
import sys


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
        """ Shouldn’t execute anything """
        pass


if __name__ == '__main__':
    '''main loop for console'''
    HBNBCommand().cmdloop()
