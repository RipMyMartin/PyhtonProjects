from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

def solve_equation():
    try:
        a = float(a_.get())
        b = float(b_.get())
        c = float(c_.get())
    except ValueError:
        solution_label.config(text="Ошибка: Пожалуйста, введите числа в поля для ввода.")
        return

    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        solution_label.config(text=f"Уравнение имеет два корня:\nX1 = {x1:.2f},\nX2 = {x2:.2f}\nD = {D:.2f}")
    elif D == 0:
        x = -b / (2*a)
        solution_label.config(text=f"Уравнение имеет один корень:\nX = {x:.2f}\nD = {D:.2f}")
    else:
        solution_label.config(text=f"Уравнение не имеет корней\nD = {D:.2f}")

def entry_changed(event):
    if event.widget.get() == "":
        event.widget.config(bg="red")
    else:
        event.widget.config(bg="lightblue")

def graafik():
    try:
        a = float(a_.get())
        b = float(b_.get())
        c = float(c_.get())
        x0 = -b / (2 * a)
        y0 = a * x0 ** 2 + b * x0 + c
        x1 = np.arange(x0 - 10, x0 + 10, 0.5)
        y1 = a * x1 ** 2 + b * x1 + c
        fig = plt.figure()
        plt.plot(x1, y1, color='red', label='Вершина', marker='D')
        plt.scatter(x0, y0, color='red', label='Вершина', marker='D')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text = f"Вершина параболы: ({x0:.2f}, {y0:.2f})"
    except ValueError:
        text = "График невозможно построить из-за ошибки ввода."
    solution_label.config(text=text)

def increase_window_height():
    current_geometry = root.geometry()
    if "1100x500" in current_geometry:
        root.geometry("1100x350")
        button_increase_height.config(text="Увеличить окно")
        for radio in radios:
            radio.grid_remove()
    else:
        root.geometry("1100x500")
        button_increase_height.config(text="Уменьшить окно")
        for radio in radios:
            radio.grid()



def kala():
    x1 = np.arange(0, 9.5, 0.5)
    x2 = np.arange(-10, 0.5, 0.5)
    x3 = np.arange(-9, -2.5, 0.5)
    x4 = np.arange(-3, 9.5, 0.5)
    x5 = np.arange(5, 9, 0.5)
    x6 = np.arange(5, 8.5, 0.5)
    x7 = np.arange(-13, -8.5, 0.5)
    x8 = np.arange(-15, -12.5, 0.5)
    x9 = np.arange(-15, -10, 0.5)
    x10 = np.arange(3,4,0.5)

    y1= (2/27)*x1*x1-3
    y2= 0.04*x2*x2-3
    y3= (2/9)*(x3+6)**2+1
    y4= (-1/12)*(x4-3)**2+6
    y5= (1/9)*(x5-5)**2+2
    y6= (1/8)*(x6-7)**2+1.5
    y7= -0.75*(x7+11)**2+6
    y8= (-0.5)*(x8+13)**2+3
    y9= [1]*len(x9)
    y10= [3]*len(x10)

    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title("Kala")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()


def prillid():
    x1 = np.arange(-9, -0.5, 0.5)
    x2 = np.arange(1, 9.5, 0.5)
    x3 = np.arange(-9, -0.5, 0.5)
    x4 = np.arange(1, 9.5, 0.5)
    x5 = np.arange(-9, -5.5, 0.5)
    x6 = np.arange(6, 9.5, 0.5)
    x7 = np.arange(-1, 1.5, 0.5)

    y1= (-1/16)*(x1+5)**2+2
    y2= (-1/16)*(x2-5)**2+2
    y3= (1/4)*(x3+5)**2-3
    y4= (1/4)*(x4-5)**2-3
    y5= -1*(x5+7)**2+5
    y6= -1*(x6-7)**2+5
    y7= -0.5*x7**2+1.5

    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title("Prillid")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def vihmavari():
    x1 = np.arange(-12, 12.5, 0.5)
    x2 = np.arange(-4, 4.5, 0.5)
    x3 = np.arange(-12, -3.5, 0.5)
    x4 = np.arange(4, 12.5, 0.5)
    x5 = np.arange(-4, 0.5, 0.5)
    x6 = np.arange(-4, 0.7, 0.5)

    y1= (-1/18)*x1**2+12
    y2= (-1/8)*x2**2+6
    y3= (-1/8)*(x3+8)**2+6
    y4= (-1/8)*(x4-8)**2+6
    y5= 2*(x5+3)**2-9
    y6= 1.5*(x6+3)**2-10

    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title("Vihmavari")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()


