import tkinter
from  tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import random
#from tkinter import PhotoImage


#Function to Ask the customer if they want to quit and quits
def quit_form():
    comfirmation = messagebox.askquestion("Quit","Are you sure you want to quit?")
    if comfirmation == 'yes':
        main_window.destroy()

def validate_data(firstname, lastname, amount):
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    item = items_combobox.get()
    amount = hire_spinbox.get()
    receipt_number = receipt()
    if not firstname.isalpha() or not lastname.isalpha():
        messagebox.showerror("Error", "Names can't contain special characters.")
        return False
    if not (1 <=int(amount) <=200):
        messagebox.showerror("Error", "Amount to hire must be between 1 and 200.")
        return False
    if firstname =="" or lastname =="" or items_combobox.get() == "":
        messagebox.showerror("Error", "Please fill in all fields.")
        return False
    return True

#Function to write data to text file and save hire details
def save_data():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    item = items_combobox.get()
    amount = hire_spinbox.get()
    receipt_number = receipt()

    if firstname !="" and lastname !="" and amount:
        with open("customer_details.txt", "a") as file:
            file.write(f"{firstname},{lastname},{item},{amount},{receipt_number}\n")
        first_name_entry.delete(0,tk.END)
        last_name_entry.delete(0, tk.END)
        messagebox.showinfo("Success!", f"Data saved successfully with receipt number:{receipt_number}")
   # else:
        #messagebox.showwarning("Warning", "Please enter both first and last name")

#Function to display customer details
def display_data():
    try:
        with open("customer_details.txt", "r") as file:
            data = file.readlines()
        display_window = tk.Toplevel()
        display_window.title("Display Data")
        text = tk.Text(display_window)
        text.pack()
        for line in data:
            text.insert(tk.END, line)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No data file found")

#Function that generates random receipt number
def receipt():
    #global generate_receipt
    return random.randint(100000,999999)

#Function to delete customer details by receipt number
#Use list like if receipt_number is here then minus row
def delete_details():
    receipt_number = delete_entry.get()
    if receipt_number:
        try:
            with open("customer_details.txt", "r") as file:
                lines = file.readlines()
            with open("customer_details.txt", "w") as file:
                for line in lines:
                    if not line.strip().endswith(receipt_number):
                        file.write(line)
                    else:
                        print(f"Deleted!: {line.strip()}") #Debug
            messagebox.showinfo("Sucess", f"Details with receipt number: {receipt_number} deleted successfully")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No data file found")
    else:
        messagebox.showwarning("Warning", "Please enter a valid receipt number")

#def function to generate receipt number
#def generate_receipt_number():
    #while True:
       # randInt = random.randint(100000, 999999)
        #if randInt not in used_receipt_numbers:
          #  used_receipt_numbers.add(randInt)
          #  return randInt
        
#Save hire details and print
#def print_details():
    
    #receipt =
    
#    if firstname and lastname and item and quantity:
  #      hire = hire_spinbox.get()
   #     items = items_combobox.get()
 #       print("First name: ", firstname, "Last name: ",lastname)
    #    print("Number Hired:", hire, "Items:", items)
     #   print("-------------------------------------------------")
   # else:
    #    tkinter.messagebox.showwarning(title="Error", message="First name and last name are required")

