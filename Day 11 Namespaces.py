# Namespaces:Local vs Global Scope


# Scope  tähistab programmeerimises konteksti, milles muutujad on nähtavad ja kättesaadavad. See määrab, kus muutujat saab kasutada ja millistes osades koodist sellele pääsetakse ligi.
enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside functionn: {enemies}")
    
increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope Muutujad, mis on defineeritud funktsiooni sees, kuuluvad selle funktsiooni kohalikku ulatusse. Need muutujad on nähtavad ainult selles funktsioonis.
def drink_potion():
    potion_strenght = 2
    print(potion_strenght)
    
    drink_potion()
    print(potion_strenght)
    
# Global Scope  Muutujad, mis on defineeritud väljaspool funktsioone või klasside piiranguid, kuuluvad globaalsesse ulatusse. Neile saab igal pool programmist ligi.
player_healt = 10
    
def drink_potion():
    potion_strenght = 2
    print(player_healt)
        
drink_potion()

# There is no Block Scope
game_level = 3
enemies = ["Skeleton", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)

# Modifyng Global Scope viitab programmeerimise kontseptsioonile, kus muutuja nähtavus on piiratud konkreetse plokiga koodi, 
# tavaliselt mõne sulgude {} vahel. Kuigi mõned programmeerimiskeeled toetavad "block scope" konstruktsiooni (näiteks JavaScript alates ECMAScript 6-st),
# mõned, näiteks Python, kasutavad peamiselt funktsionaalset ja globaalset ulatust.
enemies = 1
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 2       
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
    
# Global Constants viitab muutujatele,
# mille väärtust ei ole kavas programmi käigus muuta.
# Need on muutujad, mille väärtust säilitatakse kogu programmi ulatuses ja millele saab viidata igas osas programmist.
# Globaalsed konstandid kasutatakse sageli siis, kui on vaja defineerida püsivaid väärtusi, millele programm juurde pääseb, kuid mida ei tohiks muuta käivitamise ajal.

PI = 3.14159
URL = "https://ww.google.com"
Twitter_handle = "@kasutaja"
# Need on need mida me üldreeglina ei muuda

    