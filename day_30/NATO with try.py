
import pandas
flag = 1
nato = pandas.read_csv("nato_phonetic_alphabet.csv")  # create a data frame
nato_dict = {value.letter: value.code for (index, value) in nato.iterrows()}

user_input = input("enter your name to get it in nato phonetic \n:")
user_list = [word for word in user_input.upper()]


while flag == 1:
    try:
        user_input = input("enter your name to get it in nato phonetic \n:")
        user_list = [word for word in user_input.upper()]
        user_nato_name = [nato_dict[word] for word in user_list]  # tap dic in a key value and iterate  with the user list
        print(user_nato_name)
        flag = 0
    except KeyError:
        print('only letters pls')
        flag = 1

