f = open('24.txt').readlines()
li = []
for j in f:
    st = ''
    for x, y in zip(j, j[1:]):
        if x == 'T':
            st += y
    maxi = max(st.count(i) for i in set(st))
    for s in set(st):
        if st.count(s) == maxi:
            li += [s]
print(max(li.count(l) for l in set(li)))