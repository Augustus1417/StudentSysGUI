from tkinter import *
import tkinter.scrolledtext as st
import modules.student as student,modules.add_student as add_student, modules.search_student as search_student, modules.print_all_students as print_all_students, modules.login as login

student_info = student.StudentInfo()
student_info.load_data_from_file()
addstud = add_student.AddStudent(student_info)
searchstud = search_student.SearchStudent(student_info)
printstud = print_all_students.Print_All_Students(student_info)
loginstud = login.Login(student_info)

win = Tk()
win.title("Student Info Sytem")
win.geometry(f"1000x600+{(win.winfo_screenwidth()-1000)//2}+{(win.winfo_screenheight()-600)//2}")

class Login_Page:
    def login(self):
        if self.login_attempts == 5:
            self.login_label.destroy()
            self.id_entry.destroy()
            self.login_btn.destroy()
            self.msg_lbl.config(text="You ran out of attempts.")
            return
        self.user_id = self.id_entry.get()
        message, login_status = loginstud.login(self.user_id)
        if login_status:
            self.destroy_page()
            menu_page.view_page()
            menu_page.welcome_label.config(text=f"Welcome to the Student Info System, {message}!")
        else: 
            self.login_attempts += 1
            self.msg_lbl.config(text=message)

    def view_page(self):
        self.login_attempts = 0
        self.login_frame = Frame(win, bg="#2c3646")
        self.login_container = Frame(self.login_frame, bg="#d4d4d4", padx=30, pady=10)
        self.login_label = Label(self.login_container, text="Enter ID:", font=("Cascadia Code","18"), bg="#d4d4d4", fg="black")
        self.id_entry = Entry(self.login_container, width=14, font=("Cascadia Code", "15"), relief=FLAT)
        self.login_btn = Button(self.login_container, text="Login", command=self.login, bg="#4f627e", fg="white", font=("Cascadia Code", "14"), relief=FLAT)
        self.msg_lbl = Label(self.login_container, text="", font=("Cascadia Code", "14"), bg="#d4d4d4", fg="black")
        self.login_frame.pack(fill="both", expand=True)
        self.login_container.place(relx=.5, rely=.5, anchor=CENTER)
        self.login_label.pack(pady=(0,10))
        self.id_entry.pack()
        self.login_btn.pack(pady=(20,5))
        self.msg_lbl.pack()

    def destroy_page(self):
        self.login_frame.destroy()
        self.login_container.destroy()

class Menu_Page:
    def __init__(self): self.active_page = ""

    def view_info(self):
        self.hide_active_page()
        self.active_page = "view_info"
        view_info_page.view_page()

    def search_student_page(self): 
        self.hide_active_page()
        self.active_page = "search_student_page"
        search_page.view_page()

    def add_student_page(self): 
        self.hide_active_page()
        self.active_page = "add_student_page"
        add_student_page.view_page()

    def print_all(self):
        self.hide_active_page()
        self.active_page = "print_all"
        print_all_page.view_page()

    def logout(self):
        self.active_page = ""
        self.destroy_page()
        login_page.view_page()
    
    def hide_active_page(self):
        if self.welcome_container: self.welcome_container.destroy()
        if self.active_page == "view_info": view_info_page.destroy_page()
        elif self.active_page == "search_student_page": search_page.destroy_page()
        elif self.active_page == "add_student_page": add_student_page.destroy_page()
        elif self.active_page == "print_all": print_all_page.destroy_page()

    def view_page(self):
        self.menu_frame = Frame(win, borderwidth=1,bg="#2c3646")
        self.content_frame = Frame(win, bg="#323e50", padx=20, pady=20)
        self.menu_label = Label(self.menu_frame,text="Main Menu", width=15, font=("Cascadia Code", "16"), bg="#d4d4d4")
        self.welcome_container = Frame(self.content_frame, bg="#d4d4d4", padx=20,pady=40)
        self.welcome_label = Label(self.welcome_container, text="", font=("Cascadia Code","17"), bg="#d4d4d4")
        self.menu_frame.pack(side="left", fill="y")
        self.menu_label.pack(fill="x", pady=30)
        self.content_frame.pack(fill="both",expand=True)
        self.welcome_container.place(relx=.5,rely=.5, anchor=CENTER)
        self.welcome_label.pack()
        self.menu_options = {"View Info":self.view_info, "Search Student":self.search_student_page, "Add Student":self.add_student_page,
                            "Print All Students":self.print_all, "Logout": self.logout}
        for option, command in self.menu_options.items():
            Button(self.menu_frame, text=option, command=command, width=20, font=("Cascadia Code", "14"), fg="white", bg="#4f627e",relief=FLAT).pack(fill="x", pady=1)

    def destroy_page(self):
        self.menu_frame.destroy()
        self.content_frame.destroy()

