# (EXAMPLES OF NESTED FUNTIONS)
# 1)
# def f1():
#    s="i love navgurukul"
#    def f2():
#        print(s)
#    f2()

# f1()

# 2)
# def first_function():
#     s = 'I love India'
#     def second_function():
#    	 print(s)	 
#     second_function()
# first_function()

# ===================================================================================
# (NESTED IF QUESTIONS )

# (QUESTIONS 1)

# def eligible_for_vote():
# 	age=int(input("enter a age"))
# 	if age<18:
# 		print("not eligible")	
# 	else:
# 		print("you are eligible")
# eligible_for_vote()			


# (QUESTIONS 2)

# def  perfect() 

# QUESTIONS 3

# def count():
# 	num1=int(input("enter a first numbers"))
# 	num2=int(input("enter a second numbers"))
# 	num3=int(input("enter a third numbers"))
# 	sum=0
# 	avarge=0
# 	sum=num1+num2+num3
# 	print(sum)
# 	avarge=sum/3
# 	print(avarge)
# count()	

# QUESTIONS 4

# def showNumbers():
# 	index=0
# 	num=int(input("enter a numbers"))
# 	while index<(num):
# 		if index%2==0:
# 			print(index,"Even")
# 		else:
# 			print(index,"odd")
# 		index=index+1
# showNumbers()			

# (QUESTIONS 5)

# def multiples():
# 	i=0
# 	sum=0
# 	num=int(input("enter a numbers"))
# 	while i<=num:
# 		if i%3==0 or i%5==0:
# 			print(i)
# 			sum=sum+i
# 		i=i+1
# 	print(sum)
# multiples()		

# QUESTIONS 6

# def drivers_ki_speed(speed):
# 	score=speed-70
# 	point=score//5
# 	if point<12:
# 		return point,"License suspended"
# 	if speed<70:
# 		return "ok"
# 	if speed<70:
# 		return ("total points",point,"above 70 speed")
# speed=int(input("enter a numbers:-"))
# print(drivers_ki_speed(speed))		

# QUESTION 7

# def word():
# 	name1=input("Enter a string value")
# 	name2=input("Enter a string value")
# 	if len(name1)<len(name2):
# 		print(name2)
# 	elif len(name1)==len(name2):
# 		print("both length are same",name1,name2)
# 	else:
# 		print(name1)
# word()				

# QUESTION 8 


# def squares(n):
# 	dic={ }
# 	for i in range(1,n+1):
# 		dic[i]=i*i
# 	return dic
# numbers=int(input("enter a numbers"))
# print(squares(numbers))