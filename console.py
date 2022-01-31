#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd, sys
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Defining HBNBCommand Class """

    prompt = '(hbnb) '
    __classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        'Quit command to exit the program'
        quit()
    def do_EOF(self, arg):
        'EOF command to exit the program'
        quit()
    def do_create(self, arg):
        'create command to Creates a new instance of BaseModel'
        arg = arg.split()
        if arg is None:
            print ("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print ("** class doesn't exist **")
        else:
            new = eval(arg[0] + '()')
            models.storage.save()
            print(new.id)

    def do_show(self, arg):
        'show command to Prints the string representation of an instance based on the class name and id'
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print ("** class doesn't exist **")
        else:
            all_obj = models.storage.all()
            key_value = arg[0] + '.' + arg[1]
            if key_value in all_obj:
                print(all_obj[key_value])
            else:
                print("** no instance found **")
    def do_destroy(self, arg):
        'destroy command to Deletes an instance based on the class name and id'
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print ("** class doesn't exist **")
        elif len(arg) == 1:
            print ("** instance id missing **")
        else:
            all_obj = models.storage.all()
            key_value = arg[0] + '.' + arg[1]
            if key_value in all_obj:
                all_obj.pop(key_value,None)
                models.storage.save()
            else:
                print ("** no instance found **")

    def do_all(self, arg):
        'all command to Prints all string representation of all instances based or not on the class name'
        all_obj = models.storage.all()
        new_list = list()
        if len(arg) == 0:
            for obj in all_obj.values():
                new_list.append(obj.__str__())
            print (new_list)
        elif arg not in HBNBCommand.__classes:
            print ("** class doesn't exist **")
        else:
            for obj in all_obj.values():
                new_list.append(obj.__str__())
            print (new_list)

    def do_update(self, arg):
        'Updates an instance based on the class name and id by adding or updating attribute'
        all_obj = models.storage.all()
        arg = arg.split()
        
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            key_value = arg[0] + '.' + arg[1]
            obj = all_obj.get(key_value, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, arg[2], arg[3].lstrip('"').rstrip('"'))
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()