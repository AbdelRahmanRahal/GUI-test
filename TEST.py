import tkinter as tkn

# ----- WINDOW SETTINGS -----
wndw = tkn.Tk()
wndw.configure(bg="#D5E5ED")
wndw.title("Test title!")
wndw.geometry("500x500")

# ----- LABEL TEST -----
lbl = tkn.Label(master=wndw, text="Hello, world!", fg="red", bg="#D5E5ED")
lbl.grid()

# ----- PROGRAM INITIATION -----
wndw.mainloop()