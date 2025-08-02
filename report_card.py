import math
def valid_name(name):
    return name != "" and not any(char.isdigit() for char in name)


def valid_roll(roll):
    return roll.isdigit() and int(roll) > 0


def valid_subject_count(sn):
    return sn.isdigit() and int(sn) > 0


def valid_subject_mark(mark):
    return mark.isdigit() and 0 < int(mark) <= 100


def grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def print_report_card(student):
    print("\n------- REPORT CARD -------")
    print(f"Name      : {student['Name']}")
    print(f"Roll No.  : {student['Roll']}")
    print("\nSubjects and Marks:")
    for subject, mark in student['Subjects'].items():
        print(f"  {subject}: {mark}")
    print(f"\nTotal     : {student['Total Marks']}")
    print(f"Percentage: {student['Percentage']}%")
    print(f"Grade     : {student['Grade']}")
    print(f"Status    : {'Pass' if student['Grade'] != 'F' else 'Fail'}")
    print("----------------------------")


all_students = {}

while True:
    while True:
        s_name = input("Enter Student Name: ").strip().title()
        if valid_name(s_name):
            break
        else:
            print("Invalid name. Try again.")

    while True:
        s_roll = input("Enter Roll Number: ").strip()
        if valid_roll(s_roll):
            s_roll = int(s_roll)
            break
        else:
            print("Invalid roll number. Must be a positive number.")
    while True:
        sn = input("How many subjects? ").strip()
        if valid_subject_count(sn):
            sn = int(sn)
            break
        else:
            print("Enter a valid number of subjects.")
    subjects = {}
    for i in range(sn):
        while True:
            mark = input(f"Enter marks for Subject {i + 1}: ").strip()
            if valid_subject_mark(mark):
                subjects[f"Subject{i + 1}"] = int(mark)
                break
            else:
                print("Enter a valid mark (1–100).")
    total = sum(subjects.values())
    max_marks = sn * 100
    percentage = math.round((total / max_marks) * 100, 2)
    average = total / sn
    gpa = grade(average)
    student_info = {
        'Name': s_name,
        'Roll': s_roll,
        'Subjects': subjects,
        'Total Marks': total,
        'Percentage': percentage,
        'Grade': gpa
    }

    all_students[s_name] = student_info
    print_report_card(student_info)
    again = input("Do you want to enter another student? (y/n): ").lower()
    if again != 'y':
        break
print("\n ALL STUDENTS' REPORT CARDS")
for student in all_students.values():
    print_report_card(student)
