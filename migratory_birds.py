
arr = "1 2 3 4 5 4 3 2 1 3 4".split(" ")


def migratoryBirds(arr):
    Type_count = {}
    for _ in arr:
        if _ not in Type_count.keys():
            Type_count[_] = 1
        else:
            Type_count[_] += 1
    l = [x[0] for x in Type_count.items() if x[1] == max(Type_count.values())]
    return sorted(l)[0]
    
    
print(migratoryBirds(arr))