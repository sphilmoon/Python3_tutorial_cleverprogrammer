# completing a square:
import turtle

ninja_turtle = turtle.Turtle()

ninja_turtle.forward(100) # moving forward 100 distance.
ninja_turtle.right(90) # changing the direction in degree only. No movement.
ninja_turtle.forward(100)
ninja_turtle.right(90)
ninja_turtle.forward(100)
ninja_turtle.right(90)
ninja_turtle.forward(100)

# creating a function:
def square():
        ninja_turtle.forward(100)
        ninja_turtle.right(90)
        ninja_turtle.forward(100)
        ninja_turtle.right(90)
        ninja_turtle.forward(100)
        ninja_turtle.right(90)
        ninja_turtle.forward(100)
square() #calling the square. Now I have two squares.
ninja_turtle.forward(150)
square()
square()
# just made a ribbon.
