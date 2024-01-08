#                                           Dictionary     

# Pythonis on sõnastik (dictionary) andmestruktuur, mis võimaldab salvestada võti-väärtus paare. Sõnastikud on muudetavad, 
# dünaamilised ja neid kasutatakse laialdaselt erinevates olukordades, kus on vaja talletada seotud andmeid.
# Sõnastikud on defineeritud sügavate kaldkriipsudega {} ja võivad sisaldada erinevat tüüpi väärtusi, sealhulgas numbreid,
# sõnesid, loendeid ja isegi teisi sõnastikke.


# Näide

# Lihtne sõnastik
minu_sõnastik = {"nimi": "Alice", "vanus": 25, "linn": "Tallinn"}

# Väärtustele juurde pääseda võtmete abil
print(minu_sõnastik["nimi"])  # Väljund: Alice
print(minu_sõnastik["vanus"])  # Väljund: 25
print(minu_sõnastik["linn"])  # Väljund: Tallinn

# Dictionaryid on kasulikud andmestruktuurid, kuna võimaldavad kiiret otsingut ja juurdepääsu andmetele
# ning neid kasutatakse laialdaselt programmeerimises erinevate ülesannete lahendamiseks.

# Näide 1 

# Sõnastik loenditega
õpilased = {
    "Alice": [90, 85, 88],
    "Bob": [87, 91, 89],
    "Charlie": [78, 82, 80]
}

# Väärtustele ligipääs
print(õpilased["Alice"])  # Väljund: [90, 85, 88]
print(õpilased["Bob"][1])  # Väljund: 91 (teine hinne)

# Näide 2 

# Pesastatud sõnastik
autod = {
    "Toyota": {"mudel": "Camry", "aasta": 2022, "värv": "hall"},
    "Honda": {"mudel": "Civic", "aasta": 2021, "värv": "sinine"}
}

# Väärtustele ligipääs
print(autod["Toyota"]["aasta"])  # Väljund: 2022
print(autod["Honda"]["värv"])  # Väljund: sinine

# Näide 3

# Sõnastiku lisamine ja muutmine
telefoniraamat = {"Alice": 123456789, "Bob": 987654321}

# Uue kontakti lisamine
telefoniraamat["Charlie"] = 555555555

# Muutmise
telefoniraamat["Bob"] = 999999999

# Väärtustele ligipääs
print(telefoniraamat["Alice"])  # Väljund: 123456789
print(telefoniraamat["Charlie"])  # Väljund: 555555555
print(telefoniraamat["Bob"])  # Väljund: 999999999

