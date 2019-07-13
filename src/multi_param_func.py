def func1(*p):
    return p

def func2(**p):
    for k,v in p.items():
        return k,v

b = func2(a=1, b=2, c=3, d=4)
print(b)

a = func1(1,2,3,4,5,6)
print(a)
