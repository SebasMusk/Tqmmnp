import turtle
import json

def draw_from_json(json_file):
    #configurar turtle
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(800, 800)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    screen.tracer(0)