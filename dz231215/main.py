
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

def separation(s):
    exer = []
    l = ""
    for i in s:
        if i in ('+', '-', '*', '/', '(', ')'):
            if len(l)!=0:
                exer.append(l)
                l = ""
            exer.append(i)

        else:
            l+=i
    if len(l)!=0:
        exer.append(l)
    exer.append('+')
    exer.append('0')
    return exer


def solution(s):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ')': 3}
    # print(operators['+'])
    numbers = []
    signs = []
    exer = separation(s)
    for i in exer:
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
     print(solution("602-(3+99)"))
    #print(solution('8-9'))

