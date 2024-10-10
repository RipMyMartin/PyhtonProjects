from tkinter import *

k=0
def vajuta():
    global k
    k+=1
    nupp.config(text=k)

def vajuta_(event):
    global k
    k-=1
    nupp.config(text=k)

#def textboxtist(event):
#    t=textbox.get()
#    pealkiri.configure(text=t,width=len(t))
#    textbox.delete(0,END)

def valik():
    arv=var.get()
    textbox.incert(END,arv)



aken = Tk()
aken.configure(bg='yellow')
aken.geometry("700x250")
aken.iconbitmap('martinsild.ico')
aken.title("TK_Kasutamine")
tekst= "Решение квадратного уровнение\n"

pealkiri = Label(aken,
                 text=tekst,
                 bg="#96f3eb",
                 fg="#3ba243",
                 font="Algerian 16",
                 height=2,width=len(tekst),
                 cursor=("man"))
textbox=Entry(aken,
              bg="#000000",
              fg="#ff7373",
              font="Algerian 20",
              justify=LEFT,
              width=20,
              ) #show="****" отоброжать будет *****

nupp=Button(aken,
            text="Vajuta mind!",
            font="Arial 20",
            height=3,width=10,
            relief=RAISED,
            bg="lightblue",
            command=vajuta,
            )#SUNKEN, GROOVE


obj=[pealkiri,textbox,nupp,f]
for i in obj:
    i.pack()

aken.mainloop()