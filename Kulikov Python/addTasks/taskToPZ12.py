_str = list(map(str,input()))
_str.remove('[')
_str.remove(']')
f = list(("".join(_str)).split(','))
g = []
print(f)
for x in f:
    int(x)
    g.append(x)
_m =g.pop(g.min)
print(_m + g.min())
    