# Student Grade Calculator
# Module 2: Python Mini Project


def get_grade(percentage):
    """Return grade based on percentage."""

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def get_valid_marks(subject):
    """Get valid marks between 0 and 100."""

    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    print("=" * 40)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 40)

    student_name = input("Enter student name: ")

    subjects = [
        "Mathematics",
        "Science",
        "English",
        "Computer Science",
        "Social Studies"
    ]

    marks = []

    for subject in subjects:
        mark = get_valid_marks(subject)
        marks.append(mark)

    total_marks = sum(marks)
    average = total_marks / len(marks)
    percentage = average
    grade = get_grade(percentage)

    print("\n" + "=" * 40)
    print("          STUDENT RESULT")
    print("=" * 40)

    print("Student Name:", student_name)

    print("\nSubject Marks:")

    for subject, mark in zip(subjects, marks):
        print(f"{subject}: {mark:.2f}")

    print("\nTotal Marks:", f"{total_marks:.2f}")
    print("Average:", f"{average:.2f}")
    print("Percentage:", f"{percentage:.2f}%")
    print("Grade:", grade)

    if grade == "F":
        print("Result: Needs Improvement")
    else:
        print("Result: Passed")

    print("=" * 40)


if __name__ == "__main__":
    main()
