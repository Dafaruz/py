from art_week2 import hammer
print(hammer)

silent_bid_dict={}
other_bidders="yes"
def user_dictonary(user_name , user_bid):
    silent_bid_dict[user_name]=user_bid




while other_bidders=="yes":
    print("Welcome to the secret auction program,")
    user_name=input("what is your name:  ")
    user_bid=int(input("What's your bid: $"))
    user_dictonary(user_name , user_bid)
    other_bidders=input("Are there any other bidders? Type 'yes' or 'no'")
value=0
name=""
for bidder in silent_bid_dict:

    if value< silent_bid_dict[bidder]:
        value=silent_bid_dict[bidder]
        name =bidder
print(f"\n\nThe winner is {name} with a bid of ${value}")

