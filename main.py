import random 
#since we make random module, we need to write import random in the beginning

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images=[rock,paper,scissors] #to create list of images
user_choice=int(input("What do you choose? Type 0 for rock,1 for paper and 2 for scissors\n ")) 
#user choice with numbers ,thats why we use integer

if user_choice>=3 or user_choice< 0: #to prevent error when we enter invalid number
   print("You entered invalid number,Game Over!")
else: #when user choose a number that will show the above images with below code:
   print(game_images[user_choice])

   computer_choice=random.randint(0,2) #limit of numbers that com will choose
   print("Computer chose")
   print(game_images[computer_choice]) #when comp choose a number that will show the above images with this code


   if user_choice==0 and computer_choice==2:
    print("You Win")
   elif computer_choice==0 and user_choice==2:
    print("You Lose")
   elif computer_choice>user_choice:
    print("You Lose")
   elif user_choice>computer_choice:
    print("You Win")
   elif user_choice==computer_choice:
    print("It is a Draw")



