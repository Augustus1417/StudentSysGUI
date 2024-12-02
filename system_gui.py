from tkinter import *
import modules.student as student,modules.add_student as add_student, modules.search_student as search_student, modules.print_all_students as print_all_students, os, modules.login as login, modules.load_student_data as load_student_data

student_info = student.StudentInfo()
load_data = load_student_data.Load_Student_Data(student_info)
addstud = add_student.AddStudent(student_info)
searchstud = search_student.SearchStudent(student_info)
printstud = print_all_students.Print_All_Students(student_info)
Login = login.Login(student_info)

def login():
    global user_id
    user_id = id_entry.get()
    message, login_status = Login.login(user_id)
    msg_lbl.config(text=message)
    if login_status:
        login_frame.pack_forget()
        menu_frame.pack(side="left", fill="y")
        content_frame.pack(fill="both",expand=True)
        output_lbl.config(text=f"Welcome to the Student Info System, {message}!")

def view_info(): output_lbl.config(text=searchstud.search_student(user_id))
def search_student(): pass
def add_student(): pass
def print_all(): pass
def logout():
    menu_frame.pack_forget()
    content_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)
    msg_lbl.config(text="")

win = Tk()
win.title("Student Info Sytem")
win.geometry(f"1000x600+{(win.winfo_screenwidth()-1000)//2}+{(win.winfo_screenheight()-600)//2}")

login_frame = Frame(win, bg="#2c3646")
login_frame.pack(fill="both", expand=True)
login_container = Frame(login_frame, bg="#d4d4d4", padx=30, pady=10)
login_container.place(relx=.5, rely=.5, anchor=CENTER)

Label(login_container, text="Enter ID:", font=("Cascadia Code","18"), bg="#d4d4d4", fg="black").pack(pady=(0,10))
id_entry = Entry(login_container, width=14, font=("Cascadia Code", "15"), relief=FLAT)
id_entry.pack()
Button(login_container, text="Login", command=login, bg="#4f627e", fg="white", font=("Cascadia Code", "14"), relief=FLAT).pack(pady=(20,5))
msg_lbl = Label(login_container, text="", font=("Cascadia Code", "14"), bg="#d4d4d4", fg="black")
msg_lbl.pack()

menu_frame = Frame(win, borderwidth=1,bg="#2c3646")
content_frame = Frame(win, bg="#323e50", padx=20, pady=20)
Label(menu_frame,text="Main Menu", width=15, font=("Cascadia Code", "16"), bg="#d4d4d4").pack(fill="x",pady=(30,30))

output_container = Frame(content_frame, bg="#d4d4d4", padx=20,pady=65)
output_container.place(relx=.5,rely=.5, anchor=CENTER)

output_lbl = Label(output_container, text="", font=("Cascadia Code","17"), bg="#d4d4d4")
output_lbl.pack()

menu_options = {"View Info":view_info, "Search Student":search_student, "Add Student":add_student,
                "Print All Students":print_all, "Logout": logout}
for option, command in menu_options.items():
    Button(menu_frame, text=option, command=command, width=20, font=("Cascadia Code", "14"), fg="white", bg="#4f627e",relief=FLAT).pack(fill="x", pady=1)

win.mainloop()
