#!/usr/bin/python3
""" Class BaseModel """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ construct """


    def __init__(self, *args, **kwargs):
        """ Construct """
        if kwargs:
            for key, value in kwargs.items():
                date_format = "%Y-%m-%dT%H:%M:%S.%f"
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, date_format)
                elif key == 'created_at':
                    value = datetime.strptime(value, date_format)
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ String """
        # return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.to_dict)

        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))

    def save(self):
        """ save function """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ copy of original dictionary """
        obj_ct = self.__dict__.copy()
        obj_ct['__class__'] = self.__class__.__name__
        obj_ct['created_at'] = self.created_at.isoformat()
        obj_ct['updated_at'] = self.updated_at.isoformat()
        return obj_ct
