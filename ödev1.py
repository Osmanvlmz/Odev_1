'''
Veri tipleri arasında dönüşümler
'''

# İntegerdan float ve stringe

x = 26

print(float(x))

print(str(x))

# Floattan integer ve stringe

y = 36.4

print(int(y))

print(str(y))

# Stringden İnteger ve floata

z = "16"

print(int(z))

print(float(z))



'''
Yaş atanmış 3 değişkenin birbiri aralarında karşılaştırılması
'''

Ali = 20
Mustafa = 25
Cem = 22

print(Ali > Mustafa)
# -> False

print(Cem < Mustafa) 
# -> True

print(Cem >= Ali)
# -> True

print(Mustafa <= Ali)
# -> False

print(Cem != Cem)
# -> False

print(Cem > Ali and Cem < Mustafa)
# ->True

print(Ali >= Mustafa and Cem >= Ali)
# -> False

print(Ali == Cem or Cem > Ali)
# -> True

print(Mustafa == Ali or Cem < Ali)
# -> False



'''
4 işlem
'''

print("Birinci değeri girin")
x = input()

print("İkinci değeri girin")
y = input()

print("Yapmak istediğiniz işlemi seçin. Toplama için '+' tuşuna, Çıkarma için '-' tuşuna, Çarpma için '×' tuşuna, Bölme için '÷' tuşuna basınız.")
işlem = input()

if işlem == "+" :
    print(int(x) + int(y))

elif işlem == "-" :
    print(int(x) - int(y))

elif işlem == "*" :
    print(int(x) * int(y))

elif işlem == "/" :
    print(int(x) / int(y))

else : 
    print("Girdiğiniz değerler sayı değil veya işlem için yanlış tuşa bastınız")



'''
Kullanıcıdan isim, yaş, şehir ve meslek bilgilerini istenir ve cevaplarını yazdırılır
'''

print("Adınızı giriniz.")
isim = input()

print("Yaşınızı giriniz.")
yaş = int(input())

print("yaşadığınız şehri giriniz.")
şehir = input()

print("Mesleğinizi giriniz")
meslek = input()

print(isim + " " + str(yaş) + " " + şehir + " " + meslek)



'''
"Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlama
'''
HK= "Hi-Kod Veri Bilimi Atölyesi"
 
print(HK.split(" "))

print(HK.upper())

print(HK.lower())



'''
0123456789 sayısındaki tek ve çift sayları yazdırma
'''

x = "0123456789"

print(x[::2]) #çift sayıları yazdırmak için

print(x[1::2]) #tek sayıları yazdırmak için