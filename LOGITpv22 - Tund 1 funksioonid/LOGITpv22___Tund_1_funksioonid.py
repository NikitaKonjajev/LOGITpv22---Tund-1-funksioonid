from math import * #*-kõik funktsioonid on vaja kasutada. kasutema: sen()
#import math kasutame: math.sin()
#2.osa Math kasutamine 
print("Ristkülik ja ringi pindalad")
a=float(input("Anna laius: "))
b=float(input("Anna kõrgus: "))
S=a*b #+,-,/,*,**, sqrt(),//,%
d=sqrt(a**2+b**2)
r=float(input("Anna raadius: "))
Skr=pi*r**2
print(f"Ristkülik pindala on {S}. Ringi pindala on {round(Skr,2)}.")

      




#1. osa print(), input(), int(), float()
print ("Tere tulemast!") #print() teksti või andmete väljastuseks
nimi=input("Mis on sinu nimi? ")#Sisendi lugemine "..." ja oota , kuni kasutaja vajutab Enter klahvi
# input () -> str
print(f"{nimi}, sul on väga ilus nimi!") 
print(nimi,", sul on väga ilus nimi!") #kui on sarnane andmete tüübib
print(nimi+", sul on väga ilus nimi!") #kui on sarnane andmete tüüp
vanus=int(input("kui vana sa oled?")) # input()->int
print(f"{nimi} Jarmisel aastal saad {vanus+1}") #muutja vanus ei muuda
print ("aga selle aastal on ", vanus)
vanus+=1 #muudame muutuja väärtus
print(f"Järgmine aasta on käes, siis {nimi} on {vanus} aastat vana")
pikkus=float(input("Mis on sinu pikkus")) #input()->float: 1.75
print(f"{nimi} on {vanus} aastat vana ja suurepärase pikkusega {pikkus}")
