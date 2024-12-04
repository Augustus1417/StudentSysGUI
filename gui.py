from tkinter import *
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
        self.login_label.destroy()
        self.id_entry.destroy()
        self.login_btn.destroy()
        self.msg_lbl.destroy()

class Menu_Page:
    def view_info(self):
        self.welcome_label.config(text=searchstud.search_student(login_page.user_id))
    def search_student_page(self): pass
    def add_student_page(self): pass
    def print_all(self): pass
    def logout(self):
        self.destroy_page()
        login_page.view_page()
    
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
        self.welcome_container.destroy()
        self.welcome_label.destroy()

class View_Info_Page:
    def view_page(self):
        pass

class Search_Page:
    def view_page(self):
        pass

    def destroy_page(self):
        pass

login_page = Login_Page()
login_page.view_page()
menu_page = Menu_Page()

win.mainloop()