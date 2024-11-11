from tkinter import *
import student, add_student, search_student, print_all_students, os, login, load_student_data

student_info = student.StudentInfo()
load_data = load_student_data.Load_Student_Data(student_info)
addstud = add_student.AddStudent(student_info)
searchstud = search_student.SearchStudent(student_info)
printstud = print_all_students.Print_All_Students(student_info)
Login = login.Login(student_info)

login_status = False

def gui_login():
    login_message, login_status = Login.login(id_input.get())
    if login_status:
        greeting.config(text=login_message)
        view_btn.config(state=NORMAL)
        search_btn.config(state=NORMAL)
        search_id.config(state=NORMAL)
    else: 
        greeting.config(text=login_message)
        view_btn.config(state=DISABLED)

def view_info():
    result.config(text = searchstud.search_student(id_input.get()))

def gui_search():
    result.config(text =searchstud.search_student(search_id.get()))
    
# Title & Size
win = Tk()
win.title("Student Info System")
win.geometry("650x450+600+300")

# Login Section
id_lbl = Label(win, text="Enter User ID :")
id_lbl.grid(row=0, column=0)

id_input = Entry(win, width=15)
id_input.grid(row=0, column=1)

login_btn = Button(win, text="Login", command=gui_login)
login_btn.grid(row=0, column=2)

greeting = Label(win,text="")
greeting.place(x=1,y=30)

# Menu
view_btn = Button(win, text="View your information", command=view_info)
view_btn.place(x=1,y=60)
view_btn.config(state=DISABLED)

search_id = Entry(win, width=15)
search_id.place(x=1,y=90)
search_btn = Button(win, text="Search for a student.", command=gui_search)
search_btn.place(x=1,y=120)
search_btn.config(state=DISABLED)

result = Label(win,text="result")
result.place(x=300,y=120)
win.mainloop()
