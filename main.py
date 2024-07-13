#data = []
#with open("weather_data.csv") as file:
#    rows = file.readlines()
#    for row in rows:
#        data.append(row.split("\n"))

#print(data)
# this way is a bit paintful there is an easier way
#import csv

#temperatures = []

# with open("weather_data.csv") as file:
#    rows = csv.reader(file)
#    counter = 0
#    for row in rows:
#        if counter != 0:
#            temperature = int(row[1])
#            temperatures.append(temperature)
#        counter += 1
#    print(temperatures)

# thats another way of takin tempraetues

import pandas
# thats an awsome libary has two type of data dataframe and series methods are below
data = pandas.read_csv("weather_data.csv")
# print(data)
# after the next line its more then just awsome

# data = data["temp"]
# print(data)
# for i in data:
#     print(i)

# there is even easier way to that first how to convert csw to a dictionary

# data_dictionary = data.to_dict()
# print(data_dictionary)
#
# # now how to take a column as a series just easy as possible its name is series
#
# temperatures = data["temp"].to_list()
# print(temperatures)
# print(f"{sum(temperatures) / len(temperatures)}")
# # build in function for average just name is different
# print(data["temp"].mean())
# print(data["temp"].max())
# print(max(temperatures))
#
# # against to use data[""] form
#
# print(data.condition)
# print(data["condition"])

# how we read a row of a table

# print(data[data.day == "Monday"])


day = data[data.temp == data.temp.max()].day
print(day)

max_temp = data.temp.max()
print(max_temp)

monday = data[data.day == "Monday"]
print(f"day :  {monday.day} , temperature : {monday.temp}")


# using pandas lbary to create a dataframe

students_data = {
    "students" : ["ali","veli","mehmet"],
    "scores" : [99,98,97]
}

students_infos = pandas.DataFrame(students_data)

print(students_infos)

# creating csv files

# students_infos.to_csv("student_infos.csv")


# the days temp = 14

fourteen = data[data.temp == 14]
print(fourteen)

max_temp = data[data.temp == data.temp.max()].day
print(max_temp)
