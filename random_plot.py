import random

def random_plot(canvas, color):
    w = int(canvas["width"])
    h = int(canvas["height"])
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    print(f"({x},{y})")
    canvas.create_oval(
        w / 2 + x, h / 2 - y,
        w / 2 + x, h / 2 - y,
        outline=color, width=10
    )