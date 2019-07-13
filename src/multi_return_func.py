def swap(a,b):
    return b,a

#tuple  return
a =  swap(1,2)
x,y = swap(1,2)

print(type(a))
#return된 tuple값 하나씩 읽기
print(a[0],a[1])
print(a)
print(x,y)