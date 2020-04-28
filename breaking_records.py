s = "10 5 20 20 4 5 2 25 1"
scores = list(map(int, s.rstrip().split()))

def breakingrecords(scores):
    change = [0,0]
    least = scores[0]
    most = scores[0]
    for _ in scores[1:]:
        if _ > most:
            change[0] += 1
            most = _
        elif _ < least:
            change[1] += 1
            least = _
    print(change[0],change[1])

breakingrecords(scores)