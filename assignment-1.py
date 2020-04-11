# assignment-1

class MaxSizeList(object):
    def __init__(self,max_length):
        self.emp_list = []
        self.max_length = max_length

    def push(self,value):
        cur_length = len(self.emp_list)
        if cur_length == self.max_length:
           self.emp_list.pop(0)
           self.emp_list.append(value)
        else:
            self.emp_list.append(value)
    
    def get_list(self):
        return self.emp_list

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())


