import pandas
data = pandas.read_csv("central_park.csv")
# my task create a csv file wich includes color and how many of them gray , black , Cinnamon
gray = data[data["Primary Fur Color"] == "Gray"]
number_of_gray = len(gray)
print(number_of_gray)

black = data[data["Primary Fur Color"] == "Black"]
number_of_black = len(black)
print(number_of_black)

Cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
number_of_Cinnamon = len(Cinnamon)
print(number_of_Cinnamon)

central_info = {
    "color" : ["Gray", "Black", "Cinnamon"],
    "count" : [number_of_gray,number_of_black,number_of_Cinnamon]
}

central_park_data = pandas.DataFrame(central_info)
central_park_data.to_csv("central_park_data.csv")