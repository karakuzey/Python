numbers = [1,2,3,4,5,6]
print(numbers[1])
print(numbers[2])
# -ile başladığında tersten ilerliyoruz ama bu sefer 0 yok
print(numbers[-1])

numbers.append(999)
# listenin sonuna ekleme
print(numbers)

# insert belirlenen konuma veri girişi yapan bir sistem 

numbers.insert(1,888)
print(numbers)

numbers.remove(1)
print(numbers)

# insert te istenene konuma ekleme yapılırken remove da istenen veri aranıyor ilk bulunan siliniyor
numbers.remove(888)
print(numbers)

# queue gibi default ta listenin sonunda olan veriyi silip döndürüyor istersen index te verebilirsin
# hem popta sayı girmez ve append kullanrısan stack oluyor
print(numbers.pop())
 
# print( numbers.count(5))  belirtilen itemin listede kaç kez bulunduğunu gösterir
