#                             Functions with Outputs

# Funktsioonid väljundiga (Functions with outputs) on funktsioonid, 
# mis tagastavad mingisuguse väärtuse pärast nende töö lõpetamist.
# Selleks kasutatakse Pythoni return avaldist. Väljund võib olla üksik väärtus või isegi mitu väärtust,
# kuid return avaldus peatab funktsiooni käivitamise ja tagastab need väärtused selle koha,
# kus funktsioon välja kutsuti.

# Siin on lihtne näide funktsioonist väljundiga:

def square(number):
    result = number * number
    return result

# Funktsiooni väljakutse
result = square(5)
print(result)  # Väljund: 25 / 5*5=25

# Antud näites arvutab funktsioon square antud numbri ruudu ja tagastab selle väärtuse.
# Välja kutsudes funktsiooni square(5) salvestatakse tulemus muutujasse result ning seejärel prinditakse välja. 
# Funktsioon on defineeritud return result abil, mis tagastab arvutatud tulemuse.


# Samuti on võimalik tagastada mitu väärtust, kasutades tuple'it (korrutatud väärtusi saab hiljem lahti pakkida):

def calculate_square_and_cube(number):
    square_result = number * number
    cube_result = number * number * number
    return square_result, cube_result

# Funktsiooni väljakutse
square_result, cube_result = calculate_square_and_cube(3)
print("Square:", square_result)  # Väljund: 9
print("Cube:", cube_result)  # Väljund: 27

# Funktsioon calculate_square_and_cube arvutab antud numbri ruudu ja kuupi ning tagastab mõlemad tulemused tuple'ina.
# Need väärtused lahti pakkides saab neid eraldi kasutada.

# Functions with Outputs

def format_name(f_name, l_name):
    print(f_name.title()) # Väljastab nime igas formaadis suured tähed, väiksed tähed, segamini kokkuvõttes väljastab nime ikka korrekselt.
    print(l_name.title())

format_name("Riho", "RIHO")


# Kui sul on mitu sisendit või siis väärtust
def format_name(f_name, l_name):
 if f_name == "" or l_name == "":

    print(f_name.title())
    print(l_name.title())
print(format_name(input("What is your first name"), 
input("What is your last name? ")))

# Docstrings

# Already used functions with outputs
length = len(formatted_name)

# Return as an early exit
def format_name(f_name, l_name):
 """Take a first and last name and format it to return the title case version of the name"""
 if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
    formated_f_name =(f_name.title())
    formated_l_name = (l_name.title())
    return f"Result: {formated_f_name} {formated_l_name}"




    