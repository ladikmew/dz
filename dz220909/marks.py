import pandas as pd
import numpy as np

d = [
    {
        "name": "Artem",
        "value": 5,
        "klass": "10N",
    },

    {
        "name": "Stas",
        "value": 3,
        "klass": "10N",
    },

    {
        "name": "Lada",
        "value": 4,
        "klass": "10N",
    },
]

data = pd.DataFrame(d)

data.to_csv("klass.csv")

def get_name(klass, value):
    if "10N" in d and c == "5":
        s.append(b)


with (open("klass.csv", "r")) as f:
    for line in f:
        a, b, c, d = map(str, line.split(','))
        s = input().split()
        get_name(c,a)
print(*s)

