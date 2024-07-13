import pandas
import turtle
import time


screen = turtle.Screen()
screen.title("US states game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


city_infos = pandas.read_csv("50_states.csv")
city_names = city_infos["state"].to_list()
print(city_names)

game_is_on = True


def create_and_send_city(city, x, y):
    city_place = turtle.Turtle()
    city_place.hideturtle()
    city_place.penup()
    city_place.goto(x, y)
    city_place.write(city, align="center", font=("Courier", 8, "normal"))


while game_is_on:
    city_name = shape = screen.textinput("Şekil Girişi", "wich city do you wanna try if you wanna quit \n"
                                                         "type s : ")
    if city_name in city_names:
        cor_x = city_infos[city_infos.state == city_name].x.iloc[0]
        # becasue of cor_x is a pandas series we use iloc its the same thing with x[0} or x.iloc[0]
        # just because of its a part of pandas libary we use it
        print(cor_x)
        cor_y = city_infos[city_infos.state == city_name].y.iloc[0]
        print(cor_y)
        create_and_send_city(city_name, cor_x, cor_y)
        time.sleep(2)

    if city_name == "s":
        game_is_on = False

screen.exitonclick()
