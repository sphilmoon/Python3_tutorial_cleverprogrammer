import turtle

ninja_turtle = turtle.Turtle()

def square():
        ninja_turtle.forward(100)
        ninja_turtle.right(90)
        ninja_turtle.forward(100)
        ninja_turtle.right(90)
        ninja_turtle.forward(100)
        ninja_turtle.right(90)
        ninja_turtle.forward(100)

elephant_weight = 6000
rhino_weight = 2200

# if statement:
if elephant_weight < rhino_weight:
    square()
    print(elephant_weight > rhino_weight)
else:
    ninja_turtle.forward(200)
    print(False)

# while loop: this will not stop until you break the loop.
phil = 'max'
while phil == 'max':
    square()
    break

# for loop: printing 0, 1, 2, 3, 4.
for i in range(5):
    print(i)
