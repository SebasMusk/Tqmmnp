import turtle
import json

def draw_from_json(json_file):
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(800, 800)
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    with open(json_file) as f:
        regions = json.load(f)

    # Calcular límites para centrar
    all_points = [(p[0], p[1]) for r in regions for p in r['contour']]
    min_x = min(p[0] for p in all_points)
    max_x = max(p[0] for p in all_points)
    min_y = min(p[1] for p in all_points)
    max_y = max(p[1] for p in all_points)

    width = max_x - min_x
    height = max_y - min_y
    scale = min(600 / width, 600 / height)
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    update_every_n_lines = 600  # Más líneas entre updates = más velocidad

    for region in regions:
        color = '#{:02x}{:02x}{:02x}'.format(
            int(region['color'][0] * 255),
            int(region['color'][1] * 255),
            int(region['color'][2] * 255)
        )
        t.color(color, color)

        points = region['contour'][::1]  # Puedes probar [::2] si quieres aún más velocidad

        if not points:
            continue

        # t.begin_fill()  # puedes comentar esto si relleno no es esencial
        t.penup()

        x = (points[0][0] - center_x) * scale
        y = (center_y - points[0][1]) * scale
        t.goto(x, y)
        t.pendown()

        for i, point in enumerate(points[1:], start=1):
            x = (point[0] - center_x) * scale
            y = (center_y - point[1]) * scale
            t.goto(x, y)

            if i % update_every_n_lines == 0:
                screen.update()

        t.penup()
        # t.end_fill()
        screen.update()  # asegúrate de ver cada región

    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    draw_from_json("archivo.json")
