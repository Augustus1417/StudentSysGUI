from tkinter import *

import student, add_student, search_student, print_all_students, os, login, load_student_data

student_info = student.StudentInfo()
load_data = load_student_data.Load_Student_Data(student_info)
addstud = add_student.AddStudent(student_info)
searchstud = search_student.SearchStudent(student_info)
printstud = print_all_students.Print_All_Students(student_info)
Login = login.Login(student_info)

def gui_log():
    Login.login(user_ID.get())

win = Tk()
win.title("Student Info System")
win.geometry("700x700")

login_lbl = Label(win, text = "Login")
id_lbl = Label(win, text = "Enter Student ID: ")
user_ID = Entry(win , width = 15)
enter_btn = Button(win, text="Enter", command = gui_log)

login_lbl.grid(column=0,row=0)
id_lbl.grid(column=0,row=1)
user_ID.grid(column=1, row= 1)
enter_btn.grid(column=0, row=3)

win.mainloop()