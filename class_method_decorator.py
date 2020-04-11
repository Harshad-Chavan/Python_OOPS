# class_method_decorator

class InstanceCounter(object):
    count = 0
    
    # adding a static method (method which is not bound the class nor to the instance)
    @staticmethod
    def check_int(value):
        if not isinstance(value,int):
            return 0
        else:
            return value
    
    def __init__(self,val):
        self.val = self.check_int(val)
        InstanceCounter.count += 1
        
    def set_val(self,val):
        self.val = val

    def get_val(self):
        return self.val
    
    
    # # converting this method to a class method
    # def get_count(self):
    #     return InstanceCounter.count

    # converting this method to a class method
    @classmethod
    def get_count(cls):
        return cls.count

    


a =InstanceCounter(10)
b =InstanceCounter(20)
c =InstanceCounter("hello")

for _ in (a,b,c):
    print("value :: {}".format(_.val))
    print("count :: {}".format(_.count))
