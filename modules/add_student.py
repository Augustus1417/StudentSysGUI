class AddStudent:
    def __init__(self, student):
        self.student_data = student

    def add_student(self, student):
        self.student_data.allstudents.append(student)
        with open("modules/data.txt",'a') as f:
            f.write(str(f"{student.getName()},{student.getAge()},{student.getIDNum()},{student.getEmail()},{student.getPhoneNum()}\n"))
        print(f"\nAdded student {student.getName()} to the list.\n")

    def registration(self, new_student):
        print("\n====== Add new student ======")
        name = input("\nEnter Name: ")
        new_student.setName(name)

        age = input("Enter Age: ")
        new_student.setAge(age)

        idnum = input("Enter Student ID: ")
        new_student.setIDNum(idnum)

        email = input("Enter Email Address: ")
        new_student.setEmail(email)

        phone_num = input("Enter Phone Number: ")
        new_student.setPhoneNum(phone_num)
        print("\n====== Nothing Follows ======")

        self.add_student(new_student)