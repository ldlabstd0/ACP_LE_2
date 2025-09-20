import math

class STUDENT:
  GPA_SCALE = {
    'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'E':0.0
  }

  def __init__(self, STUDENT_ID: int, STUDENT_NAME: str, EMAIL: str, GRADES: dict = None, COURSES: set = None):
    self.ID_NAME = (STUDENT_ID, STUDENT_NAME)
    self.EMAIL = EMAIL
    self.GRADES = GRADES if GRADES is not None else {}
    self.COURSES = COURSES if COURSES is not None else set()

  def __str__(self):
    STUDENT_ID, STUDENT_NAME = self.ID_NAME

    GRADED_STR = ', '.join([f"{sub}: {score}" for sub, score in self.GRADES.items()])
    COURSES_STR = ', '.join(self.COURSES)

    return (
      f"STUDENT ID: {STUDENT_ID}\n"
      f"NAME: {STUDENT_NAME}\n"
      f"EMAIL: {self.EMAIL}\n"
      f"GRADES: {{{GRADED_STR}}}\n"
      f"COURSES: {{{COURSES_STR}}}\n"
    )
    
