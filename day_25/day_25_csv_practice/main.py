#
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)


import pandas


#data = pandas.read_csv("weather_data.csv") #use pandas to read csv        #cmd to read the csv file

# # print(data)
# temp =data.temp    # get series of the temp
# dict =data.to_dict()  # transfer data to dictionary
# print(dict)
#
# list=data.temp.to_list()
# print( sum(list)//len(list))
#
# z=data.temp.max()
# print(z)
# print(data[data.temp == data.temp.max()])
#Get data in row:
# monday_temp=data[data.day == "Monday"]
#
# fer=monday_temp.temp[0]*9/5 +32 #transfer to fer
# print(fer)

#Some refresh on dic and key values :

# data_dict ={
#      "student": ["daniel", "david", "nastia", ],
#      "scores": [75,80,90]
# }
# for key in data_dict["student"]:
#     data_dict["student"].index(key)
#     print(f"the score of {key} is : {data_dict["scores"][data_dict["student"].index(key)]}")


#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")
#print(data)