def hire_window():
    global hire_window
    hire_window = tk.Toplevel()
    hire_window.title('Hire and Return')
    hire_window.configure(background='#f7dbc6')

    #Add a frame
    frame= tkinter.Frame(hire_window, bg='#f6dbc6')
    frame.pack(padx=20,pady=20)

    #Saving User Info
    user_info_frame = tk.LabelFrame(frame, text="Customer Information", bg= "#f7dbc6",font=("Arial",12,"bold"))
    user_info_frame.grid(row= 0, column=0, padx=20, pady=20)

    #Creating first name entry
    first_name_label = tkinter.Label(user_info_frame, text= "First name", bg ="#f7dbc6")
    first_name_label.grid(row=0,column=0)
    global first_name_entry
    first_name_entry = tkinter.Entry(user_info_frame)
    first_name_entry.grid(row=1,column=0)
    
    #Creating last name entry
    last_name_label = tkinter.Label(user_info_frame, text= "Last name", bg= "#f7dbc6")
    last_name_label.grid(row=0,column=1)
    global last_name_entry
    last_name_entry = tkinter.Entry(user_info_frame)
    last_name_entry.grid(row=1, column=1)

    #List of items user can choose from
    #Always specifec parent except root window this is user info frame
    global items_combobox
    items_label = tkinter.Label(user_info_frame, text="Item Hired", bg= "#f7dbc6")
    items_combobox = ttk.Combobox(user_info_frame, values= ["Balloons", "Ribbons","Tassels","Candles","Straws"], state="readonly")
    items_label.grid(row=2,column=0)
    items_combobox.grid(row=3,column=0)

    #Spinbox is counter starts at certain number aned can be counted to another number
    #Spinbox to select the number of items hired
    global hire_spinbox
    hire_label = tkinter.Label(user_info_frame, text="Number Hired", bg= "#f7dbc6")
    hire_spinbox = tkinter.Spinbox(user_info_frame, from_=1, to=110)
    hire_label.grid(row=2,column=1)
    hire_spinbox.grid(row=3, column=1)
#Configure all widgets to have same padding
    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    #Save details button
    button_save = tkinter.Button(frame, text="Save Hire Details",command= save_data)
    button_save.grid(row=2,column=0, sticky="news", padx=20, pady=10)
    
    #why command is here is because it says when this button is clicked go ahead and executee the data from def (define)
    #Retrieving the data from the input button_save.grid(row=2,column=0, sticky="news", padx=20, pady=20)

    #Display button (displays saved details)
    button_display = tk.Button(frame, text="Display Data", command=display_data)
    button_display.grid(row=3,column=0, sticky="news", padx=20, pady=10)

    #Delete (return) user's entry  by receipt number
    delete_frame = tk.Frame(frame, bg='#f7dbc6')
    delete_frame.grid(row=4, column=0, padx=20, pady=20)

    delete_label = tk.Label(delete_frame, text="Delete by receipt number:", bg="#f7dbc6")
    delete_label.grid(row=0, column=0, padx=10, pady=5)
    global delete_entry
    delete_entry= tk.Entry(delete_frame)
    delete_entry.grid(row=1, column=0, padx=10, pady=5)
    delete_button = tk.Button(delete_frame, text ="Return",command=delete_details)
    delete_button.grid(row=2, column=0, sticky="news", padx=10, pady=5)                 
    
#Main window setup
main_window = Tk()
main_window.title("Julie's Party Hire Store Data Entry Form")
main_window.geometry('275x455')
main_window.configure(background='#f7dbc6')


#Header Setup
#header_bg_frame = tk.Frame(main_window, bg='#f5e3d3', height=50, width=400)#not working
#header_bg_frame.pack()


party_img = PhotoImage(file="julies_party.png")

image_label = Label(main_window, image=party_img, bg='#f7dbc6', width= 250, height= 250)
image_label.grid(column= 1, row=0, sticky="news", padx=10, pady=10)

#IMAGE_PATH = "C:/Users/OneDrive/Ahana - Lynfield College/2PAD/Ahana Lal - 91897 and 91896 Assessment"

#IMAGE_PATH = "C:/Users/akokatnur/OneDrive - Lynfield College/Desktop/Python"
#header_frame =tk.Frame(header_bg_frame, bg ='#f5e3d3', height=50, width=400)#not working
#header_frame.pack()

#header_label = tk.Label(header_frame, text="Julie's Party Hire Store", font=("Sans serif", 24), bg= "#f7dbc6")
#header_label.pack()
#Hire/Return button
button1 = tkinter.Button(main_window, text = 'Hire', font=("Arial", 12, "bold"),command = hire_window, width= 15, height= 3)
button1.grid(column=1, row=1, sticky="news", padx=10, pady=10)

#Quit button
button3 = tk.Button(main_window, text = 'Quit', font=("Arial", 12, "bold"), command = quit_form, width= 15, height= 3)
button3.grid(column=1, row=2, sticky="news", padx=10, pady=10)

#Able to run the code
main_window.mainloop()
