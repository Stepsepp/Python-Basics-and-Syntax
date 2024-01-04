                                                    # For & While Loops

# Loops (silmustest) on programmeerimiskontseptsioon, mis võimaldab koodil korduvalt täita teatud plokki või käsku.
# Loops võimaldab automatiseerida korduvaid ülesandeid ja vähendada koodi kordamist. 
# Programmeerimiskeeltes on kaks peamist tüüpi Loops: for ja while.
# for-Loops: See Loops töötab kindlaksmääratud arvu kordi, sõltuvalt itereeritavast objektist (nt nimekiri, sõne või hulk).

# Koodiblokk, mis kordub iga itereeritava elemendi jaoks
for element in iterable:
# Selles näites prinditakse arvud 0 kuni 4.
for i in range(5):
    print(i)

# while-Loops: See  töötab seni, kuni antud tingimus on täidetud. while-Loops on järgmine üldine vorm:
    # Koodiblokk, mis kordub seni, kuni tingimus on täidetud
while condition:

# Selles näites prinditakse arvud 0 kuni 4, kuna count väärtust suurendatakse iga sammuga.
count = 0
while count < 5:
    print(count)
    count += 1

# Loops on olulised, kui soovite automatiseerida tegevusi, mis tuleb korrata, nagu andmete läbimine, nimekirjade või hulkade töötlemine,
# või seni, kuni teatud tingimused on täidetud. Loops aitavad ka muuta koodi loetavamaks ja lühemaks, kuna väldime koodi kordamist.


                                                # If / Else
    # if ja else on tingimuslausete konstruktsioonid programmeerimiskeeltes,
    # mis võimaldavad juhtida programmi käitumist sõltuvalt antud tingimustest. Siin on nende kasutamise üldine vorm:
    #if (kui) lause:
# Kasutatakse tingimuse esitamiseks. Kui tingimus on tõene (True), siis käivitatakse sellele järgnev koodiplokk.
# Kui tingimus on väär (False), siis koodiplokki ei käivitata.
x = 10
if x > 5:
    print("x on suurem kui 5")

# else (muidu) lause:
# Kasutatakse koos if lausega ja käivitatakse, kui if tingimus on väär (False).
# else lauset kasutatakse, et täpsustada, mida teha siis, kui if tingimus ei ole tõene.
x = 3
if x > 5:
    print("x on suurem kui 5")
else:
    print("x ei ole suurem kui 5")

    # elif (kui muidu) lause:

# Kasutatakse, et lisada täiendavaid tingimusi if ja else konstruktsiooni.
# Kui eelnevad tingimused on väär, kontrollitakse elif tingimusi.
x = 5
if x > 5:
    print("x on suurem kui 5")
elif x < 5:
    print("x on väiksem kui 5")
else:
    print("x on võrdne 5-ga")
# Need konstruktsioonid on fundamentaalsed programmeerimises ja võimaldavad programmeerijatel
# luua dünaamilisi ja tingimuslikke käitumismustreid oma koodis.



                                            #list     
# Listid (nimekirjad) on andmestruktuur, mis võimaldab hoida mitmeid väärtusi ühes muutujas.
# Listid on Pythoni programmeerimiskeeles olulised ja neid kasutatakse laialdaselt andmete hoidmiseks,
# töötlemiseks ja manipuleerimiseks. Listid on muudetavad, mis tähendab, et saate nende sisu programmi käivitamise ajal muuta.

# Listi saab luua, eraldades elemendid komadega ja sulgudes need kandiliste sulgudega.
minu_nimekiri = [1, 2, 3, "neli", 5.0]

#Listi indeksid:
#Listi elemendid on indekseeritud, st igal elemendil on oma asukoht listis. Pythonis algavad indeksid 0-st.
esimene_element = minu_nimekiri[0]  # Tagastab esimese elemendi (indeks 0)

#Listi pikkus:
#len() funktsioon võimaldab teil saada listi pikkust ehk elementide arvu.
pikkus = len(minu_nimekiri)  # Tagastab listi pikkuse

#Elementide muutmine:
#Listi elementide väärtusi saab muuta, põhinedes nende indeksitel.
minu_nimekiri[2] = "kolm"  # Muudab kolmanda elemendi väärtust

