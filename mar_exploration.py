s = 'SOSOOSOSOSOSOSSOSOSOSOSOSOS'
n = 3
def divide_chunks(l, n): 
      for i in range(0, len(l), n):  
        yield l[i:i + n] 

def marsExploration(s):
    count = 0
    for part in list(divide_chunks(s, n)):
        if part[0] != 'S':
            count += 1
        if part[1] != 'O':
            count += 1
        if part[2] != 'S':
            count += 1
    print(count)
    

marsExploration(s)