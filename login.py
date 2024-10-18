import tkinter
import sqlite3
# con=sqlite3.connect('tkinter.db')
# con.execute('create table sample(username text,password text)')

win=tkinter.Tk()
win.title=('Login')
win.configure(bg='purple')
win.minsize(400,400)
win.maxsize(500,500)

def Home():
    win2=tkinter.Tk()
    l1=tkinter.Label(win2,text='Home Page',bg='lime',fg='blue')
    l1.place(x=150,y=20)
    btn1=tkinter.Button(win2,text='Logout',command=win2.quit)
    btn1.place(x=200,y=0)
    win2.mainloop()

def login():
    con=sqlite3.connect('tkinter.db')
    data=con.execute('select * from sample')
    f=0
    for i in data:
        if i[0]==e1.get() and i[1]==e2.get():
            f=1
            Home()
    if f==0:
        l3.config(text='invalid username or password')


def reg_form():
    win1=tkinter.Tk()
    win1.minsize(400,400)
    win1.maxsize(500,500)


    def reg():
        con=sqlite3.connect('tkinter.db')
        con.execute('insert into sample(username,password)values(?,?)',(e1.get(),e2.get()))
        con.commit()
        win1.destroy()

    l2=tkinter.Label(win1,text='user name')
    l2.place(x=75,y=30)

    e1=tkinter.Entry(win1)
    e1.place(x=150,y=30)
    l2=tkinter.Label(win1,text='password')
    l2.place(x=75,y=60)

    e2=tkinter.Entry(win1)
    e2.place(x=150,y=60)
    btn1=tkinter.Button(win1,text='register',bg='gray',activebackground='black',activeforeground='white')
    btn1.place(x=150,y=90)

    win1.mainloop()

l1=tkinter.Label(win,text='welcome ',bg='green',fg='blue')
l1.place(x=150,y=20)
l2=tkinter.Label(win,text='user name')
l2.place(x=75,y=30)

e1=tkinter.Entry(win)
e1.place(x=150,y=30)
l2=tkinter.Label(win,text='password')
l2.place(x=75,y=60)

e2=tkinter.Entry(win)
e2.place(x=150,y=60)

btn1=tkinter.Button(win,text='login',bg='gray',activebackground='black',activeforeground='white')
btn1.place(x=150,y=90)

btn2=tkinter.Button(win,text='register',bg='gray',activebackground='black',activeforeground='white')
btn2.place(x=150,y=90)
l3=tkinter.Label(win)
l3.place(x=150,y=160)

win.mainloop()













# def save():
#     win1=tkinter.Tk()
#     win1.title('Register')
#     win1.configure(bg='cyan')
#     win1.minsize(400,400)
#     win1.maxsize(500,500)
#     l4=tkinter.Label(win1,text='REGISTER',bg='cyan',fg='black')
#     l4.pack()
#     l5=tkinter.Label(win1,text='User Name')
#     l5.place(x=75,y=50)
#     l6=tkinter.Label(win1,text='Password')
#     l6.place(x=75,y=100)
#     e3=tkinter.Entry(win1)
#     e3.place(x=170,y=50)
#     e4=tkinter.Entry(win1)
#     e4.place(x=170,y=100)
#     btn2=tkinter.Button(win1,text='submit',bg='gray',activebackground='green',activeforeground='white',padx=3,pady=3)
#     btn2.place(x=200,y=200)
#     win1.mainloop()

# l1=tkinter.Label(win,text='LOGIN',bg='purple',fg='black')
# l1.pack()

# l2=tkinter.Label(win,text='User Name')
# l2.place(x=75,y=50)

# l3=tkinter.Label(win,text='Password')
# l3.place(x=75,y=100)



# e1=tkinter.Entry(win)
# e1.place(x=170,y=50)

# e2=tkinter.Entry(win)
# e2.place(x=170,y=100)


# btn=tkinter.Button(win,text='submit',bg='gray',activebackground='black',activeforeground='white',padx=3,pady=3,)
# btn.place(x=200,y=200)
# btn1=tkinter.Button(win,text='register',bg='gray',activebackground='green',activeforeground='black',padx=3,pady=3,command=save)
# btn1.place(x=50,y=250)


# win.mainloop()
