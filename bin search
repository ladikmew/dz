a = sorted(list()[el**2 for el in range(10)]) + list([-el**2 for el in range(10)])

def bin_search(a: list, s) -> int:
    start = 0
    finish = len(a)-1
    while start <= finish:
        sred = (finish + start)//2
        if a[sred]>s:
            start = sred+1
        if a[sred]<s:
            finish = sred-1
        if a[sred]==s:
            return sred


def bin_search2(a: list, s) -> int:
    start = 0
    finish = len(a)-1
    while start <= finish:
        sred = (finish + start)//2
        if a[sred]<s:
            start = sred+1
        if a[sred]>s:
            finish = sred-1
        if a[sred]==s:
            return sred
        if start==finish and s!=:
            
