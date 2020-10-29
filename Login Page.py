import tkinter
import tkinter.messagebox
from tkinter import *
import os
 
# Designing window for registration
def a():
    messagebox.showinfo("NOTIFICATION","Please fill the above blanks")
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x200")
 
    global Fname
    global Lname
    global username
    global password
    global number
    global address
    global gender
    global Fname_entry
    global Lname_entry
    global username_entry
    global password_entry
    global number_entry
    global address_entry
    global gender_entry
    Fname= StringVar()
    Lname=StringVar()
    username=StringVar()
    password = StringVar()
    number=StringVar()
    address=StringVar()
    gender=StringVar()

 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    Fname_lable = Label(register_screen, text="First name * ").pack()
    Fname_entry=Entry(register_screen,textvariable=Fname)
    Fname_entry.pack()
    Lname_lable = Label(register_screen, text="Last name * ").pack()
    Lname_entry=Entry(register_screen,textvariable=Lname)
    Lname_entry.pack()
    username_lable = Label(register_screen, text="Username * ").pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ").pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    number_lable = Label(register_screen, text="Phone Number * ").pack()
    number_entry=Entry(register_screen,textvariable=number)
    number_entry.pack()
    address_lable = Label(register_screen, text="Address* ").pack()
    address_entry=Entry(register_screen,textvariable=address)
    address_entry.pack()
    gender_lable = Label(register_screen, text="Gender*").pack()
    var = IntVar()
    Radiobutton(register_screen, text="Male",padx = 5, variable=var, value=1).pack()
    Radiobutton(register_screen, text="Female",padx = 20, variable=var, value=2).pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()


# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    Lname_info=Lname.get()
    Fname_info=Fname.get()
    number_info=number.get()
    gender_info=gender.get()
    address_info=address.get()
    if username_info=="" and password_info=="" :
        a()
    else:
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info+"\n")
        file.write(Fname_info+"\n")
        file.write(Lname_info+"\n")
        file.write(number_info+"\n")
        file.write(address_info+"\n")
        file.write(gender_info+"\n")
        file.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Fname_entry.delete(0,END)
        Lname_entry.delete(0,END)
        number_entry.delete(0,END)
        address_entry.delete(0,END)
        gender_entry.delete(0,END)
        
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    if username1=="" and password1=="" :
        a()
    else:
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                login_sucess()
            else:
                password_not_recognised()
        else:
            user_not_found()

# Designing popup for login success
 
def login_sucess():
    '''global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()'''
    messagebox.showinfo("NOTIFICATION","Log in successfull")
 
# Designing popup for login invalid password
 
def password_not_recognised():
    '''global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()'''
    messagebox.showinfo("NOTIFICATION","password not recognized")
 
# Designing popup for user not found
 
def user_not_found():
    '''global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()'''
    messagebox.showinfo("NOTIFICATION","User not found")
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
def forgetpassword():
    print("r")
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="WELCOME  REASONING FOR MEDICATION ", bg="blue", width=300, height=2, font=("Calibri", 60)).pack()
    Label(text="LogIn & Registration Page", bg="blue", width=300, height=2, font=("Calibri", 40)).pack()
    Label(text="").pack()
    Button(text="Login", height=4, width=50, command = login,bg="green").pack(side=LEFT)
    Label(text="").pack()
    Button(text="Register", height=4, width=50, command=register,bg="green").pack(side=RIGHT)
    Label(text="").pack()
    Button(text="Forget Password",height=4,width=50,command=forgetpassword,bg="green").pack(side=BOTTOM)
    main_screen.mainloop()
main_account_screen()
 
 
 
main_account_screen()

