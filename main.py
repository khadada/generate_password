from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_fun():
    temp_web=web_name.get()    
    temp_user=user_name.get()    
    temp_pass = password.get() 
    if temp_user =="" or temp_pass==""or temp_web=="":
        messagebox.showerror("Error","All field are required ")
    else:
        is_ok = messagebox.askokcancel(title=f'{temp_web}',message=f"The info will saved is: \nEmail:[{temp_user}]\nPassword[{temp_pass}]")
        if is_ok:
            line = f"{temp_web} | {temp_user} | {temp_pass}\n"
            with open('saved_password.txt',mode="a") as file:
                file.write(line)
            web_name.delete(0,END)
            user_name.delete(0,END)
            password.delete(0,END)
            web_name.focus()
    

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
# entry
web_name = Entry(width=44)
web_name.grid(row=1,column=1,columnspan=2,pady=5)
web_name.focus()
user_name = Entry(width=44)
user_name.grid(row=2,column=1,columnspan=2,pady=5)
user_name.insert(0,"example123@gmail.com")
password = Entry(width=22)
password.grid(row=3,column=1,padx=(0,10),pady=5)
# buttons
Button(text="Generate password").grid(row=3,column=2,padx=(10,0))
Button(text="Add",width=37,command=add_fun).grid(row=4,column=1,columnspan=2,pady=5)
main_window.mainloop()