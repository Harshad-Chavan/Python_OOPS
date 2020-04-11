# abstract_class

import abc

class GetterSetter(abc.ABC):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self,val):
        # Have to implement this method
        return

    @abc.abstractmethod
    def get_val(self):
        # Have to implement this method
        return

class Myclass(GetterSetter):
    def set_val(self,val):
        self.val = val
    
    def get_val(self):
        return self.val


x = Myclass()
print(x)
