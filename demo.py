
print('Hello Shuvo')
A = 2;
B = 4;

sum = A**B; #power **
print('total sum:',sum)

nyc_bal = 188
bal_pittt = 247
total_dis = nyc_bal+bal_pittt
print(total_dis)

mph=65
time=total_dis/mph
print(round(time, 2))

# *********String********

text = "ice cream" 
print(text[0:3])
print(text[4:])

adress = '''1 purple street
new york
USA'''

print(adress)

s1= "hello"
s2= "world"
num=25

sum=s1+' '+s2+' '+str(num)
print(sum )

# *********List********

item=["bread","pasta","fruits","vegetable","suger"]
print(item)
print(item[4])
item[0]='chips'
print(item)
print(item[0:3])
print(item[-1])
item.insert(1,"butter")
print(item)
bathroom=["shampoo","soap"]
my_item=food+bathroom
print(my_item)
print(len(my_item))
print("bread" in my_item)

# ********If Satement**********

# odd or even
n=int(input("Enter a number: "))

if n%2 != 0:
   print("Weird")
elif n%2 == 0 and 2<n<=5:
   print("Not Weird")
elif n%2 == 0 and 6<n<=20:
   print("Weird")
else:
   print("Not Weird")

indian=["samosa","daal","naan"]
chinese=["egg role","pot sticker","fried rice"]
italian=["pizza","pasta","risotto"] 

dish = input("Enter a dish name: ")
if dish in indian:
   print("Indian")
elif dish in chinese:
   print("Chinese")
elif dish in italian:
   print("Italian")
else:
   print("i don't know!")


# *******For loop******

1
exp = [2340, 2500, 2100, 3100, 2980]
total = exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
print(total)
t=0
for item in exp:
    t = t + item
print(t)

2
print("print 1 to 10")
for i in range(1,11):
    print(i)

3
exp = [2340, 2500, 2100, 3100, 2980]
t=0
for i in range(len(exp)):
    print("Your Month ",(i+1),'Expense :',exp[i])
    t=t+exp[i]

print("Total expense is :",t)

4
key_location = "chair"
location = ["garage", "living room", "chair", "cloest"]
for i in location:
    if i == key_location:
        print("Key is found in",i)
        break
    else:
        print("Key is not found in",i)

5
for i in range(1,6):
    if i%2 ==0:
        continue
    print(i*i)

# ********While loop*********
1 
i=1
while i<=5:
    print(i)
    i = i +1

# ********Function***********

1
def calculate_total(exp):
    total = 0
    for item in exp:
        total=total+item
    return total


tom_exp_list = [2100,3400,3500]
joe_exp_list = [200,500,700]

# total = 0
# for item in tom_exp_list:
#     total = total+item
# print("Tom's total expenses:",total)

# total=0
# for item in joe_exp_list:
#     total = total+item
# print("Joe's total expenses:",total)

tom_total = calculate_total(tom_exp_list)
joes_total = calculate_total(joe_exp_list)

print("Tom's total expenses:",tom_total)
print("Joes's total expenses:",joes_total)

2

def sum(a,b):
    """
    This Function takes two arguments which are integer number
    and it will return sum of them as an output
    """

    total=a+b
    return total

x = int(input("enter the first number:"))
y = int(input("enter the second number:"))

n= sum(x,y)

print("Total Sum:",n)

# 3 leap year
def is_leap(year):
    leap = False
    

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap


year = int(input())
# year = 2000
print(is_leap(year))

4
n = int(input())
  
for i in range(1,n+1):
        print(i,end="")

5
import numpy

def arrays(arr):
    return (numpy.array(arr[::-1], float))
    

arr = input().strip().split(' ')
result=arrays(arr)

print(result)

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return(numpy.array(arr[::-1], float))                       
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# **********Dictionaries************

d={"tom":75656855588, "rob":7885458585, "jeo":758666999985}
print(d)

d["sam"]=7879995658899
print(d)

del d["jeo"]
print(d)

for key in d:
    print("key:",key,"value:",d[key])

for k,v in d.items():
    print("key:",key,"value:",v)

c="tom" in d
print(c)

a="amir" in d
print(a)

e=d.clear()
print(e)

# **********Tuples**********

point =(5,6)
print(point[1]) 

# **********Modules*********

import math

d=math.sqrt(16)
print(d)

c=math.pow(2,5)
print(c)

a=math.log10(100)
print(a)

b=math.floor(2.3)
print(b)

n=math.ceil(2.3)
print(n)


import calendar

cel = calendar.month(2025,1)
print(cel)

c=calendar.isleap(2025)
print(c)

import functions

a=functions.calculate_square_area(5)
b=functions.calculate_triangle_area(2,5)
print(a,b)

1
n = int(input())
arr = map(int, input().split())
arr1 = set(arr)
arr2 = sorted(arr1)
print(arr2)
print(arr2[-2])

2
alist = []
for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))



# **********JSON***********

f = open("G://New learning//python//book.txt","r")
s = f.read()


import json
b = json.loads(s)
p=type(b)
c=b['bob']['address']
print(p)
print(c)
print(b)

for person in b:
    print(b[person])


# *********Exception hendling*************

x=input("Enter Number:")
y=input("Enter another Number:")

try:
    z = x / int(y)
except ZeroDivisionError as e:
    print("Division by zero exceotion1")
    z=None
except TypeError as e:
    print("TypeError exception")
    z=None
print("Division is: ",z)





