
s = 'saveChangesInTheEditor'
def camelcase(s):
    start = 0
    for index,value in enumerate(s):
        if value.isupper():
            print(s[start:index])
            start = index
    print(s[start:])



camelcase(s)