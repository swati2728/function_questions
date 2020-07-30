# def add():
# 	x=10
# 	y=20
# 	c=x+y
# 	print(c)
# add()	

# def add(y):
# 	x=10
# 	c=x+y
# 	print(c)
# add(20)	

# (1 QUESTION)

# def ask_question():
# 	print("Who is the founder of Facebook?")
# 	print("Mark Zuckerberg",
# 			"Bill Gates",	
# 			"Steve Jobs",
# 			"Larry Page")
# ask_question()	
# ask_question()
# ask_question()
# ask_question()
# ask_question()

# def ask_question():
# 	index=0
# 	while index<=100:
# 		print("Who is the founder of Facebook?")
# 		print("Mark Zuckerberg",
# 			"Bill Gates",	
# 			"Steve Jobs",
# 			"Larry Page",)
# 		print(index)
# 		index=index+1
# ask_question()	
	
# ===============================================

# Default parameter value
#

# def attendance(name,status="absent"):
# 	print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")

# def function_print_lines(name,work="cleaner"):
# 	print("mara naam",name,"hai")
# 	print("Main NavGurukul ka",work,"hun")
# function_print_lines("Rishabh","co-founder")	
# function_print_lines("swati")
# function_print_lines("babaji","co-founder")

 # (QUESTIONS 2)

# def family_members(name,age="older"):
# 	print(name,"is my father")
# 	print("his age is",age)
# family_members("Anand","45")
# family_members("papa")	

# ==================================================================

# QUESTIONS 3(part1)

# def add_numbers(numbers1,numbers2):
# 	print(numbers1+numbers2)
# add_numbers(12,23)


# (part 2)

# def add_numbers_list():
# 	list1= [50, 60, 10]
# 	list2= [10, 20, 13]
# 	index=0
# 	list3=[]
# 	while index<len(list1):
# 		sum=0
# 		sum=list1[index]+list2[index]
# 		list3.append(sum)
# 		index=index+1
# 	print(list3)	
# add_numbers_list()

# ====================================================

# QUESTIONS 4 (PART1)

# def check_numbers():
# 	num=int(input("enter a number"))
# 	if num%2==0:
# 		print("it is even numbers")
# 	else:
# 		print("it is odd numbers")
# check_numbers()			

# # (PART2)
# def check_numbers_list():
# 	list1=[2, 6, 18, 10, 3, 75]
# 	list2=[6, 19, 24, 12, 3, 87]
# 	index=0
# 	while index<len(list1):
# 		if list1[index]%2==0 and list2[index]%2==0:
# 			print(list1[index],list2[index],"both are even numbers by there indexing")
# 		else:
# 			print(list1[index],list2[index],"both are not even,they are odd by there indexing")
# 		index=index+1
# check_numbers_list()	
# =======================================================
 
# (QUESTIONS 5)


# def calculator(number_x,number_y,operation):
# 	if operation=="add":
# 		sum1=number_x + number_y
# 		print(sum1)
# 	elif operation=="subtract":
# 		sum2=number_x - number_y
# 		print(sum2)
# 	elif operation=="multipication":
# 		sum3=number_x * number_y
# 		print(sum3)
# 	else:
# 		sum4=number_x / number_y
# 		print(sum4)	
# calculator(20, 25,"add")	
# calculator(40, 3,"subtract")
# calculator(10, 4,"multipication")
# calculator(40,41,"divide")

# (PART2)
# def calculator(number_x,number_y,operation):
# 	num1=int(input("enter a first numbers"))
# 	num2=int(input("enter a second numbers"))
# 	if operation=="add":
# 		sum1=number_x + number_y
# 		print(sum1)
# 	elif operation=="subtract":
# 		sum2=number_x - number_y
# 		print(sum2)
# 	elif operation=="multipication":
# 		sum3=number_x * number_y
# 		print(sum3)
# 	else:
# 		sum4=number_x / number_y
# 		print(sum4)	
# calculator(number_x,number_y,operation)	
# calculator(number_x,number_y,operation)
# calculator(number_x,number_y,operation)
# calculator(number_x,number_y,operation)


# (PART 3)

# def list_change():
# 	list1=[5, 10, 50, 20]
# 	list2=[2, 20, 3, 5]
# 	list3=[]
# 	index=0
# 	while index <len(list1):
# 		sum=0
# 		sum=list1[index]*list2[index]
# 		list3.append(sum)
# 		index=index+1
# 	print(list3)
# list_change()		
 # def say_hello_language(name, language):
#     if language == "hindi":
#         print ("Namaste ", name)
#         print ("Aap kaise ho?")
#     elif language == "punjabi":
#         print ("Sat sri akaal ", name)
#         print ("Tuhada ki haal hai?")
#     else:
#         print ("Hello ", name)
#         print ("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")

dic={"name":"swati","password":"2728"}

name = input(" Enter a name")
password=input("enter a password!")
def dict(name,password,dic):
	if name == dic["name"] and password == dic["password"]:
		return True
	else:
		return False 		
print(dict(name,password,dic))


		

