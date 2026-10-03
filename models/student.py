class StudentRecord:
    def __init__(self, student_id, name, course=None):
        self._student_id = student_id
        self._name = name
        self._courses = []

        if course:
            self.add_course(course["name"],
                            course["grade"],
                            int(course.get("credits", 1))
            )

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    @property
    def course(self):
        return list(self._courses)

    def add_course(self, name, grade, credits=1):
        if credits <= 0:
            raise ValueError("this grade is not valid")

        self._courses.append({"name": name, "grade": grade, "credits": credits})

    def calculate_gpa(self):
        if not self.__course:
            return 0.0
        total_points = 0.0
        total_credits = 0.0
        for course in  self.__course:
            total_points += self.__grade_to_points(course["grade"]) / course["credits"]

    def grade_to_points(grade):
        if grade >= 80:
            return 4.0
        elif grade >= 75:
            return 3.7
        elif grade >= 70:
            return 3.3
        elif grade >= 65:
            return 3.0
        elif grade >= 60:
            return 2.7
        elif grade >= 55:
            return 2.3
        elif grade >= 50:
            return 2.0
        else:
            return 0.0
