import tkinter as tk
from random import choice
from math import sqrt

def draw_boat():
    canvas.delete("item")
    canvas.create_polygon(50, 200, 250, 200, 200, 250, 100, 250, fill="brown", outline="black", tags="item")
    canvas.create_polygon(150, 50, 150, 200, 250, 200, fill=sail_color, outline="black", tags="item")
    canvas.create_line(150, 50, 150, 200, fill="black", width=3, tags="item")
    canvas.create_oval(125, 210, 175, 260, fill="gray", outline="black", tags="item")

def change_sail_color():
    global sail_color_index
    sail_color_index = (sail_color_index + 1) % len(sail_colors)
    update_sail_color()

def update_sail_color():
    global sail_color
    sail_color = sail_colors[sail_color_index]
    draw_boat()

def draw_estonia_flag():
    canvas.delete("item")
    draw_boat()
    canvas.create_rectangle(0, 0, 500, 100, fill="blue", tags="item")
    canvas.create_rectangle(0, 100, 500, 200, fill="black", tags="item") 
    canvas.create_rectangle(0, 200, 500, 300, fill="white", tags="item")

def draw_poland_flag():
    canvas.delete("item")
    canvas.create_rectangle(0, 0, 200, 133, fill="white", tags="item")
    canvas.create_rectangle(0, 0, 200, 66, fill="red", tags="item")

def draw_bahamas_flag():
    canvas.delete("item")
    draw_boat()
    canvas.create_rectangle(0, 0, 500, 100, fill="aqua", tags="item")
    canvas.create_rectangle(0, 100, 500, 200, fill="yellow", tags="item")
    canvas.create_rectangle(0, 200, 500, 300, fill="aqua", tags="item")
    canvas.create_polygon(0, 0, 250, 150, 0, 300, fill="black", outline="", tags="item")

def draw_rainbow_ball():
    canvas.delete("item")
    draw_boat()
    colors = ["black", "cyan", "magenta", "red", "blue", "gray", "yellow", "green", "lightblue", "pink", "gold"]
    x0 = 0
    y0 = 0
    x1 = 500
    y1 = 500
    p = 2
    for i in range(150):
        x0 += p
        y0 += p
        x1 -= p
        y1 -= p
        canvas.create_oval(x0, y0, x1, y1, fill=choice(colors), tags="item")

def draw_square_in_square():
    canvas.delete("item")
    draw_boat()
    k = 10
    x0 = 65
    y0 = 65
    x1 = 400
    y1 = 400
    a = 200
    r = int(sqrt(a ** 2 + a ** 2))
    p = a - r 
    for i in range(k):
        x0 += p 
        y0 += p 
        x1 -= p 
        y1 -= p
        canvas.create_rectangle(x0, y0, x1, y1, width=1, outline="blue", fill="Red", tags="item")
        canvas.create_oval(x0, y0, x1, y1, width=1, outline="blue", fill="Yellow", tags="item")
        p = r - a
        r = r - p
        a = int((r * sqrt(2)) / 2)

def draw_chessboard():
    canvas.delete("item")
    draw_boat()
    size = 500
    rows = cols = 8
    square_size = size // max(rows, cols)
    colors = ["white", "black"]    
    for row in range(rows):
        for col in range(cols):            
            color_index = (row + col) % 2
            color = colors[color_index]            
            x0 = col * square_size
            y0 = row * square_size            
            x1 = x0 + square_size
            y1 = y0 + square_size            
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="", tags="item")


def display_item():
    selected_item = item_var.get()
    if selected_item == "estonia":
        draw_estonia_flag()
    elif selected_item == "poland":
        draw_poland_flag()
    elif selected_item == "bahamas":
        draw_bahamas_flag()
    elif selected_item == "rainbow_ball":
        draw_rainbow_ball()
    elif selected_item == "square_in_square":
        draw_square_in_square()
    elif selected_item == "chessboard":
        draw_chessboard()
    elif selected_item == "boat":
        draw_boat()

root = tk.Tk()
root.title("Элементы")
root.geometry("900x800")

canvas = tk.Canvas(root, width=600, height=500)
canvas.pack(pady=20)

item_var = tk.StringVar()
item_var.set("estonia")
sail_colors = ["white", "blue", "green", "red"]
sail_color_index = 0
sail_color = sail_colors[sail_color_index]

estonia_radio = tk.Radiobutton(root, text="Флаг Эстонии", variable=item_var, value="estonia", command=display_item)
estonia_radio.pack(pady=5)
poland_radio = tk.Radiobutton(root, text="Флаг Польши", variable=item_var, value="poland", command=display_item)
poland_radio.pack(pady=5)
bahamas_radio = tk.Radiobutton(root, text="Флаг Багамских островов", variable=item_var, value="bahamas", command=display_item)
bahamas_radio.pack(pady=5)
rainbow_radio = tk.Radiobutton(root, text="Радужный шар", variable=item_var, value="rainbow_ball", command=display_item)
rainbow_radio.pack(pady=5)
square_radio = tk.Radiobutton(root, text="Квадрат в квадрате", variable=item_var, value="square_in_square", command=display_item)
square_radio.pack(pady=5)
chessboard_radio = tk.Radiobutton(root, text="Шахматы", variable=item_var, value="chessboard", command=display_item)
chessboard_radio.pack(pady=5)
boat_radio = tk.Radiobutton(root, text="Лодка", command=change_sail_color)
boat_radio.pack(pady=5)

root.mainloop()
