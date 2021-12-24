from tkinter import *
import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# main screen
main_window = Tk()
main_window.title("Password generator")
main_window.config(padx=20,pady=20)
# logo img
canvas = Canvas(main_window,height=200,width=200)
canvas.grid(row=0,column=0,columnspan=3)
img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img)
# labels
Label(text="Website: ").grid(row=1,column=0)
Label(text="Username/password: ").grid(row=2,column=0)
Label(text="Password: ").grid(row=3,column=0)



main_window.mainloop()