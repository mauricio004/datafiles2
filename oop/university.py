
class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        # Stores instances of CourseRunning
        self.classes = []

    def enroll(self, course_running):
        self.classes.append(course_running)
        course_running.add_student(self)


class Department:
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        # Store instances of Course
        self.courses = {}

    def add_course(self, description, course_code, credits):
        self.courses[course_code] = Course(description, course_code, credits)
        return self.courses[course_code]


class Course:
    def __init__(self, description, course_code, credits, department):
        self.description = description
        self.course_code = course_code
        self.credits = credits
        self.department = department
        self.department.add_course(self)

        self.add_running = []

    def add_running(self, year):
        self.add_running.append(CourseRunning(self, year))


class CourseRunning:
    def __init__(self, course, year):
        self.course = course
        self.year = year
        # Stores instances of Student
        self.students = []

    def add_student(self, student):
        self.students.append(student)


