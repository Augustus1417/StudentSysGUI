import student, add_student, search_student, print_all_students, os, login, load_student_data

student_info = student.StudentInfo()
load_data = load_student_data.Load_Student_Data(student_info)
addstud = add_student.AddStudent(student_info)
searchstud = search_student.SearchStudent(student_info)
printstud = print_all_students.Print_All_Students(student_info)
Login = login.Login(student_info)
                                
class Main_Menu:
    def login(self):
        print("\n====== Login - Student Info. System =====")
        for _ in range(3):
            global userId
            userId = input("\nEnter Student ID: ")
            if Login.login(userId): self.main()
        print("\nYou ran out of attempts, program will now close...")

    def main(self):
        while True:
            print("\n=============== Main Menu ===============")
            menu = input("\nPlease choose from the following options\n1. View your information\n2. View other student's information\n3. Register a New Student\n4. Print all students in the list\n5. Exit\n\nYour choice: ")
            if menu == "1": 
                os.system('cls')
                searchstud.search_student(userId) 
            elif menu == "2": 
                os.system('cls')
                print("\n========== Search Student ==========")
                while True:
                    id_num = input("\nEnter Student ID: ")
                    searchstud.search_student(id_num)
                    again = input("Do you want to view another student?(Y/N:) ").upper()
                    if again != "Y": break
                    print("=" * 36)
                os.system('cls')
                continue
            elif menu == "3":  
                os.system('cls')
                while True:
                    new_student = student.StudentInfo()
                    addstud.registration(new_student)
                    again = input("Do you want to add another student?(Y/N:) ").upper()
                    if again != "Y": break
                os.system('cls')
                continue
            elif menu == "4":
                os.system('cls')
                printstud.print_all_students()
            elif menu == "5": exit()
            else: print("Error input, try again..."); continue
            again = input("Go back to menu?(Y/N:) ").upper()
            if again != "Y": exit()
            os.system("cls")