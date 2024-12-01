from tkinter import *
import modules.student as student,modules.add_student as add_student, modules.search_student as search_student, modules.print_all_students as print_all_students, os, modules.login as login, modules.load_student_data as load_student_data

student_info = student.StudentInfo()
load_data = load_student_data.Load_Student_Data(student_info)
addstud = add_student.AddStudent(student_info)
searchstud = search_student.SearchStudent(student_info)
printstud = print_all_students.Print_All_Students(student_info)
Login = login.Login(student_info)

# button commands
def login_func():
    global message, login_status
    message, login_status = Login.login(user_id_box.get())
    if login_status:
        login_frame.pack_forget()
        menu_frame.pack(side="left", fill="y")
        content_frame.pack(side="left", fill="x")
    else:
        notice.config(text=message)
        
def view_my_info(): print("Your Info")
def search_for_student(): print("student")
def add_student(): print("add")
def view_all_students(): print("all info")
def logout(): print("logout")

# main window
win = Tk()
win.title("Student Info System")
win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenwidth()-1280)//2}")

# login frame
login_frame = Frame(win,bg="#1c1e2b")
login_frame.pack(fill="both", expand=True)
float_frame = Frame(login_frame, bg="#24273a", padx=20, pady=20)
float_frame.place(relx=0.5, rely=0.5, anchor="center")
Label(float_frame, text="Login: Enter ID Number", bg="#24273a", fg="white").pack()
user_id_box = Entry(float_frame, width=20)
user_id_box.pack()
Button(float_frame, text="Login", width=15, command=login_func).pack(pady=10)
notice = Label(float_frame, text="", bg="#24273a", fg="white")
notice.pack()

# menu and content frame
menu_frame = Frame(win,borderwidth=1, bg="black")
content_frame = Frame(win,borderwidth=1, bg="blue")

# options
menu_options = {"View My Info": view_my_info,"Search For Student": search_for_student,
                "Add Student": add_student, "View All Students": view_all_students, "Logout":logout}
for option, function in menu_options.items():
    Button(menu_frame, text=option, command=function, width=25).pack(fill="x")

win.mainloop()
