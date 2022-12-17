class Group:
    def __init__(self, group_name, max_students=10):
        self.group_name = group_name
        self.students = []
        self.max_students = max_students

    def add_student(self, student):
        if student not in self.students and len(self.students) < self.max_students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def search_student(self, surname):
        result = []
        for student in self.students:
            if student.surname == surname:
                result.append(student)
                return result

    def __str__(self):
        return f'{self.group_name}\n' + '\n'.join(map(str, self.students))
