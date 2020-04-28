
n = 6

k = 3

ar = list(map(int, "1 3 2 6 1 2".rstrip().split()))

def divisibleSumPairs(n, k, ar):
    count = 0
    for index,value in enumerate(ar):
        while index < len(ar) - 1 :
            
            if index < index+1 and (value + ar[index+1]) % k == 0:
                count += 1
        index += 1
    return count

print(divisibleSumPairs(n,k,ar))