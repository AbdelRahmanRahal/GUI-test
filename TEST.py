import tkinter as tkn

# ----- WINDOW SETTINGS -----
wndw = tkn.Tk()
wndw.title("Test title!")
wndw.geometry("500x500")

lbl = tkn.Label(master=wndw, text="Hello, world!", fg="red")
lbl.grid()

# ----- PROGRAM INITIATION -----
wndw.mainloop()