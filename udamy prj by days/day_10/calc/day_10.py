
from art_week2 import calc_logo
print(calc_logo)
exit=True
ac=""
def exit_calc(num1,num2):
    exit=False
    return 0
def clear(num1,num2):
    result=0
def  add (num1,num2):
    return num1+num2

def substract (num1,num2):
    return num1 - num2

def multiply (num1 , num2) :
    return num1 * num2

def divide (num1 , num2):
    return num1/num2
oprators={
    "+":add,
    "-":substract,
    "/":divide,
    "*":multiply,
    "ac":clear,
    "exit":exit_calc
}
while exit==True:
    print("pls chose from oprtaor: ")
    for oprator in oprators:
        print(oprator)

    user_oprator=input("what is yout oprator:\n")
    if user_oprator=="exit":
        user_function=oprators[user_oprator]
        result=user_function(0,0)
    num1=int(input("pls enter the first number:  "))
    num2=int(input("pls enter the second number:  "))

    user_function=oprators[user_oprator]
    result=user_function(num1,num2)

    print(f"{num1} {user_oprator} {num2} = {result}")
    ac=input(f"do you want to continuev with {result} 'n' for no and 'y' for yes")

 ######################################################################################
    while  ac=="y":

        if ac=="y":
            num1=result
        else:
            ac="n"
        num2=int(input("pls enter the number: "))
        for oprator in oprators:
            print(oprator)

        user_oprator=input("what is yout oprator")
        user_function=oprators[user_oprator]

        result=user_function(result,num2)
        print(f"{num1} {user_oprator} {num2} = {result}\n\n")
        ac=input(f"do you want to continuev with {result} 'n' for no and 'y' for yes")


########################################################################################################



