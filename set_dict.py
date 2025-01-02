# numbers = [1,2,3,4,5,6,7]
# even = []
# for i in numbers:
#     if i%2 ==0 :
#         even.append(i)
# print(even)

#or

# even = [i for i in numbers if i%2 == 0]
# print(even)

# sqr_numbers =[i*i for i in numbers]
# print(sqr_numbers)

s = set([1,1,2,3,4,5,2,3,3])
print(s)
e = {i for i in s if i %2 ==0}
print(e)

cities =["dhaka","ney york","paris"]
countries = ["bangladesh","usa","france"]
z=zip(cities,countries)
for a in z:
    print(a)

d = {city:country for city, country in zip(cities,countries)}
print(d)