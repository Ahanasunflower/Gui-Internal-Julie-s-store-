import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import random

# Set to store the used receipt numbers to ensure no receipt number is repeated to be unique.
used_receipt_numbers= set()

# Function to ask the customer if they want to quit.
def quit_form():
    comfirmation = messagebox.askquestion("Quit","Are you sure you want to quit?")
    if comfirmation == 'yes':
        main_window.destroy()
        
# Function to validate the correctness of the customer's data.
def validate_data():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    item = items_combobox.get()
    amount = hire_spinbox.get()

    # Validating each different field's input.
    if firstname == "" or lastname == "" or item == "":
        messagebox.showerror("Error", "Please fill in all fields.")
        return False
    if not firstname.isalpha() or not lastname.isalpha():
        messagebox.showerror("Error", "Names can't contain special characters.")
        return False
    if not amount.isdigit():
        messagebox.showerror("Error", "Only numbers are valid for 'Number Hired'")
        return False
    if not (1 <=int(amount) <=500):
        messagebox.showerror("Error", "Amount to hire must be between 1 and 500.")
        return False
    return True

# Function that generates random receipt number.
def receipt():
    while True:
        receipt_number = random.randint(100000,999999)
        if receipt_number not in used_receipt_numbers:
            used_receipt_numbers.add(receipt_number)
            return receipt_number

# Function to save customer data and write it to a text file.
def save_data():
    if validate_data():
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        item = items_combobox.get()
        amount = hire_spinbox.get()
        receipt_number = receipt()
        
        # Save customer data to file(customer_details.txt).
        with open("customer_details.txt", "a") as file:
            file.write(f"First name: {firstname}, Last name: {lastname}, Item: {item}, Amount: {amount}, Receipt: {receipt_number}\n")
        # Reset input fields to default values (original).
        first_name_entry.delete(0,tk.END)
        last_name_entry.delete(0, tk.END)
        items_combobox.set('')
        hire_spinbox.delete(0,tk.END)
        hire_spinbox.insert(0,1)
        messagebox.showinfo("Success!", f"Data saved successfully with receipt number:{receipt_number}")

# Function to display all saved customer details.
def display_data():
    try:
        with open("customer_details.txt", "r") as file:
            data = file.readlines()
        display_window = tk.Toplevel()
        display_window.title("Display Hire Details")
        text = tk.Text(display_window)
        text.pack()
        for line in data:
            text.insert(tk.END, line)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No data file found")

# Function to delete customer details by receipt number.
def delete_details():   
    receipt_number = delete_entry.get().strip()

    if not receipt_number.isdigit():
        messagebox.showwarning("Warning", "Please enter only numbers for the receipt number.")
        return
    
    receipt_found = False
    try:
        with open("customer_details.txt", "r") as file:
            lines = file.readlines()
        with open("customer_details.txt", "w") as file:
            for line in lines:
                if not line.strip().endswith(receipt_number):
                    file.write(line)
                else:
                    receipt_found = True
                    
        if receipt_found:
           messagebox.showinfo("Sucess", f"Details with receipt number:  {receipt_number} deleted successfully")
        else:
            messagebox.showwarning("Warning", f" Receipt number not found")
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No data file found")

def hire_window():
    global hire_window
    hire_window = tk.Toplevel()
    hire_window.title('Hire and Return')
    hire_window.configure(background='#f7dbc6')

    # Adds a frame in the hire window.
    frame= tkinter.Frame(hire_window, bg='#f6dbc6')
    frame.pack(padx=20,pady=20)

    # Makes a frame titled just for customer information.
    user_info_frame = tk.LabelFrame(frame, text="Customer Information", bg= "#f7dbc6",font=("Arial",12,"bold"))
    user_info_frame.grid(row= 0, column=0, padx=20, pady=20)

    # Creates first name entry.
    first_name_label = tkinter.Label(user_info_frame, text= "First name", bg ="#f7dbc6")
    first_name_label.grid(row=0,column=0)
    global first_name_entry
    first_name_entry = tkinter.Entry(user_info_frame)
    first_name_entry.grid(row=1,column=0)
    
    # Creates last name entry.
    last_name_label = tkinter.Label(user_info_frame, text= "Last name", bg= "#f7dbc6")
    last_name_label.grid(row=0,column=1)
    global last_name_entry
    last_name_entry = tkinter.Entry(user_info_frame)
    last_name_entry.grid(row=1, column=1)

    # Creates a list of items customers can choose from in a combobox.
    global items_combobox
    items_label = tkinter.Label(user_info_frame, text="Item Hired", bg= "#f7dbc6")
    items_combobox = ttk.Combobox(user_info_frame, values= ["Balloons", "Ribbons","Tassels","Candles","Straws"], state="readonly")
    items_label.grid(row=2,column=0)
    items_combobox.grid(row=3,column=0)

    # Creates a spinbox for the amount the customer wants to hire set with the default 1 to 500 as the number.
    global hire_spinbox
    hire_label = tkinter.Label(user_info_frame, text="Number Hired", bg= "#f7dbc6")
    hire_spinbox = tkinter.Spinbox(user_info_frame, from_=1, to=500)
    hire_label.grid(row=2,column=1)
    hire_spinbox.grid(row=3, column=1)
    
    # Configure all widgets in user_info_frame to have the same padding to keep the Gui layout consistent.
    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Creates a save button that saves customer's hire details.
    button_save = tkinter.Button(frame, text="Save Hire Details",command= save_data)
    button_save.grid(row=2,column=0, sticky="news", padx=20, pady=10)
    
    # Display button (displays saved customer details).
    button_display = tk.Button(frame, text="Display Details", command=display_data)
    button_display.grid(row=3,column=0, sticky="news", padx=20, pady=10)

    # Creates a delete (return) user's entry frame label for the customer.
    delete_frame = tk.Frame(frame, bg='#f7dbc6')
    delete_frame.grid(row=4, column=0, padx=20, pady=20)
    delete_label = tk.Label(delete_frame, text="Enter receipt number to return:", bg="#f7dbc6")
    delete_label.grid(row=0, column=0, padx=10, pady=5)

    # Creates a delete entry to delete customer's details by their receipt number.
    global delete_entry
    delete_entry= tk.Entry(delete_frame)
    delete_entry.grid(row=1, column=0, padx=10, pady=5)
    delete_button = tk.Button(delete_frame, text ="Return Items",command=delete_details)
    delete_button.grid(row=2, column=0, sticky="news", padx=10, pady=5)                 
    
# Main window setup.
main_window = Tk()
main_window.title("Julie's Party Hire Store")
main_window.geometry('275x455')
main_window.configure(background='#f7dbc6')

# Julie's Party Hire Store Logo is laid out on the main window (menu).
party_img = PhotoImage(file="julies_party.png")
image_label = Label(main_window, image=party_img, bg='#f7dbc6', width= 250, height= 250)
image_label.grid(column= 1, row=0, sticky="news", padx=10, pady=10)

# Hire/Return (for deletion) button.
hire_button = tkinter.Button(main_window, text = 'Hire', bg='#eda6ab', font=("Arial", 12, "bold"),command = hire_window, width= 15, height= 3)
hire_button.grid(column=1, row=1, sticky="news", padx=10, pady=10)

# Quit button.
quit_button = tk.Button(main_window, text = 'Quit', bg='#eda6ab', font=("Arial", 12, "bold"), command = quit_form, width= 15, height= 3)
quit_button.grid(column=1, row=2, sticky="news", padx=10, pady=10)

# Able to run the code.
main_window.mainloop()
