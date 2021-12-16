from .models import StockByDate, StockInfo, SourceInfo
from abc import ABCMeta, abstractmethod
from .db_manager import DBConfigManager

class abstractclassmethod(classmethod):
    __slots__ = ()

    def __init__(self, function):
        super(abstractclassmethod, self).__init__(function)
        function.__isabstractmethod__ = True

    __isabstractmethod__ = True

class Repository:

    __metaclass__ = ABCMeta
    db_config_manager = DBConfigManager()
    # Connect to DB with user role
    @staticmethod
    def connect(user):
        return user

    # Create and add new object to DB
    @classmethod
    @abstractmethod
    def create(cls, model):
        pass

    # Get object by pk
    @classmethod
    @abstractmethod
    def read_by_pk(cls, pk):
        pass

    # Get object by filter
    @classmethod
    @abstractmethod
    def read_filtered(cls, filter_dict):
        pass

    # Get all objects
    @classmethod
    @abstractmethod
    def read_all(cls):
        pass

    # Refresh by pk
    @classmethod
    @abstractmethod
    def update_by_pk(cls, pk, update_dict):
        pass

    # Refresh by filter
    @classmethod
    @abstractmethod
    def update_filtered(cls, filter_dict, update_dict):
        pass

    # Refresh all objects
    @classmethod
    @abstractmethod
    def update_all(cls, update_dict):
        pass

    # Delete by primary key
    @classmethod
    @abstractmethod
    def delete_by_pk(cls, pk):
        pass

    # Remove objects matching filter
    @classmethod
    @abstractmethod
    def delete_filtered(cls, filter_dict):
        pass

    @classmethod
    @abstractmethod
    def read_join_filtered(cls, join_field, filter_dict):
        pass