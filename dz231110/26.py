f = open("26.txt")
n = int(f.readline())
boxes = []
for s in f:
    boxes.append(int(s))
boxes.sort(reverse=True)
res = [boxes[0]]
for i in range(1, n):
    if res[-1] - boxes[i]>=3:
        res.append(boxes[i])
print(len(res), min(res))