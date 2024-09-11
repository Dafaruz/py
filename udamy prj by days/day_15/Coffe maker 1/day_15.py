from dicitonary_week_3 import coffe_manu , resources
user_input="on"
################################
#   check resurech function   #
################################


def check_for_resources(type):

    if type in ["cappuccino","latte","espresso"]:
        for resource in coffe_manu[type]["ingredients"]:
            print(resource + '  quantity:  ' + str(coffe_manu[type]["ingredients"][resource]))
            if coffe_manu[type]["ingredients"][resource]>resources[resource]:
                print(f"not anoff resource of {resource}")
                i="no"
            else:
                i="yes"
        return i
    elif type=="resource":
        for resource in resources:
            print(resource+  "  quantity:  " + str(resources[resource]))
        return
    elif type=="add" :
        O=1
    else:
        return

###############################################################################
#                            function for the mony calc                       #
###############################################################################

def change_calc(user_input):
    print("we have the anoff resources for your drink \n\n")
    print("pls insert coins")
    pennis=int(input("how many pennis:  $"))
    nickles=int(input("how many nickles:  $"))
    dimes=int(input("how many dimes:  $"))
    quaarters=int(input("how many quaarters:  $"))
    value_of_pennis=0.01*pennis
    value_of_nickles=0.05*nickles
    value_of_dimes=0.1*dimes
    value_of_quaarters=0.25*quaarters
    charge=coffe_manu[user_input]["cost"]
    sum=value_of_pennis+value_of_nickles+value_of_dimes+value_of_quaarters
    if charge<=sum:
        change=sum-charge
        return change
    else:
        return 0




###############################################################################
#                              the making progress                            #
###############################################################################
def make_the_drink(user_input):
    for resource in coffe_manu[user_input]["ingredients"]:
        resources[resource]-=coffe_manu[user_input]["ingredients"][resource]

    resources["monny"]+=coffe_manu[user_input]["cost"]
    return















def coffe_mechine_func():
    global user_input
    while not user_input=="off":
        print("What would you like? (espresso/latte/cappuccino):\n\n")
        user_input=input()
        if not user_input=="off":
            if not "monny" in resources:
                resources["monny"]=0
            do_we_have_resources=check_for_resources(user_input)

        if user_input=="off":
            return
        if  do_we_have_resources=="yes":
            change=change_calc(user_input)
            if change==0:
                print("not enoff monny inserted sorry here is your monny pls go agian\n")
            else:
                make_the_drink(user_input)
                print("your drink is ready")
                print(f"your change is {change}")
                print(resources["monny"])

coffe_mechine_func()
