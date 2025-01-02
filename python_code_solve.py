#1 odd or even
#n=int(input("Enter a number: "))

#if n%2 != 0:
#    print("Weird")
#elif n%2 == 0 and 2<n<=5:
#    print("Not Weird")
#elif n%2 == 0 and 6<n<=20:
#    print("Weird")
#else:
#    print("Not Weird")

#2 
# a = int(input())
# b = int(input())
    
# add = a+b
# sub = a-b
# mult = a*b
    
# print(add)
# print(sub)
# print(mult)

#3
# a = int(input())
# b = int(input())
    
# x=a//b
# y=a/b
    
# print(x)
# print(y)

#4

# n = int(input())

# for i in range(n):
#     print(i*i)

#5 leap year

# def is_leap(year):
#     leap = False
    

#     if year % 400 == 0:
#         leap = True
#     elif year % 100 == 0:
#         leap = False
#     elif year % 4 == 0:
#         leap = True
    
#     return leap

# year = int(input())
# print(is_leap(year))

#6
# n = int(input())
    
# for i in range(1,n+1):
#     print(i,end="")


#7
# n = int(input())
# arr = map(int, input().split())
# a = set(arr)
# b = sorted(a)
# print(b[-2])


#8
# alist = []
# for i in range(int(input())):
#         name = input()
#         score = float(input())
#         alist.append([name, score])
# second_highest = sorted(set([score for name, score in alist]))[1]
# print('\n'.join(sorted([name for name, score in alist if score == second_highest])))

#9

# import numpy

# def arrays(arr):
#     # complete this function
#     # use numpy.array
#     return(numpy.array(arr[::-1], float))                       
# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)

#10

n= int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float,line))
    student_marks[name] = scores
query_name = input()
print("%.2f" %(sum(student_marks[query_name])/len(student_marks[query_name])))