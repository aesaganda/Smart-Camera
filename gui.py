from os import system
from tkinter import *
import cv2
from PIL import Image, ImageTk

from yurut import yurut

window_width = 1366
window_height = 768


def login():
    userInformation = ["admin", "1234"]
    userName = getUserName.get()
    userPassword = getUserPassword.get()
    print("Bilgiler kontrol ediliyor...")
    if (userName == userInformation[0]) and (userPassword == userInformation[1]):
        print("Kullanici Girisi Basarili. Sisteme yonlendiriliyorsunuz.")
        master.destroy()
        systemScreen()
    else:
        print("Kullanıcı Girişi Hatalı!!!. Tekrar Giris Yapmayı Deneyiniz.")
        control.config(text="Kullanici Girisi Hatali!!!. Tekrar Giris Yapmayi Deneyiniz.", bg="#696969", fg="white",
                       font=("Calibri Italic", 16))
def close():
    print("Program sonlandirildi.")
    exit()

def openTxt(myText):
    textFile = open("simple.txt",'r')
    stuff = textFile.read()
    myText.insert(END,stuff)
    textFile.close()

def systemLogScreen():
    system1 = Tk()
    system1.title("Marmara Kamera Guvenlik Sistemi")
    system1.geometry("1366x768+250+250")
    system1.config(bg="light blue")
    system1.resizable(0, 0)

    #Frame
    frame = Frame(system1, bg="gray")
    frame.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.94)

    #Top Frame
    frameTop = Frame(system1, bg="white")
    frameTop.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.08)

    #NAV
    cameraNav = Label(frameTop, bg="white", text="Marmara Kamera Guvenlik Sistemi",fg="black",  font=("Calibri Italic",20))
    cameraNav.pack()

    #Frame Read
    frameCamera = Frame(frame, bg="gray")
    frameCamera.place(relx=0.01, rely=0.15, relwidth=0.5, relheight=0.7)

    # Read TEXT
    myText = Text(frameCamera)
    myText.pack(pady=45)
    openTxt(myText)

    #Aside Frame
    frameAside = Frame(frame,bg="gray")
    frameAside.place(relx=0.6, rely=0.23, relwidth=0.35, relheight=0.55)

    # Marmara Logo
    photo3 = PhotoImage(file="logoImages/logo.gif")
    photoLabel2 = Label(frameAside, image=photo3)
    photoLabel2.config(bg="gray")
    photoLabel2.pack()

    #Text
    title = Label(frameAside, text="Personel Giris Bilgileri", font="Verdana 15 bold")
    title.config(bg="gray", fg="white")
    title.pack(pady=15)

    #Close Button
    loginButton = Button(frameAside)
    loginButton.config(text="Kapat", bg="white", fg="black", font=("Calibri", 16), command=close)
    loginButton.pack(fill="x" , pady=10,side=BOTTOM)

    frameBottom = Frame(system1, bg="white")
    frameBottom.place(relx=0.02, rely=0.84, relwidth=0.96, relheight=0.1)

    # Marmara footer
    footer1 = Label(frameBottom, bg="white", fg="black", text="© Marmara Güvenlik Sistem Başkanlığı")
    footer1.config(font=("Calibri", 12))
    footer1.pack(pady=10)
    footer2 = Label(frameBottom, bg="white", fg="black", text="• Aziz Eren Sağanda    • Melih Afşar")
    footer2.pack(pady=5)
    system1.mainloop()

