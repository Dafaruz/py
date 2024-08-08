import pandas
gray = 0
black = 0
cinnamon = 0
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"]

for color in fur_color:
    if color == "Gray":
        gray += 1

    if color == "Black":
        black += 1
    if color == "Cinnamon":
        cinnamon += 1

fur_count_gray = len(data[data["Primary Fur Color"] == "Gray"])
fur_count_Black = len(data[data["Primary Fur Color"] == "Black"])
fur_count_Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

lists = {

    "color": ["Gray", "Black", "Cinnamon"],
    "count1": [fur_count_gray, fur_count_Black, fur_count_Cinnamon],
    "count2" :[gray, black, cinnamon]
}

data=pandas.DataFrame(lists)
data.to_csv("data.csv")
print(data)