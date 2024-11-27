from student import StudentInfo
from timeit import default_timer

class Load_Student_Data:
    def __init__(self, student):
        start = default_timer()
        self.student_data = student
        with open("data.txt", 'r') as studentfile:
            for student_data in studentfile:
                load_student = StudentInfo()
                student_data = student_data.rstrip('\n')
                student_data = student_data.split(",")
                load_student.setName(student_data[0])
                load_student.setAge(student_data[1])
                load_student.setIDNum(student_data[2])
                load_student.setEmail(student_data[3])
                load_student.setPhoneNum(student_data[4])
                self.student_data.allstudents.append(load_student)
        print(f"\nStudent data has been loaded. Finished in {(default_timer() - start):6f} seconds.")