class View_Info_Page:
    def view_page(self):
        self.info_container = Frame(menu_page.content_frame, bg="#d4d4d4", padx=30,pady=40)
        self.info_container.place(relx=.5,rely=.5, anchor=CENTER)
        Label(self.info_container,text="Your Information:", font=("Cascadia Code", "17"), bg="#d4d4d4").pack(pady=(0,10))
        Label(self.info_container,text=searchstud.search_student(login_page.user_id), font=("Cascadia Code", "15"), bg="#d4d4d4", anchor="e", justify=LEFT).pack()

    def destroy_page(self): self.info_container.place_forget()

class Search_Page:
    def search(self): self.search_output.config(text=searchstud.search_student(self.search_entry.get()))
    def view_page(self):
        self.search_container = Frame(menu_page.content_frame, bg="#d4d4d4", padx=30,pady=40)
        self.search_container.place(relx=.5,rely=.5, anchor=CENTER)
        Label(self.search_container,text="Search Student:", font=("Cascadia Code", "17"), bg="#d4d4d4").grid(row=0, column=0)
        Label(self.search_container,text="Enter ID:", font=("Cascadia Code", "15"), bg="#d4d4d4").grid(row=1, column=0)
        self.search_entry = Entry(self.search_container, width=14, font=("Cascadia Code", "14"), relief=FLAT)
        self.search_entry.grid(row=1,column=1)
        self.search_btn = Button(self.search_container, text="Search", command=self.search, bg="#4f627e", fg="white", font=("Cascadia Code", "13"), relief=FLAT)
        self.search_btn.grid(row=1,column=2, padx=(20,0))
        self.output_frame = Frame(self.search_container, bg="#d4d4d4")
        self.output_frame.grid(row=2, column=0, columnspan=3, pady=(20, 0))
        Label(self.output_frame, text="Result:", font=("Cascadia Code", 15), bg="#d4d4d4",anchor="w", justify=LEFT).pack()
        self.search_output = Label(self.output_frame, text="", font=("Cascadia Code", 14), bg="#d4d4d4", anchor="w", justify=LEFT)
        self.search_output.pack(fill="x")

    def destroy_page(self): self.search_container.destroy()

