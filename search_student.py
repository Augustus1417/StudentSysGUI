class SearchStudent:
    def __init__(self, student):
        self.student_data = student

    def search_student(self, id_number):
        for student in self.student_data.allstudents:
            if id_number == "": print("\nYou did not type an ID.\n") ; return False
            if student.idnum == id_number:
                print("\n======== Student Information ========\n")
                print(student)
                print("\n========== Nothing Follows ==========\n") ; return
        print(f"\nThe Student with the ID number {id_number} does not exist\n") ; return