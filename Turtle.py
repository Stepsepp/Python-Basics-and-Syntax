from turtle import Turtle, Screen
import random

riho_turtle = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
riho_turtle.shape("turtle")
riho_turtle.color("Red", "Pink")

# Selleks et antud koode kasutada eemalda koodirealt #
# Me tahame et kilpkonn liiguks nii et moodustusk ruut.See on pikem variant ja saab lihtsamalt

# Kood

#riho_turtle.forward(100)
#riho_turtle.right(90)
#riho_turtle.forward(100)
#riho_turtle.right(90)
#riho_turtle.forward(100)
#riho_turtle.right(90)
#riho_turtle.forward(100)
#riho_turtle.right(90)


# Lihtsam variant ja parem kuidas kilpkonn teeks ruudu 3 rea koodiga
# Kood

#for _ in range(4):
    #riho_turtle.forward(100)
    #riho_turtle.right(90)



# Nüüd teeme nii et kui kilpkonn liigub jäävad maha katkendlikud jooned
# Kood

#for _ in range(15):
        #riho_turtle.forward(10)
        #riho_turtle.penup()
        #riho_turtle.forward(10)
        #riho_turtle.pendown()


# Antud koodis  tekitab see kood Turtle'i graafilise akna, kus joonistatakse erinevaid polügoone vahemikus 3 kuni 10 külge,
# igaüks juhusliku värviga.
# Kood

#def draw_shape(num_sides):
    #angle = 360 / num_sides
    #for _ in range(num_sides):
        #riho_turtle.forward(100)
        #riho_turtle.right(angle)

#for shape_side_n in  range(3, 11):
    #riho_turtle.color(random.choice(colours))
    #draw_shape(shape_side_n)


# Draw a Random Walk
# Kood

#directions = [0, 90, 180, 270]
#riho_turtle.pensize(15)
#riho_turtle.speed("fastest")

#for _ in range(900):
    #riho_turtle.color(random.choice(colours))
    #riho_turtle.forward(30)
    #riho_turtle.setheading(random.choice(directions))



















screen = Screen()
screen.exitonclick()

