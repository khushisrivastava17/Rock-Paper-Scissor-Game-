
import random as rd
print("---WELCOME TO THE GAME---")

choice=["rock","paper","scissor"]
user_score=0
c_score=0

while True:
 user=input("Select one: Rock/Paper/Scissor(or q to quit):  ").lower()

 if user=="q":
    print("Thankyou for playing!")
    break
 if user not in choice:
    print("Invalid! Try Again")
    continue
 
 c_guess= rd.choice(["rock","paper","scissor"]).lower()
 print(c_guess)
 
 if user==c_guess:
    print("Its a tie!!")
 elif( user=="paper" and c_guess=="rock")or(user=="scissor" and c_guess=="paper") or (user=="rock"and c_guess=="scissor"):
    user_score+=1
    print("User Wins! ")
   
 else:
    c_score+=1
    print("Computer wins!")

 print(f"User score: {user_score}|Computer score: {c_score}")
    
