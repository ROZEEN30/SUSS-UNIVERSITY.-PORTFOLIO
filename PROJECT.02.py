import random


is_running= True
while is_running:
 options=("rock","paper","scissors")
 player_choice=None
 computer= random.choice(options)

 while player_choice not in options:
   player_choice=input("enter a choice from rock/ paper/ scissors:")

   print(f"person: {player_choice}")
   print(f"computer: {computer}")
   if player_choice=="paper" and computer=="rock":
    print("YOU WIN!")
   elif player_choice=="rocks" and computer=="scissors":
    print("YOU WIN!")
   elif player_choice=="scissors" and computer=="paper":
    print("YOU WIN!")
   else:
     print("YOU LOST!")
     play_again= input("play again (y/n :)?")
     if play_again=="n":
      is_running=False











