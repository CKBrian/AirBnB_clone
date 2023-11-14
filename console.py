#!/usr/bin/env python3
"""
    contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """implements console cmd interpreter"""

    prompt = "(hbnb) "
    class_names = ["BaseModel", "User", "State",
                   "City", "Amenity", "Place", "Review"]

    def do_create(self, args):
        """
            Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id
        """
        if not args:
            print("** class name missing **")  # ex: $ create
            return
        *arg, = args.split()
        if arg[0] not in type(self).class_names:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """ Prints the string representation of an instance based on
            the class name and id.
        """
        if len(args) == 0:
            print("** class name missing **")  # (ex: $ show)
            return
        *arg, = args.split()
        if arg[0] not in type(self).class_names:
            print("** class doesn't exist **")  # (ex: $ show MyModel)
            return
        if len(arg) == 1:
            print("** instance id missing **")  # (ex: $ show BaseModel)
            return
        storage.reload()
        objects = storage.all()

        obj_id = "{}.{}".format(arg[0], arg[1])
        if obj_id in objects:
            print(objects[obj_id])
            return
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id (save the
            change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        *arg, = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if arg[0] not in type(self).class_names:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        objects = storage.all()
        obj_id = "{}.{}".format(arg[0], arg[1])
        if obj_id in objects:
            del (objects[obj_id])
            storage.save()
            return
        else:
            print("** no instance found **")
            return

    def do_all(self, args):
        """ Prints all string representation of all instances based or not
            on the class name. Ex: $ all BaseModel or $ all
        """
        if len(args) > 0:
            *arg, = args.split()
        if len(args) == 0 or arg[0] in type(self).class_names:
            storage.reload()
            objects = storage.all()
            obj_list = []
            for key, value in objects.items():
                obj_list.append(str(value))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'
        """
        if len(args) == 0:
            print("** class name missing **")  # (ex: $ update)
            return
        *arg, = args.split()
        if arg[0] not in type(self).class_names:
            print("** class doesn't exist **")  # (ex: $ update MyModel)
            return
        if len(arg) == 1:
            print("** instance id missing **")  # (ex: $ update BaseModel)
            return

        objects = storage.all()
        obj_id = "{}.{}".format(arg[0], arg[1])

        if obj_id not in objects:
            print("** no instance found **")  # (ex: $ update BaseModel 121212)
        else:
            if len(arg) == 2:
                print("** attribute name missing **")
                return
            if len(arg) == 3:
                print("** value missing **")
                return
            if (
                arg[2] == 'id' or
                arg[2] == 'created_at' or
                arg[2] == 'updated_at'
            ):
                print(arg[2])
                return
            if arg[2] in objects[obj_id].__dict__.keys():
                data_type = type(objects[obj_id].__dict__[arg[2]])
                objects[obj_id].__dict__[arg[2]] = data_type(arg[3])
            else:
                objects[obj_id].__dict__[arg[2]] = arg[3]
            storage.save()
            return

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
