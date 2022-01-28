#!/usr/bin/python3 
"""Defining base_model"""

import models
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """Defining a BaseModel class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel class
        Args:
            *args: unused
            **kwargs(dict): key/value pairs
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] =  datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """return string representation of BaseModel"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """update the updated_at instance attributes"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dictionary representation of BaseModel"""
        instance_dict = dict(self.__dict__)
        instance_dict['created_at'] = self.__dict__['created_at'].isoformat()
        instance_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
