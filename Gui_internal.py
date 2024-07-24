import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    #User info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()

    if firstname and lastname:
        title = title_combobox.get()
        age = age_spinbox.get()
        items = items_combobox.get()

        print("First name: ", firstname, "Last name: ",lastname)
        print("Title: ", title, "Age:", age, "Items:", items)
        print("-------------------------------------------------")
    else:
        tkinter.messagebox.showwarning(title="Error", message="First name and last name are required")
#ttk= themed tkinter -the is the collection of themed widgets that allow more morden applications for combo box eg
window = tkinter.Tk()
window.title("Julie's Party Hire Store Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

#Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text= "First Name")
first_name_label.grid(row=0,column=0)

last_name_label = tkinter.Label(user_info_frame, text= "Last Name")
last_name_label.grid(row=0,column=1)
                                
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1, column=1)

#list user can choose from
#always specifec parent except root window this is user info frame
title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values= ["", "Ms.", "Mr.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

#spinbox is counter starts at certain number aned can be counted to another number
age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

items_label = tkinter.Label(user_info_frame, text="Items")
items_combobox = ttk.Combobox(user_info_frame, values= ["50 pack of balloons", "ribbons","tassles"])
items_label.grid(row=2,column=1)
items_combobox.grid(row=3, column=1)                        

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Saving Course Info
    #sticky when used  in grid function it means expand in news (north, east, wesst,south
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0, sticky="news", padx=20, pady=20)

registered_label = tkinter.Label(courses_frame,text="Registration Status")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Button
button = tkinter.Button(frame, text="Enter data",command= enter_data)
#why command is here is because it says when this button is clicked go ahead and executee the data from def (define)
#Retrieving the data from the input widgets
button.grid(row=2,column=0, sticky="news", padx=20, pady=20)

window.mainloop()

             

