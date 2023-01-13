from tkinter import *

import ctypes

# Compatibility Settings
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()

root.title("Encryption")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.configure(background="skyblue")

TextInput = Entry(root, font=("Arial", 15))
AsciiValueLabel = Label(
    root, text="Ascii Value: ", font=("Arial", 15), fg="white", bg="royalblue"
)
EncryptedValueLabel = Label(
    root, text="Encrypted Value: ", font=("Arial", 15), fg="white", bg="royalblue"
)


def EncryptValue():
    TextValue = TextInput.get()
    for letter in TextValue:
        AsciiValue = ord(letter)
        EncryptedAsciiValue = (AsciiValue) - 1
        AsciiValueLabel['text'] += f"{AsciiValue} "
        EncryptedValueLabel['text'] += f"{EncryptedAsciiValue} "


EncryptBtn = Button(
    root,
    text="Encrypt Value",
    command=EncryptValue,
    font=("Arial", 15),
    fg="white",
    bg="royalblue",
)

TextInput.place(relx=0.5, rely=0.1, anchor=CENTER)
AsciiValueLabel.place(relx=0.5, rely=0.15, anchor=CENTER)
EncryptedValueLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
EncryptBtn.place(relx=0.5, rely=0.25, anchor=CENTER)


root.mainloop()