# Elementide lisamine:
# append() meetod võimaldab lisada uue elemendi listi lõppu.
minu_nimekiri.append("kuus")  # Lisab uue elemendi listi lõppu

# Elementide eemaldamine:
#remove() meetod võimaldab eemaldada konkreetse elemendi listist.
minu_nimekiri.remove("neli")  # Eemaldab konkreetse elemendi

# Listide ühendamine:
#Listide saab ühendada kasutades + operaatorit või extend() meetodit.
uus_nimekiri = minu_nimekiri + [7, 8, 9]  # Ühendab kaks listi

# Listi sirvimine (for-tsükliga):
# Listi elemente saab kergesti sirvida for-tsükli abil.
for element in minu_nimekiri:
    print(element)
#Listid on väga paindlikud ja neid kasutatakse laialdaselt andmete struktureerimiseks ning programmeerimisülesannete lahendamiseks.

                                                # Strings
    
# stringid (sõned) on teksti andmetüüp, mis võimaldab teil salvestada ja manipuleerida teksti,
# tähemärke ja sõnu programmeerimiskeeles. Pythonis on stringid esitatud jutumärkides, olgu need siis ühe- või kahekordsed. 
    
# Stringi pikkus:
# Saate teada stringi pikkuse, kasutades len() funktsiooni.
    pikkus = len(minu_string)

    
# Stringi formaatimine:

# Stringi saab formatseerida, asendades märgistatud kohad reaalsete väärtustega.
nimi = "Alice"
vanus = 25
formaatitud_string = f"Nimi: {nimi}, Vanus: {vanus}"

# stringi meetodid:
# Stringidel on mitmeid meetodeid, nagu näiteks upper(), lower(), strip(), split(), mis võimaldavad erinevaid toiminguid teha stringidega.
suured_t2hed = minu_string.upper()

                                                # Range

# range() on Pythoni sisseehitatud funktsioon, mis loob järjestiku (arvude jada) vastavalt määratletud algus-, lõpp- ja sammuparameetritele.
# See on kasulik, kui soovite luua järjestikuseid arve, näiteks tsüklites või loendites.

# range(algus, lõpp, samm)

# algus: Algusarv (vaikimisi 0, kui pole määratud).

# lõpp: Lõpparv (kui jõutakse sellele arvule, ei ole see arv järjestikus hulgas).
# samm: Samm (vaikimisi 1, kui pole määratud).
# range() funktsioon tagastab arvude jada, mis vastavad määratud tingimustele.
# See ei loo tegelikult listi, vaid on kohandatud andmestruktuur, mis võimaldab tõhusamat ressursikasutust.

for i in range(5):
    print(i)
Väljund
0
1
2
3
4

# range() tulemus listina:
arvude_list = list(range(5))
print(arvude_list)
Väljund
[0, 1, 2, 3, 4]


                                                    # Modules

# Pythoni moodulid on failid, mis sisaldavad Pythoni koodi ja mida saab teistes programmides taaskasutada.
# Need võimaldavad sul jagada koodi erinevate programmide või projektide vahel ning parandada koodi loetavust ja hooldatavust.

# Mooduli loomine:

# Saad luua oma mooduleid, kirjutades Pythoni koodi faili ja salvestades selle .py laiendiga.
# Näiteks kui sul on fail nimega minu_moodul.py, saab selle teistes failides importida ja kasutada.

def tervita(nimi):
    return f"Tere, {nimi}!"

def korruta(a, b):
    return a * b

#  Seletan siia lahti kuidas võiks antud koodi kirjutamine olla samm sammult 

# 1. Start
# 2. Generate a random word
# 3. Generate as many blanks as letters in word
# 4. Aske the user to quess a letter
# 5. Is the quessed letter in the word?
# 5. Yes- Replace the blank with the letter. Are all the blanks filled if yes Win / No- Lose a life / Have they run out of lives yes-Game Over

# Antud koodid on näitlikud ja neid jooksuatada korraga pole mõtet, küll aga võid testida näiteks algus step 1 ja siis step 2
# Lõpus kirjutame terve koodi puhtalt mis kajastub minu Projektide all



#Step 1 

