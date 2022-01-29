#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd, sys

class HBNBCommand(cmd.Cmd):
    """Defining HBNBCommand Class """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        quit()
    def do_EOF(self, arg):
        'EOF command to exit the program'
        quit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
