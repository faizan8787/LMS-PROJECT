import tkinter
import pandas
import customtkinter
from customtkinter import *
from PIL import Image
root=None
def add_root():
    global root
    root=customtkinter.CTk()
    root.geometry('300x400')
    root._set_appearance_mode("dark")
add_root()
registered_users={'admin':'iadmin','faizan2021':'2021','hamza20':'2020'}
def get_credentials(user_name,password):
    # print(user_name,password)
    # print(registered_users,registered_users[user_name])
    if user_name in registered_users and password ==registered_users[user_name]:
        print("Login Successful")
        sucess_label = customtkinter.CTkLabel(master=None, width=80, height=30, text='Go to Console for further process ',
                                             font=('default', 20,),
                                             bg_color="grey", fg_color="red")
        sucess_label.place(x=600, y=400)
        print("Yes")
        process(user_name)
    else:
        error_label = customtkinter.CTkLabel(master=None, width=80, height=30, text='Incorrect User Name or Password', font=('default', 20,),
                                                bg_color="grey",fg_color="red")
        error_label.place(x=600, y=400)
def add_image():
    img=customtkinter.CTkImage(dark_image=Image.open("lms4.jpg"),size=(1600,800))
    img1=customtkinter.CTkImage(dark_image=Image.open("lm3.jpg"),size=(300,300))
    lab=customtkinter.CTkLabel(root, image=img,text="")
    lab1=customtkinter.CTkLabel(root, image=img1,text="")
    lab.grid(row=0,column=0)
    lab1.place(x=20,y=20)
add_image()

title_label=customtkinter.CTkLabel(master=root, width=150, height=70, text='Library Management System', font=('default', 50),bg_color="grey")
title_label.place(x=500,y=10)
login_label= customtkinter.CTkLabel(master=root, width=120, height=50, text='Login Here', font=('default', 30),bg_color="grey")
login_label.place(x=710,y=90)
user_name_label= customtkinter.CTkLabel(master=root, width=80, height=30, text='User Name', font=('default', 20),bg_color="grey")
user_name_label.place(x=500,y=150)
user_name_entry = customtkinter.CTkEntry(master=root, height=50, width=500, font=('default', 30))
user_name_entry.place(x=500,y=190)
password_label= customtkinter.CTkLabel(master=root, width=80, height=30, text='Password', font=('default', 20),bg_color="grey")
password_label.place(x=500,y=250)
password_entry = customtkinter.CTkEntry(master=root, height=50, width=500, font=('default', 30))
password_entry.place(x=500,y=290)
login_button=customtkinter.CTkButton(master=root, text="Login", command=lambda :get_credentials(user_name_entry.get(),password_entry.get()))
login_button.place(x=500, y=355)

# print(user_name_entry.get())


frame=pandas.read_excel('Bookshop.xlsx')
# sheet = wb['Edition']
id=list(frame['BookID'])
title=list(frame['Title'])
stock=list(frame['Stock'])
print(title)
def issue_book():
    print("Enter Book Name ")
    book=input()
    if book in title:
        x=title.index(book)
        if stock[x]>0:
            print("You have successfully issued the book")
            stock[x]-=1
        else:
            print("Sorry, Book out of stock")
    else:
        print("Oops!  Book not found")
def return_book():
    print("Enter Book Name ")
    book=input()
    if book in title:
        x=title.index(book)
        print("You have successfully returned the book")
        stock[x]+=1
    else:
        print("Book not found")
def process(user):
    global wb,sheet
    print("Welcome ",user)
    print('Here are the Available Books')
    for i in range(len(title)):
        print("ID: ", id[i], "Title: ",title[i], "Availables: ",stock[i])
    if user=='admin':
        print("press 0 to ADD BOOK")
    print("Press 1 to Get a book")
    print("Press 2 to return a book")
    x=input()
    if x=='0':
        if user=="admin":
            pass
        else:
            print("Only admins can add books")
    elif x=='1':
        issue_book()
    elif x=='2':
        return_book()
root.mainloop()


