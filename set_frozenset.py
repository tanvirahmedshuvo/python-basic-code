basket = {"orange","apple","mango","apple","orange"}
p=type(basket)
print(basket)

a=set()
a.add(1)
print(a)

numbers = [1,1,2,3,4,2,3,4]
u_num = set(numbers)
print(u_num)


#frozenset

fs = frozenset(numbers)
print(fs)

x = {"a","b","c"}
y = {"a","h","g"}

v = x|y
print(v)
n = x&y
print(n)
z = x-y
print(z)