#!/usr/bin/python3 
"""Defining base_model"""

import models
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """Defining a BaseModel class that defines all common attributes/methods for other classes"""

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        instance_dict = dict(self.__dict__)
        instance_dict['created_at'] = self.__dict__['created_at'].isoformat()
        instance_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
