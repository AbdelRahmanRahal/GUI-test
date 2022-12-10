import tkinter as tkn

# ----- WINDOW SETTINGS -----
wndw = tkn.Tk()
wndw.title("Test title!")
wndw.geometry("500x500")
wndw.configure(bg="#D5E5ED")

# ----- LABEL TEST -----
lbl = tkn.Label(master=wndw, text="Hello, world!", fg="#001061", bg="#D5E5ED", font=("Segoe UI", 20))
lbl.grid()

# ----- PROGRAM INITIATION -----
wndw.mainloop()