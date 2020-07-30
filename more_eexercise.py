# Question 1

# i=1
# while i<=1000:
# 	if i%2==0:
# 		print("nav")
# 	if i%7==0:
# 		print("gurukul")
# 	if i%21==0:
# 		print("navgurukul")
# 	i=i+1	

# Question 2

# Number_of_students=input("enter a name:")
# Ek_student_ka_kharcha=int(input("enter a spending amount:"))
# if Ek_student_ka_kharcha<=50000:
# 	print("Hum budget ke andar hain")
# else:
# 	print(" hum budget ke bahar hain")

# # Question 3

password=input("enter your sakht password:")
if len(password)>6 or len(password)>16:
	if "$" in password:
		if 2 or 8 in password:
			if "A" or "Z" in password:
				print("it is Strong password")
else:
	print("it is Weak password")


# Question 4 

# num1=int(input("enter a first numbers:"))
# num2=int(input("enter a second numbers:"))
# num3=int(input("enter a third numbers:"))
# if num1>num2:
# 	print(num1,"is highst")
# elif num2>num1:
# 	print(num2,"is highst")
# elif num3>num1:
# 	print(num3,"is highst")
# elif num3>num2:
# 	print(num3,"is highst")
# elif num2>num3:
# 	print(num2,"is highst")
# elif num1>num3:
# 	print(num1,"is highst")
# else:
# 	("nothing")		


# Question 5

# Question 6

# string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# new_list=[ ]
# index=0
# while index<len(string_list):
# 	if string_list[index] not in new_list:
# 		new_list.append(string_list[index])
# 	index=index+1
# print(new_list)

# Question 7

# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# new_list=[ ]
# index=0
# while index<len(list1):
# 	if list1[index] in list2:
# 		new_list.append(list1[index])
# 	index=index+1
# print(new_list)	

# Question 8

# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# list3=[ ]
# index=0
# while index<len(list1):
# 	list2.append(list1[index])
# 	index=index+1
# print(list2)
# j=0
# while j<len(list2):
# 	if list2[j] not in list3:
# 		list3.append(list2[j])
# 	j=j+1
# print(list3)
		
		
# # Question 9

# # def is_harshad_number(num):
# # numbers=(input("enter a number:"))
# # x=numbers.split()
# print(x)  

# Question 10

# numbers= [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# index=0
# while index<len(numbers):
# 	print(max(numbers[index]))
# 	index=index+1
	
#
# numbers= [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# index=0
# maxi=[]
# while index<len(numbers):
# 	j=0
# 	maximum=0
# 	while j<len(numbers[index]):
# 		if numbers[index][j]>maximum:
# 			maximum = numbers[index][j]
# 		j=j+1
# 	maxi.append(maximum)
# 	index=index+1
# print(maxi)	

# Question 11

# words = "navgurukul is great"
# counter = 0
# while counter < len(words):
#     print (words[counter])
#     counter=counter+1