def systemScreen():
    def passControl():
        tkSystem.destroy()
        systemLogScreen()

    tkSystem = Tk()
    tkSystem.title("Marmara Kamera Guvenlik Sistemi")
    tkSystem.geometry("1366x768+250+250")
    tkSystem.config(bg="light blue")
    tkSystem.resizable(0, 0)

    #Frame
    frame = Frame(tkSystem, bg="gray")
    frame.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.94)

    #Top Frame
    frameTop = Frame(tkSystem, bg="white")
    frameTop.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.08)

    #Camera NAV
    cameraNav = Label(frameTop, bg="white", text="Marmara Kamera Guvenlik Sistemi",fg="black",  font=("Calibri Italic",20))
    cameraNav.pack()

    #Camera Frame
    frameCamera = Frame(frame, bg="gray")
    frameCamera.place(relx=0.15, rely=0.28, relwidth=0.3, relheight=0.4)

    def show_camera():
        yurut.camera()
        
    #Camera Button
    loginButton = Button(frameCamera)
    loginButton.config(text="Kamera", bg="white", fg="black", font=("Calibri", 16), command=show_camera)
    loginButton.pack(fill="x" , pady=0,side=BOTTOM)
    
    #Aside Frame
    frameAside = Frame(frame,bg="gray")
    frameAside.place(relx=0.6, rely=0.23, relwidth=0.35, relheight=0.55)

    # Marmara Logo
    photo2 = PhotoImage(file="logoImages/logo.gif")
    photoLabel2 = Label(frameAside, image=photo2)
    photoLabel2.config(bg="gray")
    photoLabel2.pack()

    #Close Button
    loginButton = Button(frameAside)
    loginButton.config(text="Kapat", bg="white", fg="black", font=("Calibri", 16), command=close)
    loginButton.pack(fill="x" , pady=10,side=BOTTOM)

    #logButton
    logButton = Button(frameAside)
    logButton.config(text="Personel Giriş Bilgileri", bg="white",fg="black", font=("Calibri", 16), command=passControl)
    logButton.pack(fill="x",side=BOTTOM)

    frameBottom = Frame(tkSystem, bg="white")
    frameBottom.place(relx=0.02, rely=0.84, relwidth=0.96, relheight=0.1)

    # Marmara footer
    footer1 = Label(frameBottom, bg="white", fg="black", text="© Marmara Güvenlik Sistem Başkanlığı")
    footer1.config(font=("Calibri", 12))
    footer1.pack(pady=10)
    footer2 = Label(frameBottom, bg="white", fg="black", text="• Aziz Eren Sağanda    • Melih Afşar")
    footer2.pack(pady=5)

    # get the screen dimension
    screen_width = tkSystem.winfo_screenwidth()
    screen_height = tkSystem.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    tkSystem.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')



    tkSystem.mainloop()

master = Tk()
master.title("Marmara Kamera Guvenlik Sistemi")
master.geometry("1366x768+250+250")
master.config(bg="light blue")
master.resizable(0, 0)

frameTop = Frame(master, bg="#696969")
frameTop.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.94)

# Marmara Logo
photo2 = PhotoImage(file="logoImages/logo.gif")
photoLabel2 = Label(master, image=photo2)
photoLabel2.config(bg="#696969")
photoLabel2.pack(pady=35)

# Baslik
title = Label(master, text="Marmara Kamera Güvenliği Sistemi", font="Verdana 20 bold")
title.config(bg="#696969", fg="white")
title.pack(pady=20)

# Marmara giris Frame
frameLogin = Frame(master, bg="#696969")
frameLogin.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.3)

# Marmara K.Adi Frame
frameKAdi = Frame(frameLogin, bg="#696969")
frameKAdi.place(relx=0, rely=0.05, relwidth=1, relheight=0.2)

# Marmara KSifre Frame
frameKSifre = Frame(frameLogin, bg="#696969")
frameKSifre.place(relx=0, rely=0.25, relwidth=1, relheight=0.2)

# Marmara Login Button Frame
frameButton = Frame(frameLogin, bg="#696969")
frameButton.place(relx=0, rely=0.45, relwidth=1, relheight=0.3)

# Marmara Control information Frame
frameControl = Frame(frameLogin, bg="#696969")
frameControl.place(relx=0, rely=0.85, relwidth=1, relheight=0.1)

frameBottom = Frame(master, bg="white")
frameBottom.place(relx=0.02, rely=0.84, relwidth=0.96, relheight=0.1)

# Marmara footer
footer1 = Label(frameBottom, bg="white", fg="black", text="© Marmara Güvenlik Sistem Başkanlığı")
footer1.config(font=("Calibri", 12))
footer1.pack(pady=10)
footer2 = Label(frameBottom, bg="white", fg="black", text="• Aziz Eren Sağanda    • Melih Afşar")
footer2.pack(pady=5)

# Kullanici Adi
userName = Label(frameKAdi)
userName.config(text="Kullanıcı Adı:", bg="#696969", fg="white", font=("Calibri Italic", 16))
userName.pack(padx=40, side=LEFT)

# Kullanici Adi girisi
getUserName = Entry(frameKAdi)
getUserName.config(bg="white", fg="black", font=("Calibri", 14))
getUserName.pack(padx=40, side=RIGHT)

# Kullanici sifre
userPassword = Label(frameKSifre)
userPassword.config(text="Şifre:", bg="#696969", fg="white", font=("Calibri Italic", 16))
userPassword.pack(padx=40, side=LEFT)

# Kullanici sifre girisi
getUserPassword = Entry(frameKSifre,show="*")
getUserPassword.config(bg="white", fg="black", font=("Calibri", 14))
getUserPassword.pack(padx=40, side=RIGHT)

#Login Button
loginButton = Button(frameButton)
loginButton.config(text="Giriş Yap", bg="white", fg="black", font=("Calibri", 16), command=login)
loginButton.pack(fill="x", padx=40, side=RIGHT)

#Control information
control = Label(frameControl)
control.config(text="Giris yapılmadı.", bg="#696969", fg="white", font=("Calibri Italic", 15))
control.pack()

# LOOP
master.mainloop()