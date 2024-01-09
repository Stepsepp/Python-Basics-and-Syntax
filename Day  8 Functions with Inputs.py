#                                                              Day 8
#
#                                                     Functions with Inputs 
#                                                     Arguments and Parameters


# Antud koodis me loome enda mingi funksiooni, näiteks funksiooni, mis küsib küsimus.

def küsimused():
   print("Tere")
   print("Kuidas läheb")
   print("Kuidas ilm on?")
küsimused()

# Nüüd loome uue funksiooni kus lisame ka (nimi). Kindlasi tuleb panna print järgi f mis võimaldav väljastada nime.
# Antud koodi mõte on luua funksioon kus saate alati muuta nime ja ta väljastab selle, ilma et peaks kogu,
# koodi ümber kirjutama.

# Function that allows for input
def küsimused2(nimi):
   print(f"Tere {nimi}")
   print(f"Kuidas läheb {nimi}?")
   print(f"Kuidas ilm on {nimi}?")
küsimused2("Riho")


#                                         Positional vs. Keyword Arguments


# Functions with more than 1 input
# Antud funksioonis me lõime koodiploki kus me saame panna sisendiks, mitu väärtust ja antud kood ka väljastab selle.
def riks(nimi, asukoht):
   print(f"Tere {nimi}")
   print(f"Kuidas on ilm {asukoht}")
riks("Riho","Tallinnas")

# Functions with keyword arguments
# # Teine väljakutse võtmesõnadega
riks(nimi="Riho", asukoht="Tartu")




