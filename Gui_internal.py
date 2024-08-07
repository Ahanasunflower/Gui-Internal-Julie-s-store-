import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

#Ask the user if they want to quit
def quit():
    comfirmation = messagebox.askquestion("Are you are you want to quit?")
    if comfirmation == 'yes':
        window.quit()

#Function to write data to text file
def save_data():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
   # item = items_combobox.get()
  #  quantity = hire_spinbox.get()
    #save_data = button_save.get()
    if firstname !="" and lastname !="":
        with open("data.txt", "a") as file:
            file.write(f"{firstname},{lastname}\n")
        first_name_entry.delete(0,tk.END)
        last_name_entry.delete(0, tk.END)
        messagebox.showinfo("Sucess", "Data saved successfully")
    else:
        messagebox.showwarning("Warning", "Please enter both first and last name")

def display_data():
    try:
        with open("data.txt", "r") as file:
            data = file.readlines
        display_window = tk.Toplevel()
        display_window.title("Data Display")
        text = tk.Text(hire_window)
        text.pack()
        for line in data:
            text.insert(tk.END, line)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No data file found")

        
#To generate receipt
#def receipt():
    random_number_task = random.randint (100000,999999)

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
#ttk= themed tkinter -the is the collection of themed widgets that allow more morden applications for combo box eg

#def customer_reciept():
#    global hire_window
  #  hire_window = tk.Toplevel()
  #  hire_window.title('Customer Details')
 #   hire_window.configure(background='#f7dbc6')
  #  button_save = tk.Button(window, text="Save Data", command=save_data)
 #   button_save.pack()

#Function to write data to text file

#Reciept
#def generste

#Main window setup
window = tk.Tk()
window.title("Julie's Party Hire Store Data Entry Form")
window.geometry('450x350')
window.configure(background='#f7dbc6')

#Header Setup
header_bg_frame = tk.Frame(window, bg='#ebac7c', height=50, width=400)
header_bg_frame.pack()

header_frame =tk.Frame(header_bg_frame, bg ='#f7cbc6')
header_frame.pack()

header_label = tk.Label(header_frame, text="Julie's Party Hire Store", font=("Sans serif", 24), bg= "#f7dbc6")
header_label.pack()

def hire_window():
    global hire_window
    hire_window = tk.Toplevel()
    hire_window.title('Hire')
    hire_window.configure(background='#f7dbc6')

    #Add a frame
    frame= tkinter.Frame(hire_window, bg='#f7dbc6')
    frame.pack()
    #Saving User Info
    user_info_frame = tk.LabelFrame(frame, text="Customer Information", bg= "#f7dbc6")
    user_info_frame.grid(row= 0, column=0, padx=20, pady=20)
    #creating first name etry
    first_name_label = tkinter.Label(user_info_frame, text= "First name", bg ="#f7dbc6")
    first_name_label.grid(row=0,column=0)
 
    #creating last name entry
    last_name_label = tkinter.Label(user_info_frame, text= "Last name")
    last_name_label.grid(row=0,column=1)

    global first_name_entry
    global last_name_entry
    first_name_entry = tkinter.Entry(user_info_frame)
    last_name_entry = tkinter.Entry(user_info_frame)
    first_name_entry.grid(row=1,column=0)
    last_name_entry.grid(row=1, column=1)

    #list user can choose from
    #always specifec parent except root window this is user info frame
    global items_combobox
    items_label = tkinter.Label(user_info_frame, text="Item Hired", bg= "#f7dbc6")
    items_combobox = ttk.Combobox(user_info_frame, values= ["50 pack of balloons", "ribbons","tassles"])
    items_label.grid(row=2,column=0)
    items_combobox.grid(row=3,column=0)

    #spinbox is counter starts at certain number aned can be counted to another number
    global hire_spinbox
    hire_label = tkinter.Label(user_info_frame, text="Number Hired")
    hire_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=110)
    hire_label.grid(row=2,column=1)
    hire_spinbox.grid(row=3, column=1)

    #receipt_label = tkinter.Label(user_info_frame, text="Receipt")

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)
        #Button
    button = tkinter.Button(frame, text="Save Details",command= save_data)
    #why command is here is because it says when this button is clicked go ahead and executee the data from def (define)
    #Retrieving the data from the input widgets
    button.grid(row=2,column=0, sticky="news", padx=20, pady=20)

def return_window():
    global return_window
    return_window = tk.Toplevel()
    return_window.title('Return')
    return_window.configure(background='#f7dbc6')

    #Add a frame
    frame= tkinter.Frame(return_window, bg='#f7dbc6')
    frame.pack()
    #Saving User Info
    user_info_frame = tkinter.LabelFrame(frame, text="Customer Information", bg= "#f7dbc6")
    user_info_frame.grid(row= 0, column=0, padx=20, pady=20)
    #creating first name etry
    first_name_label = tkinter.Label(user_info_frame, text= "First name", bg ="#f7dbc6")
    first_name_label.grid(row=0,column=0)
 
    #creating last name entry
    last_name_label = tkinter.Label(user_info_frame, text= "Last name")
    last_name_label.grid(row=0,column=1)
    global first_name_entry
    global last_name_entry                           
    first_name_entry = tkinter.Entry(user_info_frame)
    last_name_entry = tkinter.Entry(user_info_frame)
    first_name_entry.grid(row=1,column=0)
    last_name_entry.grid(row=1, column=1)

    #list user can choose from
    #always specifec parent except root window this is user info frame
    global items_combobox  
    items_label = tkinter.Label(user_info_frame, text="Item returned", bg= "#f7dbc6")
    items_combobox = ttk.Combobox(user_info_frame, values= ["50 pack of balloons", "ribbons","tassles"])
    items_label.grid(row=2,column=0)
    items_combobox.grid(row=3,column=0)

    #spinbox is counter starts at certain number aned can be counted to another number
    global hire_spinbox
    hire_label = tkinter.Label(user_info_frame, text="Number returned")
    hire_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=110)
    hire_label.grid(row=2,column=1)
    hire_spinbox.grid(row=3, column=1)

    #receipt_label = tkinter.Label(user_info_frame, text="Receipt")

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)
        #Button
           #why command is here is because it says when this button is clicked go ahead and executee the data from def (define)
    #Retrieving the data from the input widgets
    button.grid(row=2,column=0, sticky="news", padx=20, pady=20)

    button_save = tkinter.Button(user_info_frame, text="Save Details",command= save_data)
    button_save.pack()

    button_display = tk.Button(user_info_frame, text="Display Data", command=display_data)
    button_display.pack() 
    
    
#Hire button
button1 = tkinter.Button(window, text = 'Hire', command = hire_window, width= 10, height= 2)
button1.pack(expand = True)

#Return button
button2 = tkinter.Button(window, text = 'Return', command = return_window, width= 10, height= 2)
button2.pack(expand = True)

#Quit button
button3 = tkinter.Button(window, text = 'Quit', command = quit, width= 10, height= 2)
button3.pack(expand = True)



#Able to run the code
window.mainloop()

             

