# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

import pandas as pd

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)

# print(type(data["temp"]))

# monday = data[data.day == "Monday"]
# monday_temp_C = monday.temp[0]
# monday_temp_F = monday_temp_C * 9/5 + 32
# print(monday_temp_F)


# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "Scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("data_dict")


# data = pd.read_csv("weather_data.csv")
# print(data)
# temperatures = data.temp
# print(temperatures)
# temp_higher_than_15 = 0
# for temp in temperatures:
#     if temp > 15:
#         temp_higher_than_15 += 1

# print(temp_higher_than_15)


squirrel_data = pd.read_csv(
    "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250821.csv")
gray_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_fur, red_fur, black_fur]
}

squirrel_count = pd.DataFrame(squirrel_dict)
squirrel_count.to_csv("squirrel_count.csv")

print(type(squirrel_data["Primary Fur Color"] == "Gray"))
