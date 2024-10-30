
my_list = range(0, 11)   # the range list
print(list(my_list))
index = len(my_list)/2
max1 = len(my_list)-1
min1 = 0

random_float = 10

while index != random_float:
    if index > random_float:
        max1 = index
        index = index - (max1-min1)/2
        print(f"1the index is {index} the value is {index}")
    elif index < random_float:
        min1 = index
        index = index + (max1-min1)/2
        print(f"2the index is {index} the value is {index}")

