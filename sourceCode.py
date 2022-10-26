#importing Libraries

from tkinter import *
import random, string
import pyperclip



###initialize window

root =Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")

#heading
heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='DataFlair', font ='arial 15 bold').pack(side = BOTTOM)



###select password length
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()


### Radio buttons for choosing combination
upper = IntVar()
Checkbutton(root, text="UpperCase", variable=upper).pack()
lower = IntVar()
Checkbutton(root, text="LowerCase", variable=lower).pack()
digit = IntVar()
Checkbutton(root, text="Digits", variable=digit).pack()
punc = IntVar()
Checkbutton(root, text="Punctuations", variable=punc).pack()

# Warning Label incase nothing has been selected
warning = Label(root, text = 'SELECT ATLEAST ONE!', font = 'arial 10 bold')

#####define function

pass_str = StringVar()

def Generator():
    password = ''
    set_of_chars=''
    
    # showing warning incase nothing is selected
    if not (upper.get() or lower.get() or digit.get() or punc.get()):
        warning.pack()
        return

    # to turn off warning from previous generate
    if warning.winfo_exists():
        warning.pack_forget()

    # Adding chars based on selected options
    if upper.get():
        password+=random.choice(string.ascii_uppercase)
        set_of_chars+=string.ascii_uppercase
    if lower.get():
        password+=random.choice(string.ascii_lowercase)
        set_of_chars+=string.ascii_lowercase
    if digit.get():
        password+=random.choice(string.digits)
        set_of_chars+=string.digits
    if punc.get():
        password+=random.choice(string.punctuation)
        set_of_chars+=string.punctuation

    for _ in range(pass_len.get()- len(password)):
        password = password+random.choice(set_of_chars)
    pass_str.set(password)
   


###button

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)




# loop to run program
root.mainloop()
