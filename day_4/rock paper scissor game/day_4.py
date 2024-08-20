import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''2
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

r_p_c=[rock,paper,scissors]
pc_hand=random.randint(0,2)
user_hand=int(input("what do you choose? type 0 for Rock, 1 for paper or 2 or scissors\n\n:"))

print(r_p_c[user_hand])

print(f"pc chose:\n\n {r_p_c[pc_hand]}")
if (pc_hand==0 and user_hand==1) or (pc_hand==2 and user_hand==0) or(pc_hand==1 and user_hand==2):
    print("You Won")
elif (pc_hand==1 and user_hand==0) or (pc_hand==0 and user_hand==2) or(pc_hand==2 and user_hand==1):
    print("You Lose")
else:
    print("It's a draw")


