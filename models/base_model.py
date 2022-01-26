#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

class BaseModel:

    def __init__(self, *args, **kwargs):

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.update_at = datetime.today()

        if kwargs is not None:
            for k, v in kwargs.items():
                if k == "created_at" or k == "update_at":
                    self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = v

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        
    def save(self):
        self.update_at = datetime.today()
    def to_dict(self):
        cdict = self.__dict__.copy()
        cdict["created_at"] = self.created_at.isoformat()
        cdict["update_at"] =  self.update_at.isoformat()
        cdict["__class__"] = self.__class__.__name__
        return cdict
