def f(inp):
    res = []
    n = 0
    for i in range(len(inp)):
        if inp[i] in ("+", "-", "*", "/", "(", ")"):
            res.append(int(inp[n:i]))
            res.append(inp[i])
            n = i + 1
    res.append(int(inp[i:]))

    return res


print(f("3+5*7"))
