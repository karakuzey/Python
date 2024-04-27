height = int(input("what is your height : "))
price =0
if(height > 120):
    age = int(input("how old are you : "))
    if(age < 12):
        price += 5
    elif(age > 12 and age < 18):
        price += 7
    else:
        price += 12        
    photo = input("do you want photos ? yes or no : ")
    if(photo == "yes"):
        price += 3
else:
    print("you can try after a couple year")
    
print(f"total price : {price}")    
                