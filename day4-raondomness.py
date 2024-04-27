import random
randomInteger = random.randint(1,3)
print  (f"{randomInteger} \n")
randomFloat = random.random() # 0 la bir arasında rasgele bir sayı üretiyor ama 1 dahil değil
print(randomFloat)

# bunu 1-n arasında yapmak için
randomFloat = int(randomFloat * 10) + 1

print(f"\n {randomFloat}")