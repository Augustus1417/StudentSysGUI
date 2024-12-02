class AddStudent:
    def __init__(self, student):
        self.student_data = student

    def add_student(self, student):
        self.student_data.allstudents.append(student)
        with open("modules/data.txt",'a') as f:
            f.write(str(f"{student.getName()},{student.getAge()},{student.getIDNum()},{student.getEmail()},{student.getPhoneNum()}\n"))
        return(f"\nAdded student {student.getName()} to the list.\n")

    def registration(self, new_student, name=" ", age=" ", idnum=" ",email=" ",phone_num=" "):
        new_student.setName(name)
        new_student.setAge(age)
        new_student.setIDNum(idnum)
        new_student.setEmail(email)
        new_student.setPhoneNum(phone_num)
        self.add_student(new_student)
        return(f"\nAdded student {new_student.getName()} to the list.\n")
