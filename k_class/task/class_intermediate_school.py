# 학교
# 이름, 지역, 학생 수, 선생님 수
# 학교 정보 출력 메소드

# 선생님
# 이름, 과목, 학교
# 선생님이 추가될 때마다 선생님 수 1증가
# 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가
# 선생님 정보 출력 메소드

# 학생
# 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# 학생이 추가될 때마다, 학생 수 1증가
# 학생 정보 출력 메소드

class School:
    def __init__(self, name, region, student_count=0, teacher_count=0):
        self.name = name
        self.region = region
        self.student_count = student_count
        self.teacher_count = teacher_count

    def print_info(self):
        print(self.name, self.region, self.student_count, self.teacher_count)


class Teacher:
    def __init__(self, name, subject, school):
        self.name = name
        self.subject = subject
        self.school = school
        self.school.teacher_count += 1

    def teach(self, students):
        for student in students:
            student.ability += 1

    def print_info(self):
        print(self.name, self.subject)
        self.school.print_info()


class Student:
    def __init__(self, name, grade, school, teacher, ability=0):
        self.name = name
        self.grade = grade
        self.school = school
        self.teacher = teacher
        self.ability = ability
        self.school.student_count += 1

    def print_info(self):
        print(self.name, self.grade, self.ability)
        self.school.print_info()
        self.teacher.print_info()


school = School('동석대학교', '서울시 강남구')
teacher = Teacher('한동석', '파이썬', school)
student = Student('홍길동', 1, school, teacher)
student2 = Student('이순신', 1, school, teacher)
school.print_info()
teacher.print_info()
student.print_info()
students = [student, student2]
teacher.teach(students)
student.print_info()
student2.print_info()

