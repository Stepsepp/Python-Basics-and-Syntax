# Strings-  (sõned) on Pythonis andmetüüp, mis esindab teksti või karakterite jada. Sõned märgitakse kas ühekordsete (') või kahekordsete (") jutumärkidega.
# "\n" on põhimõtteliselt põik-kaldkriips ja 'n' kombinatsioon sõnes, mis tähistab uut rida (newline) Pythoni süntaksis ja paljudes muudes programmeerimiskeeltes.

# Näide :
print ("Tere Riho")  # Print -  on Pythoni sisseehitatud funktsioon, mis võimaldab väljastada teksti või muutuja väärtusi ekraanile.

# Kuvame ühte teksti 2 korda \n abil
print("Tere Riho\nTere Riho")

# Teeme ühe näite veel kus paneme 3 korda ja üksteise alla 
print("Tere Hommikust\nTere Hommikust\nTere Hommikust")  # Niimoodi võid panna ükskõik kui palju teksti enda alla, kasulik veebilehe loomisel kus kasutatakse HTML

# Saame ka moodustada lauseid kasutadates + märki kuid siin pead arvestama et tühikud peavad olema " ja + vahel muidu kirjutab lause kokku.
# Tühikud on Bythonis väga olulised
print("Tere " + " Riks")


# input() funktsiooni kasutatakse Pythonis kasutaja sisendi vastuvõtmiseks. See loeb kasutaja sisendi rea, teisendab selle stringiks ja tagastab selle stringina.
# Näide kuidas kasutada input funktsiooni. Input kasutades me saame määrata mida kasutaja peab sisestama, olgu selleks siis nimi, sünniaeg, vms 
print("Tere tulemast tagasi loengusse " + input("Kuidas on teie nimi"))

# me saame anda ka inputile nime näiteks nimi = input või vanus = inpit 
nimi = input("Kuidas on teie nimi")
print(nimi)

# sammuti saame panna näiteks Linn = "Tallinn " print (Linn)

Linn ="Tallinn"
print(Linn)

# Pythonis kasutatakse funktsiooni len() objekti pikkuse mõõtmiseks. Funktsiooni käitumine sõltub objekti tüübist, mis antakse argumentina. 
# antud olukorras me küsime nime ja antud kood loeb mitu tähte on nimes ja kuvab selle 

nimi = input("Sisesta oma nimi")
length =len(nimi)  # length funktsioon annab objekti pikkuse või suuruse, sõltuvalt objektist.
print(length)

print("See töötab")