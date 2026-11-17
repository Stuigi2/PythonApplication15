#try:
#    t=float(input("Mis temp on nahhui"))
#    if t>18:
#        print("See on soovitatav toasoojus")
#    elif t<18:
#        print("Liiga kylm nahhui")


#except ValueError:
#    print("Viga")

#try:
#    pikk = int(input("Sisesta enda pikkus CM"))
#    if pikk < 199:
#        print("Luhike rott")
#    elif pikk >= 200:
#        print("Oled pikka alpha chud sigma")
#    else:
#        print("Oled keskmine vmdagi")
#
#except ValueError:
#    print("Viga")

#sugu = input("Sugu:")
#if sugu.lower()=="m" or sugu.lower()=="mees":
#    try:
#        pikk = int(input("Sisesta enda pikkus CM"))
#        if pikk < 199:
#            print("Luhike rott")
#        elif pikk >= 200:
#            print("Oled pikka alpha chud sigma")
#        else:
            #print("Oled keskmine vmdagi")

    #except ValueError:
#        print("Viga")
#elif sugu.lower()=="n" or sugu.lower()=="naine":
##    try:
#        pikk = int(input("Sisesta enda pikkus CM"))
#        if pikk < 199:
#            print("Luhike rott")
#        elif pikk >= 200:
#            print("Oled pikka alpha chud sigma")
#        else:
#            print("Oled keskmine vmdagi")

#    except ValueError:
#        print("Viga")
from random import *

Vana = ["kana", "Piim", "leib", "sai", "muna"]
ostukorv = {}

while len(Vana) > 0:
    toode = Vana.pop()
    hind = randint(1, 5)
    print("Kas sa soovid osta:", toode)
    vastus = input("Yes/No: ")
    if vastus == "Yes":
        kogus = int(input("Mitu? "))
        Panaks = input(f"Hind tuleb: {hind * kogus}. Kas soovid jatkata? ")
        if Panaks == "Yes":
            ostukorv[toode] = kogus
        elif Panaks == "No":
            continue

print("Sinu ostukorv:", ostukorv)