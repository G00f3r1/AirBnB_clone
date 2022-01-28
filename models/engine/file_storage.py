#!/usr/bin/python3
"""Defining file_storage model"""

import json
from models.base_model import BaseModel

class FileStorage:
    """Defining FileStorage class"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = dict()
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict().copy()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, mode='r') as file:
                new_dict = json.load(file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                self.__objects[key] = obj

        except FileNotFoundError:
            return
