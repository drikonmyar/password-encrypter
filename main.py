from tkinter import *
from tkinter import messagebox
# import base64
# import os
import config

UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    password=code.get()

    if password==config.pword:
        screen2=Toplevel(screen)
        screen2.title("Decrypted text")
        screen2.geometry("400x200")
        screen2.configure(bg="green")

        message=text1.get(1.0,END)

        decrypt = ""
        for character in message:
            if character.isupper():
                transCharIndex = (UPPER_LETTERS.find(character) - config.upper_change) % 26
                decrypt += UPPER_LETTERS[transCharIndex]
            elif character.islower():
                transCharIndex = (LOWER_LETTERS.find(character) - config.lower_change) % 26
                decrypt += LOWER_LETTERS[transCharIndex]
            else:
                decrypt += character

        # decode_message=message.encode("ascii")
        # base64_bytes=base64.b64decode(decode_message)
        # decrypt=base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="green").place(x=10,y=0)
        text2=Text(screen2,font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10,y=40,width=380, height=150)

        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("Error","Input Password")

    elif password!=config.pword:
        messagebox.showerror("Error","Invalid Password")


def encrypt():
    password=code.get()

    if password==config.pword:
        screen1=Toplevel(screen)
        screen1.title("Encrypted text")
        screen1.geometry("400x200")
        screen1.configure(bg="red")

        message=text1.get(1.0,END)

        encrypt = ""
        for character in message:
            if character.isupper():
                transCharIndex = (UPPER_LETTERS.find(character) + config.upper_change) % 26
                encrypt += UPPER_LETTERS[transCharIndex]
            elif character.islower():
                transCharIndex = (LOWER_LETTERS.find(character) + config.lower_change) % 26
                encrypt += LOWER_LETTERS[transCharIndex]
            else:
                encrypt += character

        # encode_message=message.encode("ascii")
        # base64_bytes=base64.b64encode(encode_message)
        # encrypt=base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="red").place(x=10,y=0)
        text2=Text(screen1,font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10,y=40,width=380, height=150)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("Error","Input Password")

    elif password!=config.pword:
        messagebox.showerror("Error","Invalid Password")


def main_screen():
    
    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("350x400")

    screen.title("Text Enrypter & Decrypter")

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text= "Enter text for encryption and decryption", fg="black", font=
    ("calibri", 13)).place(x=10,y=10)
    text1=Text(font="Roboto 15", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10,y=50,width=330,height=120)

    Label(text= "Enter secret key for encryption and decryption", fg="black", font=
    ("calibri", 13)).place(x=10,y=190)

    code=StringVar()
    Entry(textvariable=code, width=18, bd=0, font=("arial",25), show="*").place(x=10,y=230)

    Button(text="ENCRYPT", height="2", width=20, bg="red", fg="white", bd=0, command=encrypt).place(x=10,y=290)
    Button(text="DECRYPT", height="2", width=20, bg="green", fg="white", bd=0, command=decrypt).place(x=190,y=290)
    Button(text="RESET", height="2", width=46, bg="blue", fg="white", bd=0, command=reset).place(x=10,y=340)

    screen.mainloop()

main_screen()