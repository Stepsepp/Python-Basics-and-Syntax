import random                          # Impordi 'random' moodul juhuslike arvude genereerimiseks
random_integer = random.randint(1, 10)    # Genereeri suvaline täisarv vahemikus 1 kuni 10 (kaasa arvatud)
print(random_integer)                        # Prindi suvaliselt genereeritud täisarv

random_float = random.random()            # Genereerib suvaline ujukomaarv vahemikus 0 (kaasa arvatud) kuni 1 (välja arvatud)
print(random_float)

# Lists

Linnad = ["Tallinn", "Tartu", "Pärnu", "Narva", "Rakvere"] # Listid märgitakse []
 # Nagu me teame hakkab letelu 0,1,2,3 jne kui me aga tahame et list hakkaks altpoolt peale siis lisame hoopis -1 ehk [-1]
# Me saame ka listi muuta näiteks kui me soovime Tartu linn muudetaks listis ära tartlased, tuleks teha nii:
Linnad[1] = "Tartlased"
print(Linnad)
