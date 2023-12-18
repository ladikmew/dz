# def f(inp):
#     res = []
#     n = 0
#     for i in range(len(inp)):
#         if inp[i] in ("+", "-", "*", "/",")"):
#             res.append(int(inp[n:i]))
#             res.append(inp[i])
#             n = i + 1
#         elif inp[i] in ("("):
#             #res.append(inp[n:i])
#             res.append(inp[i])
#             n = i + 1
#     if res[len(inp)-1]!=")":
#         res.append(inp[i:])
#
#     return res
#
# print(f("3+(5*7)"))

def summ(a, b):
    return a + b


def minus(a, b):
    return a - b


def composition(a, b):
    return a * b


def devision(a, b):
    return a / b


def making_operation(signs, numbers, i):
    cur_sign = signs.pop()
    signs.append(i)
    b = numbers.pop()
    a = numbers.pop()
    if cur_sign == "+":
        numbers.append(summ(a, b))
    if cur_sign == "-":
        numbers.append(minus(a, b))
    if cur_sign == "*":
        numbers.append(composition(a, b))
    if cur_sign == "/":
        numbers.append(devision(a, b))


def solution(s):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ')': 3}
    # print(operators['+'])
    numbers = []
    signs = []

    for i in s:
        if i not in ('+', '-', '*', '/', '(', ')'):
            numbers.append(int(i))
        else:
            if i != ")":
                if len(signs) == 0:
                    signs.append(i)
                else:
                    if operators[i] > operators[signs[len(signs) - 1]]:
                        signs.append(i)
                    elif operators[i] <= operators[signs[len(signs) - 1]]:
                        if operators[signs[len(signs) - 1]] == 3:
                            signs.append(i)
                        else:
                            making_operation(signs, numbers, i)
            else:
                while signs[len(signs) - 1] != "(":
                    making_operation(signs, numbers, i)
                    f = signs.pop()
                f = signs.pop()
    if signs[0] == "+":
        res = summ(numbers[0], numbers[1])
    if signs[0] == "-":
        res = minus(numbers[0], numbers[1])
    if signs[0] == "*":
        res = composition(numbers[0], numbers[1])
    if signs[0] == "/":
        res = devision(numbers[0], numbers[1])
    return res


if __name__ == "__main__":
     print(solution("4+((6/2)*3)"))
    #print(solution('8-9'))
