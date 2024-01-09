# Õpime täna if ja else 
# if - on Pythoni võtmesõna, mida kasutatakse tingimuslause algatamiseks.
# Tingimuslaused aitavad programmeerijatel teha otsuseid ja kontrollida, milliseid tegevusi programm peaks sooritama sõltuvalt antud tingimustest.
# else -  on võtmesõna Pythonis, mida kasutatakse koos if-lausega, et määratleda koodiblokk, mis käivitub siis, kui antud tingimus if-lause juures on väär (False).
# Näidis ülesanne

print("Tere tulemast ameerikamäele")
Pikkus = int(input("Mis on sinu pikkus cm?")) # int(input()) kombinatsioon Pythonis kasutatakse selleks, et saada kasutajalt sisendit, mis on täisarv (integer).

if Pikkus > 120:
   print("Sa võid minna!")
else:
   print("Kahjuks pead kasvama pikemaks!!")

   # Kui me tahame et ka 120 cm pikkused inimesed läheksid arvesse tuleb teha muudatus, tuleb märkida ka võrdus märk if Pikkus >= 120:

print("Tere tulemast ameerikamäele")
Pikkus = int(input("Mis on sinu pikkus cm?")) # int(input()) kombinatsioon Pythonis kasutatakse selleks, et saada kasutajalt sisendit, mis on täisarv (integer).
if Pikkus >= 120:
   print("Sa võid minna!")
else:
   print("Kahjuks pead kasvama pikemaks!!")

   # Operator and Meaning

   # > Greater than 
   # < Less than
   # >= Greater than or equal to
   # <= Less than or egual to
   

   print("Tere tulemast ameerikamäele")
Pikkus = int(input("Mis on sinu pikkus cm?")) # int(input()) kombinatsioon Pythonis kasutatakse selleks, et saada kasutajalt sisendit, mis on täisarv (integer).

# Antud koodis mes küsime lisaks pikkusele ka vanust, kui pikkus on lubatud, alles siis küsib script vanust ja ütleb pileti maksumuse
if Pikkus >= 120:
   print("Sa võid minna!")
   vanus = int(input("Mis on inu vanus?"))
   if vanus <= 18:
      print("Pilet maksab 7 eurot.")
   else:
    print("Pilet maksab 12 eurot")     
else:
   print("Kahjuks pead kasvama pikemaks!!")

# Antud koodis me lisame ka elif variandi, mille abil saab määrata täiendavaid tingimusi just nii palju kui vaja.
   print("Tere tulemast ameerikamäele")
Pikkus = int(input("Mis on sinu pikkus cm?")) # int(input()) kombinatsioon Pythonis kasutatakse selleks, et saada kasutajalt sisendit, mis on täisarv (integer).
if Pikkus >= 120:
   print("Sa võid minna!")
   vanus = int(input("Mis on inu vanus?"))
   if vanus < 12:
      print("Pilet maksab 5 eurot")
   elif  vanus <= 18:  
      print("Pilet maksab 7 eurot.")
   else:
    print("Pilet maksab 12 eurot")     
else:
   print("Kahjuks pead kasvama pikemaks!!")

   # elif (lühend "else if") on veel üks võtmesõna Pythonis, mida kasutatakse koos if-lausega, et määratleda täiendavaid tingimusi.
   # See võimaldab teha järjestikuseid tingimuskontrolli blokke.

   # Antud koodis me küsime ka inimeselt kas ta soovib ka pilti osta ja paneme paika foto hinna ja ka matemaatilise tehte mis selle kohe juurde rehkendab.

   # Tervitus
print("Tere tulemast ameerikamäele")

# Küsi kasutajalt pikkust
Pikkus = int(input("Mis on sinu pikkus cm?"))

# Kontrolli kas kasutaja saab minna mäele
if Pikkus >= 120:
    print("Sa võid minna!")
    # Küsi kasutajalt vanust
    vanus = int(input("Mis on sinu vanus?"))
    # Määra arve nulliks
    Arve = 0  
    # Kontrolli vanuse põhjal
    if vanus < 12:
        Arve = 5
        print("Lapse Pilet maksab 5 eurot")
    elif 12 <= vanus <= 18:
        Arve = 7
        print("Nooruki pilet maksab 7 eurot.")
    else:
        Arve = 12
        print("Täispilet maksab 12 eurot")
    # Küsi kasutajalt, kas nad soovivad osta pilti
    Pildi_Soov = input("Kas sa soovid ka pilti osta? Jah või Ei. ")
    # Lisa pildi hinna arvele, kui vastus on "Jah"
    if Pildi_Soov.lower() == "jah":  
        Arve += 3
    # Prindi välja arve
    print(f"Sinu arve on {Arve}")
else:
    print("Kahjuks pead kasvama pikemaks!!")
