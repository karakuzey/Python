bill = float(input("what is the total bill :"))

tip = int(input("how much tip would you like to give : 10,12,15 :"))

numPeople = int(input("how many people will split the bill : "))

result = bill + bill* (tip/100)

print(f"total price for one person : " + str(result / numPeople) + "$")