class Add_Student_Page:
    def add_new_student(self):
        errors = []
        if self.name_entry.get() == "": errors.append("- Name cannot be empty\n")
        if self.age_entry.get() == "": errors.append("- Age cannot be empty\n")
        if self.id_num_entry.get() == "": errors.append("- ID cannot be empty\n")
        if self.email_entry.get() == "": errors.append("- Email cannot be empty\n")
        if self.phone_entry.get() == "": errors.append("- Phone No. cannot be empty")

        if not errors: 
            self.output_lbl.config(text=addstud.registration(self.name_entry.get(), self.age_entry.get(), self.id_num_entry.get(), self.email_entry.get(), self.phone_entry.get()), fg="black")
            self.name_entry.delete(0,'end')
            self.age_entry.delete(0,'end')
            self.id_num_entry.delete(0,'end')
            self.email_entry.delete(0,'end')
            self.phone_entry.delete(0,'end')
        else: self.output_lbl.config(text=f"Warning!\n{''.join(errors)}", fg="red")
    def view_page(self):
        self.add_container = Frame(menu_page.content_frame, bg="#d4d4d4", padx=30,pady=40)
        self.add_container.place(relx=.5,rely=.5, anchor=CENTER)
        Label(self.add_container,text="Add New Student:", font=("Cascadia Code", "17"), bg="#d4d4d4").grid(row=0, column=0)

        Label(self.add_container,text="Name:", font=("Cascadia Code", "15"), bg="#d4d4d4").grid(row=1, column=0)
        self.name_entry = Entry(self.add_container, width=18, font=("Cascadia Code", "14"), relief=FLAT)
        self.name_entry.grid(row=1,column=1)

        Label(self.add_container,text="Age:", font=("Cascadia Code", "15"), bg="#d4d4d4").grid(row=2, column=0)
        self.age_entry = Entry(self.add_container, width=18, font=("Cascadia Code", "14"), relief=FLAT)
        self.age_entry.grid(row=2,column=1)

        Label(self.add_container,text="ID Number:", font=("Cascadia Code", "15"), bg="#d4d4d4").grid(row=3, column=0)
        self.id_num_entry = Entry(self.add_container, width=18, font=("Cascadia Code", "14"), relief=FLAT)
        self.id_num_entry.grid(row=3,column=1)
    
        Label(self.add_container,text="Email:", font=("Cascadia Code", "15"), bg="#d4d4d4").grid(row=4, column=0)
        self.email_entry = Entry(self.add_container, width=18, font=("Cascadia Code", "14"), relief=FLAT)
        self.email_entry.grid(row=4,column=1)

        Label(self.add_container,text="Phone No.:", font=("Cascadia Code", "15"), bg="#d4d4d4").grid(row=5, column=0)
        self.phone_entry = Entry(self.add_container, width=18, font=("Cascadia Code", "14"), relief=FLAT)
        self.phone_entry.grid(row=5,column=1)

        self.add_btn = Button(self.add_container, text="Register", command=self.add_new_student, bg="#4f627e", fg="white", font=("Cascadia Code", "13"), relief=FLAT)
        self.add_btn.grid(row=6,column=0, pady=(10,0))

        self.output_frame = Frame(self.add_container, bg="#d4d4d4")
        self.output_frame.grid(row=7, column=0, columnspan=3, pady=(20, 0))
        Label(self.output_frame, text="Result:", font=("Cascadia Code", 15), bg="#d4d4d4",anchor="w", justify=LEFT).pack()
        self.output_lbl = Label(self.output_frame, text="", font=("Cascadia Code", 14), bg="#d4d4d4", anchor="w", justify=LEFT)
        self.output_lbl.pack(fill="x")

    def destroy_page(self): self.add_container.destroy()

class Print_All_Page:
    def view_page(self):
        self.all_students_container = Frame(menu_page.content_frame, bg="#d4d4d4", padx=30,pady=40)
        self.all_students_container.place(relx=.5,rely=.5, anchor=CENTER)
        Label(self.all_students_container,text="All Students:", font=("Cascadia Code", "17"), bg="#d4d4d4").pack(pady=(0,20))
        self.output_area = st.ScrolledText(self.all_students_container,font=("Cascadia Code", "14"), bg="#d4d4d4", width=50, height=10)
        self.output_area.insert(INSERT, printstud.print_all_students())
        self.output_area.config(state=DISABLED)
        self.output_area.pack()
    
    def destroy_page(self): self.all_students_container.destroy()

login_page = Login_Page()
login_page.view_page()
menu_page = Menu_Page()
view_info_page = View_Info_Page()
search_page = Search_Page()
add_student_page = Add_Student_Page()
print_all_page = Print_All_Page()

win.mainloop()