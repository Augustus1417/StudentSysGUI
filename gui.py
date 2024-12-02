from tkinter import *
import modules.student as student,modules.add_student as add_student, modules.search_student as search_student, modules.print_all_students as print_all_students, os, modules.login as login, modules.load_student_data as load_student_data

student_info = student.StudentInfo()
load_data = load_student_data.Load_Student_Data(student_info)
addstud = add_student.AddStudent(student_info)
searchstud = search_student.SearchStudent(student_info)
printstud = print_all_students.Print_All_Students(student_info)
Login = login.Login(student_info)

def hide_other_frames():
    search_student_frame.place_forget()
    output_frame.place_forget()
    add_student_frame.place_forget()

# button commands
def login_func():
    global message, login_status, user_id
    user_id = user_id_box.get()
    message, login_status = Login.login(user_id)
    if login_status:
        login_frame.pack_forget()
        menu_frame.pack(side="left", fill="y")
        content_frame.pack(fill="both", expand=True)
        output_frame.place(relx=0.5, rely=0.5, anchor="center")       
        output_label.config(text=message)
    else:
        notice.config(text=message)
        
def view_my_info():
    hide_other_frames()
    output_frame.place(relx=0.5, rely=0.5, anchor="center") 
    output_label.config(text=searchstud.search_student(user_id))

def search_student_menu():
    hide_other_frames()
    search_student_frame.place(relx=0.5,rely=0.5, anchor="center")

def search_for_student():
    search_output.config(text=searchstud.search_student(search_entry.get()))

def add_student():
    hide_other_frames()
    add_student_frame.place(relx=0.5,rely=0.5, anchor="center")

def register_student():
    new_student = student.StudentInfo()
    name = name_entry.get()
    age = age_entry.get()
    id_num = id_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    add_label.config(text=addstud.registration(new_student, name,age,id_num,email,phone))

def view_all_students():
    hide_other_frames()
    output_frame.place(relx=0.5, rely=0.5, anchor="center") 
    output_label.config(text=printstud.print_all_students())

def logout():
    menu_frame.pack_forget()
    content_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

# main window
win = Tk()
win.title("Student Info System")
win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenwidth()-1280)//2}")

# login frame
login_frame = Frame(win,bg="#1c1e2b")
login_frame.pack(fill="both", expand=True)
float_frame = Frame(login_frame, bg="#24273a", padx=20, pady=20)
float_frame.place(relx=0.5, rely=0.5, anchor="center")
Label(float_frame, text="Login: Enter ID Number", bg="#24273a", fg="white", font=("Arial", "14")).pack(pady=10)
user_id_box = Entry(float_frame, width=20)
user_id_box.pack()
Button(float_frame, text="Login", width=15, command=login_func).pack(pady=10)
notice = Label(float_frame, text="", bg="#24273a", fg="white")
notice.pack()

# menu and content frame
menu_frame = Frame(win,borderwidth=1,bg="#1c1e2b")
content_frame = Frame(win,bg="#171924")
output_frame = Frame(content_frame,borderwidth=1, bg="#171924")
Label(menu_frame, text="Main Menu", bg="#24273a", fg="white", font=("Arial", "16")).pack(pady=10, fill="x")
Label(content_frame,text="Student Info System", bg="#24273a", fg="white", font=("Arial","20")).pack(pady=20)
output_label = Label(output_frame, text="", bg="#24273a",fg="white", font=("Arial", "20"))
output_label.pack()

# search student frame
search_student_frame = Frame(content_frame,borderwidth=1, bg="#171924")
Label(search_student_frame, text="Enter ID Number to search:", font=("Arial", "20")).pack()
search_entry = Entry(search_student_frame,width=10, font=("Arial","16"))
search_entry.pack(pady=(10,1))
Button(search_student_frame,text="Search", font=("Arial","17"), command=search_for_student).pack()
search_output = Label(search_student_frame,text="", font=("Arial","17"))
search_output.pack()

# add student frame
add_student_frame = Frame(content_frame,borderwidth=1, bg="#171924")
Label(add_student_frame,text="Name: ").pack()
name_entry = Entry(add_student_frame,width=10)
name_entry.pack()

Label(add_student_frame,text="Age: ").pack()
age_entry = Entry(add_student_frame,width=10)
age_entry.pack()

Label(add_student_frame,text="ID Number: ").pack()
id_entry = Entry(add_student_frame,width=10)
id_entry.pack()

Label(add_student_frame,text="Email: ").pack()
email_entry = Entry(add_student_frame,width=10)
email_entry.pack()

Label(add_student_frame,text="Phone No.: ").pack()
phone_entry = Entry(add_student_frame,width=10)
phone_entry.pack()

Button(add_student_frame,text="Register", command=register_student).pack()
add_label =Label(add_student_frame,text="")
add_label.pack()
# options
menu_options = {"View My Info": view_my_info,"Search For Student": search_student_menu,
                "Add Student": add_student, "View All Students": view_all_students, "Logout":logout}
for option, function in menu_options.items():
    Button(menu_frame, text=option, command=function, width=25, font=("Arial", "14"), bg="#414868", fg="white").pack(fill="x", pady=10)

win.mainloop()
