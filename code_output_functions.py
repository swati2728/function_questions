# Question 1

# def employee(name,salary=20000):
#         print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak")

# Question 2

# def primeorNot(num):     
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")

#     else:
#            print(num,"is not a prime number")
# primeorNot(406)

# Question3

# def greet(*names):
#     for name in names:
#                print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

# Question 4 

# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum

# print(sumofdigits(123))

# Question 5 

def  meal(day,time):
    if day=="sunday":
        if time=="breakfast":
            return "dosa"
        elif time=="lunch":
            return "dal rice"
        elif time=="dinner":
            return "paneer and  chapati"
        else :
            return "time not found"
    elif day=="monday":
        if time=="breakfast":
            return "fried rice"
        elif time=="lunch":
            return "aloo rice"
        elif time=="dinner":
            return "chhole bhature"
        else :
            return "time not found"
    elif day=="other":
        if time=="breakfast":
            return "aloo"
        elif time=="lunch":
            return "rajma rice"
        elif time=="dinner"    :
            return "veg-chapati"
        else :
            return "time not found"
            
print(meal("sunday","lunch"))
print(meal("monday","dinner"))