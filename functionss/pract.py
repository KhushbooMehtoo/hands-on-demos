# Question 1: Reverse a String
# Write a program to reverse a string without using built-in reverse functions.

# name="Atul"
# arr=[]
# for word in name:
#     arr.insert(0,word)
#     # print(arr)
#     rev=''.join(arr)
# print(f"Reverse a string: {rev}")


#.........recursion.............#
# name="atul"
# def rever():
#     global name
#     arr=list(name)
#     if arr in name:
#         return
   
#     x=arr[::-1]
#     print(x)
#     rever()
# print(rever())

# n=0
# def number():
#     global n
#     if n==5:
#         return
#     n=n+1 
#     print(5-n)
#     number()
# print(number())

#  Question 3: Count Vowels in a String
# Write a program to count the number of vowels (a, e, i, o, u) in a string.

# def check(s):
#     flag = False
#     vowel="aeiou"
    
#     for vol in vowel:
#         if vol in s:
#             flag=True
    
#     return flag
# print(check("khush"))

#  Question 4: Print Pattern (Triangle)
# Write a program to print a triangle pattern of stars.
# x=0
# y=8
# def star():
#     global x,y
#     if x==y:
#         return
#     x=x+1
#     print((y-x)*"*")
#     star()
# star()

# def even(lis):
    
#     count=0
#     for num in lis:
#         if num % 2==0:
#             print(num)
#             count=count+1
        
#     return "Total Even numbers: ",count
# print(even([2,4,3,4,1,5,6]))
# remove duplicate from list
def duplicate(lis):
    arr=[]
    for num in lis:
        if num not in arr:
            arr.append(num)
            # print(arr)
    
    return arr
print(duplicate([1,1,2,4,3,2,4,5,3]))
