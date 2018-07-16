from turtle import *
edge_length = 100
angle = 120
def teleport(distance):
    penup()      
    forward(distance)
    pendown()   
def draw_hexagram(colour):
    color(colour)
    for _ in range(3):
        forward(edge_length)
        left(angle)
        forward(edge_length)
        teleport(edge_length)     
draw_hexagram('red')
left(60)
teleport(edge_length)
draw_hexagram('blue')
