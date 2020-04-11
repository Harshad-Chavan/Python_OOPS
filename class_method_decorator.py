# class_method_decorator

class InstanceCounter(object):
    count = 0
    def __init__(self,val):
        self.val = val
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
c =InstanceCounter(30)

for _ in (a,b,c):
    print("value :: {}".format(_.val))
    print("count :: {}".format(_.count))
