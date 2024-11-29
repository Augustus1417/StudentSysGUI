class StudentInfo:
    def __init__(self):
        self.allstudents = []
    
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