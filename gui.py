from tkinter import *
import modules.student as student,modules.add_student as add_student, modules.search_student as search_student, modules.print_all_students as print_all_students, os, modules.login as login, modules.load_student_data as load_student_data

student_info = student.StudentInfo()
load_data = load_student_data.Load_Student_Data(student_info)
addstud = add_student.AddStudent(student_info)
searchstud = search_student.SearchStudent(student_info)
printstud = print_all_students.Print_All_Students(student_info)
Login = login.Login(student_info)

# main window
win = Tk()
win.title("Student Info System")

# menu frame
menu_frame = Frame(win,borderwidth=1, bg="black")
menu_frame.pack(side="left", fill="y")

win.mainloop()