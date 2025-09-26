import math 

class Student: # creating this class to store student details (id, name, email, grades, courses)
    
    GPA_SCALE = { # dictionary for converting grades (letters) to GPA (numbers)
        'A': 4.0, 
        'B': 3.0, 
        'C': 2.0, 
        'D': 1.0, 
        'F': 0.0
    }

    def __init__(self, student_id, student_name, email, grades=None, courses=None): # initializing new Student object
        self.id_name = (student_id, student_name)  # tuple for id and name
        self.email = email # string for email
        self.grades = grades if grades is not None else {}  # dictionary for grades 
        self.courses = courses if courses is not None else set()  # set for courses

    def __str__(self): # this is for printing student's information
        student_id, student_name = self.id_name
        grades_str = ', '.join([f"{subject}: {score}" for subject, score in self.grades.items()])
        courses_str = ', '.join(self.courses)
        
        return (
            f"Student ID: {student_id}\n"
            f"Name: {student_name}\n"
            f"Email: {self.email}\n"
            f"Grades: {{{grades_str}}}\n"
            f"Courses: {{{courses_str}}}"
        )

    
    def calculate_gpa(self): # calculating student's grades based on their GPA
        if not self.grades:
            return 0.0
        
        total_gpa_points = 0
        num_grades = 0
        
        for grade in self.grades.values():
            letter_grade = str(grade).upper()
            if letter_grade in self.GPA_SCALE:
                total_gpa_points += self.GPA_SCALE[letter_grade]
                num_grades += 1
                
        return total_gpa_points / num_grades if num_grades > 0 else 0.0


class StudentRecords: # creating this class to store student records; also handles adding, updating, and deleting records
    def __init__(self):
        self.students = []

    def search_student(self, student_id, return_object=False): # searching students using their ID
        for student in self.students:
            if student.id_name[0] == student_id:
                return student if return_object else str(student)
                
        return "Student not found."

    def add_student(self, student_id, student_name, email, grades=None, courses=None): # adding new Student object and adds it to the list; prevents duplicate IDs
        if isinstance(self.search_student(student_id, return_object=True), Student): # here is the checking if the ID already exists
            return "Error: Student with this ID already exists."
        
        new_student = Student(student_id, student_name, email, grades, courses) # adding new student
        self.students.append(new_student)
        
        return "Student added successfully."

    def update_student(self, student_id, email=None, grades=None, courses=None): # updating information using their IDs as well
        student = self.search_student(student_id, return_object=True)
        
        if isinstance(student, Student): # update only what's provided; all other information remains the same
            if email is not None:
                student.email = email
            if grades is not None:
                student.grades.update(grades)
            if courses is not None:
                student.courses.update(courses)
            
            return "Student record updated successfully."
        else:
            return "Student not found."

    def delete_student(self, student_id): # removing students from the list using their IDs
        initial_length = len(self.students)
        self.students = [s for s in self.students if s.id_name[0] != student_id] # recreating the list with the remaining items
        
        if len(self.students) < initial_length:
            return "Student deleted successfully."
        else:
            return "Student not found."

    def enroll_course(self, student_id, course): # adding a course on the student's enrollment record
        student = self.search_student(student_id, return_object=True)
        
        if isinstance(student, Student):
            student.courses.add(course)
            return f"Course '{course}' enrolled successfully for student ID {student_id}."
        else:
            return "Student not found."

    def search_by_name(self, name): # searching for partial matches on the student name, ignoring lower or upper cases
        matches = []
        search_term_lower = name.lower()
        
        for student in self.students:
            student_name_lower = student.id_name[1].lower()
            
            if search_term_lower in student_name_lower:
                matches.append(str(student))
                
        if matches:
            return "\n---\n".join(matches)
        else:
            return "No students found with that name."



# <displaying all the output>

print("Student Records Management System\n")

records = StudentRecords() # initialize the system first

print(" Adding Students ") # add
print(records.add_student(12340, "Ledz Danreb", "ledzdanreb@gmail.com", 
                         grades={"MathMod": 'A', "GenPhysics": 'B'}, 
                         courses={"BasicCalculus", "DSA"})) 
print(records.add_student(12340, "Ledz Danreb", "ledzdanreb@gmail.com")) # should fail because same student ID
print(records.add_student(12341, "John Lenard", "johnlenard@gmail.com", 
                         grades={"PhilHistory": 'C', "EnglishGrammar": 'A'}, 
                         courses={"AsianLiterature"}))
print(records.add_student(12342, "Melchizedek Mccain", "mccain@gmail.com"))
print("\n")

print(" Search Student ") # search
print(records.search_student(12340))
print("")
print(records.search_student(12341))
print("")
print(records.search_student(12342))
print("\n")

print(" Enroll Course ") # enroll
print(records.enroll_course(12340, "SetsAndAlgorithms"))
print(records.enroll_course(12341, "EarthScience"))
print(records.enroll_course(00000, "OfCourse")) # should fail because student doesn't exist
print("\n")

print(" Search Student ") # search
print(records.search_student(12340))
print("")
print(records.search_student(12341))
print("\n")

print(" Update Student ") # update
print(records.update_student(12342, email="melchizedekmccain@gmail.com", 
                            grades={"ComputerProgramming": 'B'}, 
                            courses={"AdvCompProg"}))
print("\n")

print(records.search_student(12342))
print("\n")

print(" Calculate GPA ") # GPA
student_12342 = records.search_student(12342, return_object=True)
if isinstance(student_12342, Student):
    gpa_12342 = student_12342.calculate_gpa()
    print(f"Melchizedek Mccain GPA: {gpa_12342:.2f}")
print("\n")

print(" Delete Student ") # delete
print(records.delete_student(12341))
print(records.delete_student(12341)) # should fail because already deleted it
print("\n")

print(records.search_student(12340))
print("")
print(records.search_student(12342))
print("\n")

