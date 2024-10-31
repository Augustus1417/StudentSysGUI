import os
class Login:
    def __init__(self, student):
        self.student_data = student

    def login(self, id_number):
        if id_number == "": print("\nYou did not type an ID.") ; return False
        for student in self.student_data.allstudents:
            if student.idnum == id_number: 
                os.system('cls')
                print( f"\nWelcome, {student.name}!") ; return True
        print(f"The Student with the ID number {id_number} does not exist") ; return False