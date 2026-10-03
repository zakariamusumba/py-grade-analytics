from engine.statistics import (
    mean,
    median,
    sample_variance,
    standard_deviation,
)
from models.student import StudentRecord

def flatten_students(nested_students):
    records = []

    for group in nested_students:
        if isinstance(group, StudentRecord):
            records.append(group)
            continue

        if isinstance(group, dict):
            records.append(
                StudentRecord(
                    group["id"],
                    group["name"],
                    group["courses"],
                )
            )
            continue

        for student_data in group:
            if isinstance(student_data, StudentRecord):
                records.append(student_data)
                continue

            records.append(
                StudentRecord(
                    student_data["id"],
                    student_data["name"],
                    student_data["courses"],
                )
            )

    return records

def academic_standing(gpa):
    if gpa < 2.0:
        return "Academic Probation"
    elif gpa >= 3.7:
        return "Honors"
    else:
        return "Good Standing"


def print_statistics(grades):
    if not grades:
        print("\nGrade Statistics")
        print("----------------")
        print("Count:              0")
        print("Mean:               N/A")
        print("Median:             N/A")
        print("Sample Variance:    N/A")
        print("Standard Deviation: N/A")
        return

    print("\nGrade Statistics")
    print("----------------")
    print(f"Count:              {len(grades)}")
    print(f"Mean:               {mean(grades):.2f}")
    print(f"Median:             {median(grades):.2f}")
    print(f"Sample Variance:    {sample_variance(grades):.2f}")
    print(f"Standard Deviation: {standard_deviation(grades):.2f}")

def main():
    # Nested input: groups -> students -> courses.
    nested_students = [
        [
            {
                "id": "S001",
                "name": "Amina",
                "courses": [
                    {"name": "Mathematics", "grade": 86, "credits": 3},
                    {"name": "Programming", "grade": 91, "credits": 3},
                    {"name": "Statistics", "grade": 82, "credits": 3},
                ],
            },
            {
                "id": "S002",
                "name": "Brian",
                "courses": [
                    {"name": "Mathematics", "grade": 52, "credits": 3},
                    {"name": "Programming", "grade": 48, "credits": 3},
                    {"name": "Statistics", "grade": 55, "credits": 3},
                ],
            },
        ],
        [
            {
                "id": "S003",
                "name": "Chloe",
                "courses": [
                    {"name": "Mathematics", "grade": 74, "credits": 3},
                    {"name": "Programming", "grade": 78, "credits": 3},
                    {"name": "Statistics", "grade": 71, "credits": 3},
                ],
            },
            {
                "id": "S004",
                "name": "David",
                "courses": [
                    {"name": "Mathematics", "grade": 63, "credits": 3},
                    {"name": "Programming", "grade": 67, "credits": 3},
                    {"name": "Statistics", "grade": 61, "credits": 3},
                ],
            },
        ],
    ]

    students = flatten_students(nested_students)

    all_grades = [
        course["grade"]
        for student in students
        for course in student.courses
    ]

    print("Student Academic Report")
    print("========================")

    for student in students:
        gpa = student.calculate_gpa()
        standing = academic_standing(gpa)

        print(
            f"{student.student_id} | "
            f"{student.name:<10} | "
            f"GPA: {gpa:.2f} | "
            f"{standing}"
        )

    print_statistics(all_grades)