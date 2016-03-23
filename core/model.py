'''
CORE MODEL
==========
it's a core about model inheritance from Anchor in application core, this class
provide standard and anything for class model class in application.

:package :     core stigma
'''
from abc import abstractmethod, ABCMeta
from core.application import Anchor


class _Model(Anchor):
    '''
    model base class, for parent class model below. used to provide variable,
    object and type_data only for model needed.
    '''
    behavior = None


class Model(_Model):
    __metaclass__ = ABCMeta

    def __init__(self):
        '''
        Model class, you can check it from the documentation for more information
        '''
        super(Model, self).__init__()

    @abstractmethod
    def layer(self):
        '''
        an abstract method is used layering the model method.
        '''
        pass
