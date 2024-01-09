# Loops- Pythonis viitab "loop" (eesti keeles "tsükkel") kontrollistrateegiale,
#  mis võimaldab koodil korduvalt täita teatud plokki.
#  Pythonis on kaks peamist tüüpi tsükleid: for tsükkel ja while tsükkel.

# for -tsükkel võimaldab teil läbida teatud järjestust (nt. loend, sõne, järjend) ja teha mingi tegevus iga elemendi jaoks.
# while  - while tsükkel võimaldab teil korrata koodiplokki seni, kuni teatud tingimus on tõene.

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
   print(fruit)

   # Range functions - unktsioon on sisseehitatud funktsioon Pythonis,
   #  mis genereerib arvujärjestusi. See on sageli kasutusel koos for tsükliga,
   #  kuid seda saab kasutada ka teistes olukordades, kus on vaja arvujärjestust.

   # For Loop with Range
for number in range(1, 11, 3):
      print(number)

