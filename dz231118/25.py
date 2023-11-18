from fnmatch import *
for i in range(2024,10**10+1,2024):
    if fnmatch(str(i),'3?6906*4'):
        print(i)
