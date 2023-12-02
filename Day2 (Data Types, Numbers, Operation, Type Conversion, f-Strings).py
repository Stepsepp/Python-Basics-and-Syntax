# Data Types

# See Pythoni kood prindib sõna "Hello" esimese tähemärgi, kuna sõned on indekseeritavad ja indeksid algavad nullist. Seega, "Hello"[0] väljastab "H"
print("Hello"[0])
# Nüüd proovime printida o tähe selleks et seda teha ja selles teame et H = 0 E = 1 jne 
print("Hello"[4])

#Integer-  Kui viitate sõna "Integer" kasutamisele Pythonis, siis see viitab täisarvude andmetüübile. Pythonis on täisarvud tähistatud tüübiga int.
print(123 + 345)

# Float Sõna "Float" kasutatakse Pythonis täisarvude (integer) vastandina ujukomaarvude
#  (float) tähistamiseks. Ujukomaarv on arv, mis sisaldab komakohta või kasutab teaduslikku märki (näiteks 3.14 või 2.0e-5).
3.14159

# Boolean- Booleani (bool) andmetüüp Pythonis esindab kahte väärtust: True (tõene) ja False (väär).
# See on kasulik tüüp, eriti tingimuslauseid (if-else laused) ja loogilisi operatsioone tehes.
True
False

# Antud koodis  küsime  kasutajalt nime, arvutab nime pikkuse ja prindib välja sõnumi, mis ütleb, mitu tähte nimes on.
num_char = len(input("Mis on sinu nimi?"))
print(type(num_char)) 
new_num_char = str(num_char)
print("Sinu nimes on " + new_num_char + " tähte.")

a = str(123)
print(type(a))

3 + 5
7 - 3
3 * 2
2 ** 3

#PEMDASLR
#()
#**
#*
#/
#+
# -
#print(3 * 3 + 3 / 3 3 - 3)

# f-String - on Pythoni süntaksivariant, mis võimaldab mugavalt ja loetavalt sisestada muutujate väärtusi stringidesse.
#  See on saadaval alates Python 3.6 versioonist.
# f-string kasutamiseks lisatakse f- või F-tähis stringi ette,
#  ja muutujad lisatakse sulgudesse {} sisse. Seejärel asendatakse need sulgudes olevad muutujad nende väärtustega.

score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


# Proovime hakata kirjutama scripti mis annab sulle teada kui palju tipi sa pead teenindajale jätma kui soovite selle teatud inimeste vahel ära jagada.
# Kui arve on 150 eur ja soovite selle jagada 5 inimese vahel, andes 12% tippi.
# Iga inimene peaks maksma (150.00 / 5) * 1.12

print("Tere tulemast arvutama tippi")
arve = float(input("Mis on arve summa €"))
tip = int(input("Kui palju tippi sa soovid anda ? 10,12, või 15?"))
inimesed = int(input("Kui palju inimeste vahel tuleb jagada"))
tippTuleksJätta = tip / 100 * arve + arve 
print(tippTuleksJätta)
