result_search = []
for x in '0123456789AB':
    for y in '0123456789AB':
        t = int(y + 'AA' + x, 12) + int(x + '02' + y, 14)
        if t % 80 == 0:
            result_search.append(t)
if result_search:
    print(min(result_search) // 80)