def vaal():
    x1 = np.arange(0, 9.5, 0.5)
    y1 = (2/27) * x1 * x1 - 3
    x2 = np.arange(-10, 0, 0.5)
    y2 = 0.04 * x2 * x2 - 3
    x3 = np.arange(-9, -2.5, 0.5)
    y3 = (2/9) * (x3 + 6) ** 2 + 1
    x4 = np.arange(-3, 9.5, 0.5)
    y4 = (-1/12) * (x4 - 3) ** 2 + 6
    x5 = np.arange(5, 9, 0.5)
    y5 = (1/9) * (x5 - 5) ** 2 + 2
    x6 = np.arange(5, 8.5, 0.5)
    y6 = (1/8) * (x6 - 7) ** 2 + 1.5
    x7 = np.arange(-13, -8.5, 0.5)
    y7 = (-0.75) * (x7 + 11) ** 2 + 6
    x8 = np.arange(-15, -12.5, 0.5)
    y8 = (-0.5) * (x8 + 13) ** 2 + 3
    x9 = np.arange(-15, -10, 0.5)
    y9 = [1] * len(x9)
    x10 = np.arange(3, 4, 0.5)
    y10 = [3] * len(x10)
    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10)
    plt.title('Vaal')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def liblikas():
    x1 = np.arange(-9, -1.5, 0.5)
    y1 = (-1/8) * (x1 + 9) ** 2 + 8
    x2 = np.arange(1, 9.5, 0.5)
    y2 = (-1/8) * (x2 - 9) ** 2 + 8
    x3 = np.arange(-9, 8.5, 0.5)
    y3 = 7 * (x3 + 8) ** 2 + 1
    x4 = np.arange(8, 9.5, 0.5)
    y4 = 7 * (x4 - 8) ** 2 - 1
    x5 = np.arange(-8, -1.5, 0.5)
    y5 = (1/49) * (x5 + 1) ** 2
    x6 = np.arange(1, 8.5, 0.5)
    y6 = (1/49) * (x6 - 1) ** 2
    x7 = np.arange(-8, -1.5, 0.5)
    y7 = (-4/49) * (x7 + 1) ** 2
    x8 = np.arange(1, 8.5, 0.5)
    y8 = (-4/49) * (x8 - 1) ** 2
    x9 = np.arange(-8, -2.5, 0.5)
    y9 = (1/3) * (x9 + 5) ** 2 - 7
    x10 = np.arange(2, 8.5, 0.5)
    y10 = (1/3) * (x10 - 5) ** 2 - 7
    x11 = np.arange(-2, 1.5, 0.5)
    y11 = -2 * (x11 + 1) ** 2 - 2
    x12 = np.arange(1, 2.5, 0.5)
    y12 = -2 * (x12 - 1) ** 2 - 2
    x13 = np.arange(-1, 1.5, 0.5)
    y13 = -4 * x13 ** 2 + 2
    x14 = np.arange(-1, 1.5, 0.5)
    y14 = 4 * x14 ** 2 - 6
    x15 = np.arange(-2, 0.5, 0.5)
    y15 = -1.5 * x15 + 2
    x16 = np.arange(0.5, 2.5, 0.5)
    y16 = 1.5 * x16 + 2
    fig = plt.figure()
    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13, y13, x14, y14, x15, y15, x16, y16)
    plt.title('Liblikas')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()


root = Tk()
root.geometry("1100x350")
root.title("TK_Inter usage")

title_label = Label(root,
                    text="Решение квадратного уравнения\n",
                    bg="#96f3eb",
                    fg="#3ba243",
                    font="Algerian 16",
                    height=2, width=30,
                    cursor=("man"))

button_frame = Frame(root, bg="")

a_ = Entry(button_frame,
           font="Arial 20",
           width=10,
           bg="lightblue",
           )
label1 = Label(button_frame,
               text="x**2 +",
               font="Arial 12",
               bg="lightblue",
               )
b_ = Entry(button_frame,
           font="Arial 20",
           width=10,
           bg="lightblue",
           )
label2 = Label(button_frame,
               text="x +",
               font="Arial 12",
               bg="lightblue",
               )
c_ = Entry(button_frame,
           font="Arial 20",
           width=10,
           bg="lightblue",
           )
label3 = Label(button_frame,
               text="= 0",
               font="Arial 12",
               bg="lightblue",
               )
button4 = Button(button_frame,
                 text="Решить",
                 font="Arial 20",
                 height=3, width=10,
                 relief=RAISED,
                 bg="#67ff1c",
                 command=solve_equation
                 )

button_graph = Button(button_frame,
                      text="График",
                      font="Arial 20",
                      height=3, width=10,
                      relief=RAISED,
                      bg="#ff6f61",
                      command=graafik
                      )

button_increase_height = Button(button_frame,
                                text="Увеличить окно",
                                font="Arial 12",
                                bg="#ffcc00",
                                command=increase_window_height)

solution_label = Label(button_frame, text="решение", font="Arial 12", bg="yellow", justify=LEFT, padx=20)

title_label.grid(row=0, column=0, columnspan=4)
button_frame.grid(row=2, column=0, columnspan=4)

a_.grid(row=0, column=0, padx=10, pady=10)
label1.grid(row=0, column=1, padx=10, pady=10)
b_.grid(row=0, column=2, padx=10, pady=10)
label2.grid(row=0, column=3, padx=10, pady=10)
c_.grid(row=0, column=4, padx=10, pady=10)
label3.grid(row=0, column=5, padx=10, pady=10)
button4.grid(row=0, column=6, padx=10, pady=10)
button_graph.grid(row=0, column=7, padx=10, pady=10)
solution_label.grid(row=1, column=0, columnspan=10, pady=10)
button_increase_height.grid(row=3, column=0, columnspan=10, pady=10)

a_.bind("<KeyRelease>", entry_changed)
b_.bind("<KeyRelease>", entry_changed)
c_.bind("<KeyRelease>", entry_changed)

radios = []
for i, text in enumerate(["Vaal"]):
    radio = Radiobutton(button_frame, text=text, command=vaal)
    radio.grid(row=5, column=1, padx=10, pady=10)
    radios.append(radio)

for i, text in enumerate(["Liblikas"]):
    radio = Radiobutton(button_frame, text=text, command=liblikas)
    radio.grid(row=5, column=2, padx=10, pady=10)
    radios.append(radio)

for i, text in enumerate(["Vihmavari"]):
    radio = Radiobutton(button_frame, text=text, command=vihmavari)
    radio.grid(row=5, column=3, padx=10, pady=10)
    radios.append(radio)


for i, text in enumerate(["Prillid"]):
    radio = Radiobutton(button_frame, text=text, command=prillid)
    radio.grid(row=5, column=4, padx=10, pady=10)
    radios.append(radio)




root.mainloop()
