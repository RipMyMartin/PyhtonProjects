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

def textboxtist(event):
    t=textbox.get()
    pealkiri.configure(text=t,width=len(t))
    textbox.delete(0,END)

def valik():
    arv=var.get()
    textbox.incert(END,arv)



aken = Tk()
aken.geometry("400x200")
aken.iconbitmap('martinsild.ico')
aken.title("TK_Kasutamine")
tekst= "Pealkiri\n"
pealkiri = Label(aken,
                 text=tekst,
                 bg="#ff7373",
                 fg="#ff7373",
                 font="Algerian 20",
                 height= 3,width=len(tekst),
                 cursor=("man"))
textbox=Entry(aken,
              bg="#ff7373",
              fg="#ff7373",
              font="Algerian 20",
              width=20,
              justify=CENTER) #show="****" отоброжать будет *****
nupp=Button(aken,
            text="Vajuta mind!",
            font="Arial 20",
            height=3,width=10,
            relief=RAISED,
            bg="lightblue",
            command=vajuta,
            )#SUNKEN, GROOVE

f=Frame(aken)
var=IntVar() #StringVar()
e_=Radiobutton(f,text="Esimene",variable=var,value=1,command=valik)
t_=Radiobutton(f,text="Teine",variable=var,value=2,command=valik)
k_=Radiobutton(f,text="Kolmas",variable=var,value=3,command=valik)


nupp.bind("<Button-3>",vajuta_)
textbox.bind("<Return>",textboxtist)#Enter

obj=[pealkiri,textbox,nupp,f]
for i in obj:
    i.pack()

obj2=[e_,t_,k_]
for n in range(len(obj2)):
    obj2[n].grid(row=0,column=1)

pealkiri.pack()
textbox.pack()
nupp.pack()
aken.mainloop()