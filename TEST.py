from tkinter import *
from tkinter import simpledialog
from ConverterFunctions import *

# ----- FUNCTIONS -----
# ----- Title Case -----
def TitleButton():
	outputbox.delete(1.0, END)
	outputbox.insert(END, Title(txtbox.get()))

# ----- UPPERCASE -----
def UpperButton():
	outputbox.delete(1.0, END)
	outputbox.insert(END, txtbox.get().upper())

# ----- lowercase -----
def LowerButton():
	outputbox.delete(1.0, END)
	outputbox.insert(END, txtbox.get().lower())

# ----- AlT CaSe -----
def AltButton():
	outputbox.delete(1.0, END)
	outputbox.insert(END, Alt(txtbox.get()))

# ----- Spell Checker -----
def SpellButton():
	outputbox.delete(1.0, END)
	outputbox.insert(END, Spell(txtbox.get()))

# ----- Caesar Cipher -----
def CaesarButton():
	outputbox.delete(1.0, END)
	dlgbox = simpledialog.askinteger("Caesar Cipher", "Enter number of shifts!", parent=wndw, minvalue=-25, maxvalue=25)
	outputbox.insert(END, Caesar(txtbox.get(), dlgbox))

# ----- Password Generator -----
def PasswordButton():
	outputbox.delete(1.0, END)
	outputbox.insert(END, PasswordGen(txtbox.get(), PGchckboxVar))

# ----- WINDOW SETTINGS -----
wndw = Tk()
wndw.title("Text Converter")
wndw.geometry("720x405")
wndw.configure(bg="#D5E5ED")

# ----- TITLE -----
titlelabel = Label(master=wndw, text="Text Converter\n", font=("Segoe UI", 22, "bold", "underline"), fg="#001061", bg="#D5E5ED")
titlelabel.grid(column=1, columnspan=4)

# ----- BODY -----
# ----- INPUT -----
boxlabel1 = Label(master=wndw, text="Enter text to convert:  ", font=("Segoe UI", 16), fg="#001061", bg="#D5E5ED")
boxlabel1.grid(column=0, row=1)
txtbox = Entry(master=wndw, font=("Segoe UI", 16), fg="#001061", width=45)
txtbox.grid(column=1, row=1, columnspan=5)

linebreak1 = Label(master=wndw, text="", bg="#D5E5ED")
linebreak1.grid(column= 0, row=2, columnspan=6)

# ----- BUTTONS -----
TCbttn = Button(text="Title Case", font=("Segoe UI", 11), fg="#001061", command=TitleButton)
TCbttn.grid(column=1, row=3)
UCbttn = Button(text="UPPERCASE", font=("Segoe UI", 11), fg="#001061", command=UpperButton)
UCbttn.grid(column=2, row=3)
LCbttn = Button(text="lowercase", font=("Segoe UI", 11), fg="#001061", command=LowerButton)
LCbttn.grid(column=3, row=3)
ACbttn = Button(text="AlT CaSe", font=("Segoe UI", 11), fg="#001061", command=AltButton)
ACbttn.grid(column=4, row=3)
SCbttn = Button(text="Spell Check", font=("Segoe UI", 11), fg="#001061", command=SpellButton)
SCbttn.grid(column=5, row=3)

linebreak2 = Label(master=wndw, text="", bg="#D5E5ED")
linebreak2.grid(column= 0, row=4, columnspan=6)

CCbttn = Button(text="Caesar Cipher", font=("Segoe UI", 11), fg="#001061", command=CaesarButton)
CCbttn.grid(column=1, row=5, columnspan=2)
PGbttn = Button(text="Password Generator", font=("Segoe UI", 11), fg="#001061", command=PasswordButton)
PGbttn.grid(column=3, row=5, columnspan=2)

PGchckboxVar = IntVar()
PGchckbox = Checkbutton(master=wndw, text="Allow Spaces", font=("Segoe UI", 11), fg="#001061", bg="#D5E5ED", activebackground="#C4DDEA", onvalue = 1, offvalue = 0, variable=PGchckboxVar)
PGchckbox.grid(column=5, row=5)

linebreak3 = Label(master=wndw, text="\n", bg="#D5E5ED")
linebreak3.grid(column= 0, row=6, columnspan=6)

# ----- OUTPUT -----
boxlabel2 = Label(master=wndw, text="Converted text:", font=("Segoe UI", 16), fg="#001061", bg="#D5E5ED")
boxlabel2.grid(column=0, row=7)
outputbox = Text(master=wndw, height=1, width=45, font=("Segoe UI", 16), fg="#001061")
outputbox.grid(column=1, row=7, columnspan=5)

# ----- PROGRAM INITIATION -----
wndw.mainloop()