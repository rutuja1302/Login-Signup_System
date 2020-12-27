from tkinter import *
import sqlite3

#create an object to create a window
window = Tk()

#Actions on Pressing Login Button
def login():
    def login_database():
        conn = sqlite3.connect("1.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
        row=cur.fetchall()
        conn.close()
        print(row)
        if row!=[]:
            user_name=row[0][1]
            l3.config(text="user name found with name: "+user_name)
        else:
            l3.config(text="user not found")

    window.destroy()  #closes the previous window
    login_window = Tk() #creates a new window for loging in
    login_window.title("LogIn")  #set title to the window
    login_window.geometry("400x250")  #set dimensions to the window
    #add 2 Labels to the window
    l1 = Label(login_window,text="email: ",font="times 20")
    l1.grid(row=1,column=0)

    l2 = Label(login_window,text="Password: ",font="times 20")
    l2.grid(row=2,column=0)

    l3 = Label(login_window,font="times 20")
    l3.grid(row=5,column=1)

    #creating 2 adjacent text entries
    email_text = StringVar() #stores string
    e1 = Entry(login_window,textvariable=email_text)
    e1.grid(row=1,column=1)

    password_text = StringVar()
    e2 = Entry(login_window,textvariable=password_text,show='*')
    e2.grid(row=2,column=1)

    #create 1 button to login
    b = Button(login_window,text="login",width=20,command=login_database)
    b.grid(row=4,column=1)

    login_window.mainloop()

#Actions on Pressing Signup button
def signup():
    #Database action on pressing signup button
    def signup_database():
        conn = sqlite3.connect("1.db") #create an object to call sqlite3 module & connect to a database 1.db
        #once you have a connection, you can create a cursor object and call its execute() method to perform SQL commands
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text,password text)")
        cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
        
        #execute message after account successfully created
        l4 = Label(signup_window,text="account created",font="times 15")
        l4.grid(row=6,column=2)
        
        conn.commit()  #save the changes 
        conn.close() #close the connection

    window.destroy()  #closes the previous window
    signup_window = Tk() #creates a new window for signup process
    signup_window.geometry("400x250") #dimensions for new window
    signup_window.title("Sign Up") #title for the window
    #create 3 Labels
    l1 = Label(signup_window,text="User Name: ",font="times 20")
    l1.grid(row=1,column=1)

    l2 = Label(signup_window,text="User email: ",font="times 20")
    l2.grid(row=2,column=1)

    l3 = Label(signup_window,text="Password: ",font="times 20")
    l3.grid(row=3,column=1)

    #create 3 adjacent text entries
    name_text = StringVar() #declaring string variable for storing name and password
    e1 = Entry(signup_window,textvariable=name_text)
    e1.grid(row=1,column=2)

    email_text = StringVar()
    e2 = Entry(signup_window,textvariable=email_text)
    e2.grid(row=2,column=2)

    password_text = StringVar()
    e3 = Entry(signup_window,textvariable=password_text,show='*')
    e3.grid(row=3,column=2)

    #create 1 button to signup
    b1 = Button(signup_window,text="signup",width=20,command=signup_database)
    b1.grid(row=4,column=2)

    signup_window.mainloop()

#main window code and driver code
#give dimensions to the window
window.geometry("300x150")
#add title to the window
window.title("Login and Signup system")
#adding the label "Register Here"
label1 = Label(window, text="Register Here!",font="times 20")
label1.grid(row=1,column=2,columnspan=2)
#adding two buttons - login and signup
button1 = Button(window,text="Login",width=20,command=login)
button1.grid(row=2,column=2)

button2 = Button(window,text="Signup",width=20,command=signup)
button2.grid(row=2,column=3)
#calling mainloop method which is used when your application is ready to run and it tells the code to keep displaying
window.mainloop()