word_list = ["Koer", "Inimene", "Ananass"] #Sõnad mida mängus küsib
import random: #Importib Pythoni standardteegis oleva random mooduli, mis võimaldab teil töötada juhuslike arvude ja juhuslike valikute funktsioonidega.
word_list = ["auto", "Koer", "Jäääär", "Banaan"]: #Defineerib nimekirja word_list, mis sisaldab nelja sõna.
chosen_word = random.choice(word_list): #Kasutab random.choice() funktsiooni, et valida juhuslikult üks sõna word_list nimekirjast.
# See valitud sõna salvestatakse muutujasse chosen_word.
#Pärast koodi käivitamist on chosen_word muutuja väärtuseks üks juhuslikult valitud sõna nimekirjast word_list.
# See on kasulik näiteks mängude või muude rakenduste jaoks, kus on vaja juhuslikult valitud sõna.

# Antud kood 
import random
chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
     

#Step 2

import random
word_list = ["Koer", "Inimene", "Ananass",]
chosen_word = random.choice(word_list)

#Testing code
print(): #See funktsioon väljastab teksti konsooli.

f'Pssst, the solution is {chosen_word}.': #See kasutab f-string (formaaditud stringi), et lisada valitud sõna väärtus teate sisse. {chosen_word} asendatakse tegeliku valitud sõnaga.

#Kui soovite, et mängija näeks valitud sõna (näiteks arendusprotsessis või testimise eesmärgil), on see hea viis seda konsoolis kuvada. Pange tähele, et reaalses mängus ei pruugi soovite, et mängija näeks lahendust, sest see rikub mängu mõtet.

print(f'Pssst, the solution is {chosen_word}.')


display = []: # Loob tühja nimekirja nimega display. See on ette nähtud selleks, et hoida jälgimist, millised tähed on juba ära arvatud ja millised on veel avastamata.

for _ in range(word_length):: # Kasutades for tsüklit, käite word_length kordust, kus _ asendatakse praeguse iteratsiooni arvuga.
# Kuigi  ei kasuta tegelikku iteratsioonimuutujat (näiteks for i in range(word_length)), kasutate ikkagi range(word_length).

display += "_": # Lisab iga tsükli iteratsiooni korral nimekirja display ühe allkriipsu (_).
# Seejärel kasutatakse print(display), et näidata, kuidas display muutub igal sammul.

#Antud kood
display = []
for _ in range(word_length):
    display += "_"
    print(display)
guess = input("Guess a letter: ").lower()
for position in range(word_lenght):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)


#Step 3

import random: # Importib Pythoni standardteegis oleva random mooduli, mis võimaldab teil töötada juhuslike arvude ja juhuslike valikute funktsioonidega.

word_list = ["Koer", "Inimene", "Ananass"]: # Defineerib nimekirja word_list, mis sisaldab kolme sõna.

chosen_word = random.choice(word_list): # Kasutab random.choice() funktsiooni, et valida juhuslikult üks sõna word_list nimekirjast. See valitud sõna salvestatakse muutujasse chosen_word.

word_length = len(chosen_word): # Kasutab len() funktsiooni, et leida valitud sõna pikkus ja salvestab selle muutujasse word_length.

# Nüüd, pärast nende käskude käivitamist, on teil valitud sõna (chosen_word) ja selle pikkus (word_length). Need on kasulikud muutujad mängus, kus kasutatakse juhuslikult valitud sõna.

#Antud kood 
import random
word_list = ["Koer", "Inimene", "Ananass",]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guess = input("Guess a letter: ").lower()



for position in range(word_length): #Käivitab tsükli, kus position võtab väärtused vahemikus 0 kuni word_length - 1.

letter = chosen_word[position]: #Määrab muutuja letter väärtuseks sõna chosen_word tähe, mis asub praegusel positsioonil position.

print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"): #Väljastab teabe praeguse positsiooni, tähe ja sisestatud tähe kohta. See on kasulik selleks, et jälgida, kuidas programm töötab.

if letter == guess: # Kontrollib, kas praegune täht (letter) on võrdne kasutaja sisestatud tähega (guess).

#Kui True, siis asendatakse vastava positsiooni display nimekirjas olev allkriips letter väärtusega. See võib olla osa mängulaual näidatavast tähestiku osast, mis on seni ära arvatud.
print(display):# Väljastab display nimekirja pärast tsüklit, kus on täiendatud tähtede asukohad vastavalt kasutaja äraarvamistele.


#Check guessed letter
for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter
print(display)

if "_" not in display:
    end_of_game = True
    print("You win.")