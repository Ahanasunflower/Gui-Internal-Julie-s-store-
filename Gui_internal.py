import tkinter 
from tkinter import ttk
from tkinter import messagebox

def quit():
    main_window.destroy()

#def receipt():
    #random_number_task = random.randint (1,80000)

def print_details():
    #User info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()

    if firstname and lastname:
        hire = hire_spinbox.get()
        items = items_combobox.get()

        print("First name: ", firstname, "Last name: ",lastname)
        print("Number Hired:", hire, "Items:", items)
        print("-------------------------------------------------")
    else:
        tkinter.messagebox.showwarning(title="Error", message="First name and last name are required")
#ttk= themed tkinter -the is the collection of themed widgets that allow more morden applications for combo box eg
window = tkinter.Tk()
window.title("Julie's Party Hire Store Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Add background color
window.configure(background='#f7dbc6')

frame = tkinter.Frame(window, bg='#f7dbc6')
frame.pack()

#Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information", bg= "#f7dbc6")
user_info_frame.grid(row= 0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text= "First name")
first_name_label.grid(row=0,column=0)

last_name_label = tkinter.Label(user_info_frame, text= "Last name")
last_name_label.grid(row=0,column=1)
                                
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1, column=1)

#list user can choose from
#always specifec parent except root window this is user info frame

items_label = tkinter.Label(user_info_frame, text="Item Hired", bg= "#f7dbc6")
items_combobox = ttk.Combobox(user_info_frame, values= ["50 pack of balloons", "ribbons","tassles"])
items_label.grid(row=2,column=0)
items_combobox.grid(row=3,column=0)

#spinbox is counter starts at certain number aned can be counted to another number
hire_label = tkinter.Label(user_info_frame, text="Number Hired")
hire_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=110)
hire_label.grid(row=2,column=1)
hire_spinbox.grid(row=3, column=1)

#receipt_label = tkinter.Label(user_info_frame, text="Receipt")


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#Button
button = tkinter.Button(frame, text="Print Details",command= print_details)
#why command is here is because it says when this button is clicked go ahead and executee the data from def (define)
#Retrieving the data from the input widgets
button.grid(row=2,column=0, sticky="news", padx=20, pady=20)



window.mainloop()

             

