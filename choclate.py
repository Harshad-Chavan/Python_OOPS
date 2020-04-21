s = [1, 2, 1, 3, 2]
# s = [1, 2, 3, 4, 5,6,7]
d = 3 
m = 2
l = []
def birthday(s, d, m):
    i = 0
    count = 0
    for _ in s[i:len(s)]:
        if sum(s[i:(i + m)]) == d:
            count += 1
        i += 1
    print(count)
birthday(s,d,m)