import customtkinter as ctk 
import tkinter.messagebox as tkmb
import tkinter as tk
import openpyxl
import random
import secrets
import pandas as pd
from ff3 import FF3Cipher

# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 
  
# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 
  


def login():
  
    username = "priyaa"
    password = "123LD"
    
    if user_entry.get() == username and user_pass.get() == password: 
        tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
        app.withdraw()
        #ctk.CTkLabel(register_window).pack()
        register_window.deiconify()
    elif user_entry.get() == username and user_pass.get() != password: 
        tkmb.showwarning(title='Wrong password',message='Please check your password') 
    elif user_entry.get() != username and user_pass.get() == password: 
        tkmb.showwarning(title='Wrong username',message='Please check your username') 
    else: 
        tkmb.showerror(title="Login Failed",message="Invalid Username and password")



def register():
    # Get customer details from entry widgets
    name = name_entry.get()
    cardno = cardno_entry.get()
    expiry = expiry_entry.get()
    cvvno = cvv_entry.get()

    # Check if card number already exists
    if(check_existing_card_number(cardno)):
        tkmb.showerror("Error", "Card number already exists")
        return

    # Validate card number, account number, and CVV
    if not (validate_card_number(cardno)):
        tkmb.showerror("Error", "Invalid input")
        return
    
    if not (validate_cvv_number(cvvno)):
        tkmb.showerror("Error", "Invalid input")
        return

    # Perform encryption
    encrypted_card_number, key = encrypt_card_number(cardno)

    # Save data to Excel
    save_to_excel(name, cardno, expiry, cvvno, encrypted_card_number, key)
    tkmb.showinfo("Success", "Registration successful")

app = ctk.CTk() 
app.geometry("400x400") 
app.title("AUB")

label = ctk.CTkLabel(app,text="AU Banking")  
label.pack(pady=20)

frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True)

user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10)

user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10)

button = ctk.CTkButton(master=frame,text='Login',command=login) 
button.pack(pady=12,padx=10) 
  
checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
checkbox.pack(pady=12,padx=10)

register_window = ctk.CTkToplevel(app)
register_window.title("Customer Registration")
register_window.geometry("350x350")
register_window.withdraw()

frame = ctk.CTkFrame(master=register_window) 
frame.pack(pady=20,padx=40,fill='both',expand=True)

name_entry = ctk.CTkEntry(master=frame,placeholder_text="CardHolder_Name")
name_entry.pack(pady=12,padx=10)

cardno_entry = ctk.CTkEntry(master=frame,placeholder_text="Card_Number")
cardno_entry.pack(pady=12,padx=10)

expiry_entry = ctk.CTkEntry(master=frame,placeholder_text="Expiry_date")
expiry_entry.pack(pady=12,padx=10)

cvv_entry = ctk.CTkEntry(master=frame,placeholder_text="CVV_no")
cvv_entry.pack(pady=12,padx=10)

register_button = ctk.CTkButton(master=frame, text="Register", command=register)
register_button.pack(pady=12,padx=10)

def check_existing_card_number(cardno):
        # Here you would check if the card number already exists in your database
        # For simplicity, I'll just use a dummy list
        dummy_card_numbers = ["1234567890123456", "2345678901234567", "3456789012345678"]
        return cardno in dummy_card_numbers
        
def validate_card_number(cardno):
    return len(cardno) == 16 and cardno.isdigit()
    
def validate_cvv_number(cvvno):
    return len(cvvno) == 3 and cvvno.isdigit()

def encrypt_card_number(cardno):
    key = secrets.token_hex(16)
    tweak = "D8E7920AFA330A73"
    c = FF3Cipher(key, tweak)

    #plaintext = "1234567890123456"
    encrypted_card_number = c.encrypt(cardno)
    #decrypted = c.decrypt(encrypted_card_number)
    return encrypted_card_number, key

def save_to_excel(name, cardno, expiry, cvvno, encrypted_card_number, key):
    data = {
        "Cardholder Name": [name],
        "Card Number": [cardno],
        "Expiry Date": [expiry],
        "CVV": [cvvno],
        "Encrypted Card Number": [encrypted_card_number],
        "Key": [key]
    }

    df = pd.DataFrame(data)
    df.to_csv('filepath', mode='a', index = False)


app.mainloop()
