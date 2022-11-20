#!/usr/bin/python3
"""The entry point of the command interpreter"""
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import cmd
import shlex


class HBNBCommand(cmd.Cmd):
    """Defining HBNBCommand Class """

    prompt = '(hbnb) '

    classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Review': Review
            }

    intiger = [
            'number_rooms',
            'number_bathrooms',
            'max_guest',
            'price_by_night'
            ]
    floating = ['latitude', 'longitude']

    def default(self, arg):
        '''default method '''
        fun_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        args = arg.split(".", 1)
        f_class = args[0]
        if (f_class in self.classes) and len(args) >= 2:
            args = "".join(args[1:]).split("(")
            f_func = args[0]
            if (f_func in fun_dict) and len(args) >= 2:
                f_args = " ".join(tuple("".join(args[1:])[:-1].split(", ")))
                fun_dict[f_func]("{} {}".format(f_class, f_args))
                return False
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        '<Quit> command to exit the program.'
        return True

    def do_EOF(self, arg):
        '<EOF> command to exit the program.'
        return True

    def emptyline(self):
        """Don't do any thing when receiving an empty line."""
        pass

    def do_create(self, arg):
        '''<create> command to Creates a new instance of BaseModel
        Usage: create <class name>
        '''
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.classes[arg]()
            storage.save()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        '''<show> command to Prints the string representation of an instance
        based on the class name and id
        Usage: show <class name> <id>
        '''
        new = arg.partition(' ')
        class_name = new[0]
        class_id = new[2]

        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif not class_id:
            print("** instance id missing **")
        else:
            key = class_name + "." + class_id
            try:
                print(storage._FileStorage__objects[key])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''<destroy> command to Deletes an instance based on
        the class name and id
        Usage: destroy <class name> <id>
        '''

        new = arg.partition(' ')
        class_name = new[0]
        class_id = new[2]

        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif not class_id:
            print("** instance id missing **")
        else:
            key = class_name + "." + class_id
            try:
                del(storage.all()[key])
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        '''<all> command to Prints all string representation of all
        instances based or not on the class name
        Usage: all <class name> or all
        '''

        args = arg.split()
        if len(args) == 0:
            for key, value in storage.all().items():
                print(value)
            return False
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return False
        else:
            for key, value in storage.all().items():
                if key.startswith(class_name):
                    print(value)

    def do_update(self, arg):
        '''<updates> command to Update an instance based on the class name
        and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        '''

        args = shlex.split(arg)
        if len(arg) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                if args[0] == 'Place':
                    if args[2] in self.intiger:
                        args[3] = int(args[3])
                    if args[2] in self.floating:
                        args[3] = float(args[3])

                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()

    def do_count(self, arg):
        """Count Classes"""

        args = arg.split()
        count = 0
        if len(args) > 0:
            for obj in storage.all():
                if obj.startswith(args[0]):
                    count += 1
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
