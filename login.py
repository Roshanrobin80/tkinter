import tkinter

win=tkinter.Tk()
win.title=('Login')
win.configure(bg='purple')
win.minsize(400,400)
win.maxsize(500,500)
def save():
    

l1=tkinter.Label(win,text='LOGIN',bg='purple',fg='white')
l1.pack()

l2=tkinter.Label(win,text='User Name')
l2.place(x=75,y=50)

l3=tkinter.Label(win,text='Password')
l3.place(x=75,y=100)

# l4=tkinter.Label(win,text='Login')
# l4.place(x=200,y=170)

e1=tkinter.Entry(win)
e1.place(x=170,y=50)

e2=tkinter.Entry(win)
e2.place(x=170,y=100)

btn1=tkinter.Button(win,text='Login',bg='gray',activebackground='black',activeforeground='white',padx=10,pady=8,command=save)
btn1.place(x=150,y=80)


win.mainloop()