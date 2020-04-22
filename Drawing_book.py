n = 5
p = 4
temp = []
page_sets = [[x,x+1] for x in range(0,n+1,2)]
f_count = 0
b_count = 0
for f,b in zip(page_sets,page_sets[::-1]):
    if p not in f:
        f_count += 1
    else:
        ff_count = f_count
    if p not in b:
        b_count += 1
    else:
        bf_count = b_count
print(min(ff_count,bf_count))