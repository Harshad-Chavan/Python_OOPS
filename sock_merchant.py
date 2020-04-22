n = 9
ar = "6 5 2 3 5 2 2 1 1 5 1 3 3 3 5".split(" ")

def sockMerchant(n, ar):
    pair_count = 0
    temp = ar
    for index,value in enumerate(temp[0:]):
        print(index,value)
        count = temp.count(value)
        if count  > 1:
            pair_count += count // 2
        while count != 0:
            temp.remove(value)
            count -= 1
        print(temp)
    print(pair_count)
        
                 
    
sockMerchant(n,ar)