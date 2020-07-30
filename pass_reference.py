# question 1

# def numbers_less_than_twenty(list1):
# 	num_list_sub_20 =[]
# 	i=0
# 	while i <len(list1):
# 		if list1[i]<20:
# 			num_list_sub_20.append(list1[i])
# 		i=i+1
# 	return num_list_sub_20
# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
# num_list_sub_20 = numbers_less_than_twenty(num_list)
# print ("Initial list", num_list)
# print ("List that doesn't contain numbers greate than 20", num_list_sub_20)
# ==============================================================================================

# question 2  {rock paper scissors game}
	
# from random import randint

# def win():
#     print ('You win!')

# def lose():
#     print ('You lose!')

# while True:
#     player_choice = input('What do you pick? (rock, paper, scissors)')
#     # player_choice.strip()
#     random_move =randint(0, 2)
#     moves = ['rock', 'paper', 'scissors']
#     computer_choice = moves[random_move]
#     print(computer_choice,":this is computer_choice which is taken randomly")
#     if player_choice == computer_choice:
#     	print ('Draw!')
#     elif player_choice == 'rock' and computer_choice == 'scissors':
#     	print (player_choice,"win")
#     elif player_choice  == 'paper' and computer_choice == 'scissors':
#         print(player_choice,"lose")
#     elif player_choice == 'scissors' and computer_choice == 'paper':
#         print(player_choice,"win")
    # elif player_choice == 'scissors' and computer_choice == 'rock':
    #     print(player_choice,"lose")
    # elif player_choice == 'paper' and computer_choice == 'rock':
    #     print(player_choice,"win")
    # elif player_choice == 'rock' and computer_choice == 'paper':
    #     print(player_choice,"lose")
    # else:
    # 	print("not valid")
    # again = input('Do you want to play again? (y or n)')
    # if again == 'y':
    # 	continue
    # else:	
    # 	break

# =====================================================================================

# Cipher wheel with a function for finding an element in a list

# # find_in_list function defined here but not called
# def find_in_list(query, mainlist):
# # this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None
#     mainlist_len = len(query)
#     range_for_loop = range(mainlist_len)
#     index = None
#     for i in range_for_loop:
#         element = mainlist[i]
#         if element == query:
#             index = i
#     return i
# # this should return the position of the "query" in the "mainlist"


# chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# # encrypt_message function defined here but not called
# def encrypt_message(plain_msg):
# # this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
#     encrypted_msg = ""
#     for character in encrypted_msg:
#       # for character in msg
#         if character in chars:
#             char_index = find_in_list(character, chars)
#             new_char = shifted_chars[char_index]
#             encrypted_msg = encrypted_msg + new_char
#         else:
#             encrypted_msg = encrypted_msg + character

# # decrypt_message function defined here but not called
# def decrypt_message(encrypted_msg):
# # this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
#     decrypted_msg = ""
#     for character in decrypted_msg:
#         if character in shifted_chars:
#             char_index = find_in_list(character, shifted_chars)
#             new_char = chars[char_index]
#             decrypted_msg = decrypted_msg + new_char
#         else:
#             decrypted_msg = decrypted_msg + character


# # methods should return or print the new messages.
# ############################################### Code starts from here ##################################################
# flag = True
# while flag == True:
# 	choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
# 	if choice == 'e':
# 	    plain_message = input("Enter message to encrypt??")
# 	    encrypt_message(plain_message)
# 	elif choice == 'd':
# 		encrypted_msg = input("Enter message to decrypt?")
# 		decrypt_message(encrypted_msg)
# 	else:
# 		play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
# 		if play_again == 'Y':
# 			continue
# 		else:
# 			break

# ==================================================================================

# FIGHT THE ALIEN

from random import randint # allows you to generate a random number

# variables for the alien
alive = True
stamina = 10

# this function runs each time you attack the alien
def report(stamin):
# syntactic error in if else statements
    if stamina > 8:
        print ("The alien is strong! It resists your pathetic attack!")
    elif stamina > 5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamina > 3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamina > 0:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")

# main function - accepts your input for fight with the alien/
def fight(stam): # stamina
    while stam < 0:
      # won't enter this loop ever. The function will always return False.
        response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run")
        # chose a response from ( hit, attack, fight and run)
        # fight scene
        if "hit" in response or "attack" in response:
            less = randint(0, stam)
            stam = stamina-less # subtract random int from stamina
            report(stam) # see function above
        elif "fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
            return True
    # return False

print ("A threatening alien wants to fight you!\n")
# quotes at the end.

# call the function - what it returns will be the value of alive
alive = fight(stamina)

if alive: # means if alive == True
    print ("\nThe alien lives on, and you, sadly, do not.\n")
else:
    print ("\nThe alien has been vanquished. Good work!\n")



