'''
CORE BEHAVIOR
=============
it's a core about behavior inheritance from Anchor in application core, this class
provide standard and anything for class behavior class in application.

:package :     core stigma
'''
from abc import abstractmethod, ABCMeta
from core.application import Anchor


class _Behavior(Anchor):
    '''
    Behavior base class, for parent class behavior below. used to provide variable,
    object and type_data only for behavior needed.
    '''
    model = None


class Behavior(_Behavior):
    __metaclass__ = ABCMeta

    def __init__(self):
        '''
        Behavior class, you can check it from the documentation for more information
        '''
        super(Behavior, self).__init__()

    @abstractmethod
    def alias(self):
        '''
        an abstract method is used to collecting method or data for model class.
        '''
        pass