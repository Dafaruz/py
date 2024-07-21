from art_week2 import guess_a_number_logo
print(guess_a_number_logo)
import random
RUN=True
random_guess=random.randint(0,100)
print(random_guess)
def guess_a_num (life):
    print(f"Hi and welcome")
    while  life!=0:
        print(f" notice you got {life} life left")
        user_guess=int(input("pls chose your number:\n"))
        if user_guess==random_guess:
            return "yes"
        elif user_guess>random_guess:
            print("to high\n\n")
            life-=1
        elif user_guess<random_guess:
            print("to low\n\n")
            life-=1
    return "no"

while RUN==True:
    hardness=input("""hi there you are going to geuss a number between 1 to 100 
    pls chose you difuculty's hard or easy???  \n\n:
    """).lower()
    if hardness=='hard':
        is_won=guess_a_num(6)
        RUN=False
    elif hardness=='easy':
        is_won=guess_a_num(10)
        RUN=False
    else:
        print('check for typo')
if is_won=='yes':
    print("you won!!!!!!!!\n")
    print(f"the number was {random_guess} you ware right")
else:
    print("sorry you lose!!!!!!!")
    print(f"the number was {random_guess} you ware rong sorry")
