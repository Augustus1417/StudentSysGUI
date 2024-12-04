from timeit import default_timer
class StudentInfo:
    def __init__(self):
        self.allstudents = []
    
    def load_data_from_file(self):
        start = default_timer()
        with open("modules/data.txt", 'r') as studentfile:
            for student_data in studentfile:
                load_student = StudentInfo()
                student_data = student_data.strip().split(',')
                load_student.setName(student_data[0])
                load_student.setAge(student_data[1])
                load_student.setIDNum(student_data[2])
                load_student.setEmail(student_data[3])
                load_student.setPhoneNum(student_data[4])
                self.allstudents.append(load_student)
        print(f"\nStudent data has been loaded. Finished in {(default_timer() - start):6f} seconds.")

    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age

    def setIDNum(self, idnum):
        self.idnum = idnum

    def setEmail(self, email):
        self.email = email

    def setPhoneNum(self, phone):
        self.phone = phone

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def getIDNum(self):
        return self.idnum

    def getEmail(self):
        return self.email

    def getPhoneNum(self):
        return self.phone

    def __str__(self): 
        return f"Name: {self.name}\nAge: {self.age}\nID Number: {self.idnum}\nEmail: {self.email}\nPhone Number: {self.phone}"