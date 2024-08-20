from art_week_3 import hi_or_low_logo , vs_logo
from dicitonary_week_3 import hi_or_low_dictonary
import random
user_is_right=True
good_guess=0
first_contestent=random.choice(hi_or_low_dictonary)          ## now this is a person with dictonary
first_contestent_index=hi_or_low_dictonary.index(first_contestent)  # get the person index in the list
second_contestent=random.choice(hi_or_low_dictonary)
second_contestent_index=hi_or_low_dictonary.index(second_contestent)
print(hi_or_low_logo)
while user_is_right:
    print("")
    print(f"Compare A: {first_contestent['name']}, {first_contestent['description']} from {first_contestent['country']}")
    print(vs_logo)
    print("")
    print(f"Compare B: {second_contestent['name']}, {second_contestent['description']} from {second_contestent['country']}")
    user_chose=input().lower()
    flowers_count_a=first_contestent['follower_count']
    flowers_count_b=second_contestent['follower_count']
    if (flowers_count_a > flowers_count_b) and (user_chose=='a'):
        print("yow ware right")
        good_guess+=1
        first_contestent=hi_or_low_dictonary[first_contestent_index]
        second_contestent=random.choice(hi_or_low_dictonary)
    elif (flowers_count_a < flowers_count_b) and (user_chose=='a'):
        print("you ware wrong ")
        break
    elif flowers_count_a > flowers_count_b and user_chose=='b':
        print("you ware wrong")
        break
    else:
        print("yow ware right")
        good_guess+=1
        second_contestent=first_contestent
        second_contestent=random.choice(hi_or_low_dictonary)


print(f" nice try you score is :{good_guess}")
