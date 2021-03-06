from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    randint(2, 4)
    letter_password = [choice(letters) for _ in range(randint(8, 10))]
    symbole_password = [choice(symbols) for _ in range(randint(2, 4))]
    number_password = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter_password+symbole_password+number_password
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    
    

    #print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_fun():
    temp_web=web_name.get()    
    temp_user=user_name.get()    
    temp_pass = password_entry.get() 
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
            password_entry.delete(0,END)
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
password_entry = Entry(width=22)
password_entry.grid(row=3,column=1,padx=(0,10),pady=5)
# buttons
Button(text="Generate password",command=generate_password).grid(row=3,column=2,padx=(10,0))
Button(text="Add",width=37,command=add_fun).grid(row=4,column=1,columnspan=2,pady=5)
main_window.mainloop()