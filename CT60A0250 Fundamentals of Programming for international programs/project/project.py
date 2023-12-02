import datetime


def random() -> float:
    return abs(hash(datetime.datetime.now()) / 2**64)


def csv_does_exist(fname: str, col: int, val: str) -> bool:
    try:
        with open(fname, "r") as f:
            for line in f:
                if line.split(",")[col] == val:
                    return True
    except FileNotFoundError:
        return False
    return False


def csv_parse(fname: str) -> list:
    try:
        with open(fname, "r") as f:
            return [line.split(",") for line in f]
    except FileNotFoundError:
        return []


def courses_dict() -> dict:
    courses = {}
    for course in csv_parse("./courses.txt"):
        courses[course[0]] = course
    return courses


def add_student():
    first_name = last_name = ""
    while not (first_name.isalpha() and last_name.isalpha() and first_name[0].isupper() and last_name[0].isupper()):
        print("Names should contain only letters and start with capital letters.")
        first_name = input("Enter the first name of the student:\n")
        last_name = input("Enter the last name of the student:\n")

    id = int(random() * 89999 + 10000)
    while csv_does_exist("./students.txt", 0, str(id)):
        id = int(random() * 89999 + 10000)

    major = ""
    while not ["CE", "EE", "ET", "ME", "SE"].count(major) == 1:
        major = input("Select student's major:\n\tCE: Computational Engineering\n\tEE: Electrical Engineering\n\tET: Energy Technology\n\tME: Mechanical Engineering\n\tSE: Software Engineering\nWhat is your selection?\n")

    with open("./students.txt", "a") as f:
        f.write(f"{id},{first_name},{last_name},{ str(datetime.datetime.now().year)},{major},{first_name.lower()}.{last_name.lower()}@lut.fi\n")


def search_student():
    search_string = ""
    while len(search_string) < 3:
        search_string = input("Give at least 3 characters of the students first or last name:\n").lower()

    found = []
    for student in csv_parse("./students.txt"):
        if (student[1].lower().count(search_string) > 0 or student[2].lower().count(search_string) > 0):
            found.append(student)

    print("Matching students:")
    for student in found:
        print(f"ID: {student[0]}, First name: {student[1]}, Last name: {student[2]}")


def search_course():
    search_string = ""
    while len(search_string) < 3:
        search_string = input("Give at least 3 characters of the name of the course or the teacher:\n").lower()

    found = []
    for course in csv_parse("./courses.txt"):
        if course[1].lower().count(search_string) > 0:
            found.append(course)
            continue
        for teacher in course[3:]:
            if teacher.lower().count(search_string) > 0:
                found.append(course)
                break

    print("Matching courses:")
    for course in found:
        print(f"ID: {course[0]}, Name: {course[1]}, Teacher(s): {', '.join(course[3:])}")


def add_course_completion():
    course_id = ""
    while not csv_does_exist("./courses.txt", 0, course_id):
        course_id = input("Give the course ID:\n")

    student_id = ""
    while not csv_does_exist("./students.txt", 0, student_id):
        student_id = input("Give the student ID:\n")

    grade = int(input("Give the grade:\n"))
    if grade < 1 or grade > 5:
        print("Grade is not a correct grade.")
        return

    should_overwrite = False
    for completion in csv_parse("./passed.txt"):
        if completion[0] == course_id and completion[1] == student_id and grade <= int(completion[3]):
            print(f"Student already passed this course earlier with grade {completion[3]}")
            return
        if completion[0] == course_id and completion[1] == student_id and grade > int(completion[3]):
            should_overwrite = True

    def validate_date(date: str) -> int:
        try:
            datetime.datetime.strptime(date, "%d/%m/%Y")
        except:
            return 1

        if datetime.datetime.strptime(date, "%d/%m/%Y") > datetime.datetime.now():
            return 2
        elif (datetime.datetime.now() - datetime.datetime.strptime(date, "%d/%m/%Y")).days > 30:
            return 3
        else:
            return 0

    date = input("Enter a date (DD/MM/YYYY):\n")
    while validate_date(date) != 0:
        date = input("Enter a date (DD/MM/YYYY):\n")

        err = validate_date(date)
        if err == 1:
            print("Invalid date format. Use DD/MM/YYYY. Try again!")
        elif err == 2:
            print("Input date is later than today. Try again!")
        elif err == 3:
            print('Input date is older than 30 days. Contact "opinto".')

    print("Input date is valid.")

    if should_overwrite:
        with open("./passed.txt", "r") as f:
            lines = f.readlines()
            with open("./passed.txt", "w") as f:
                for line in lines:
                    if line.split(",")[0] == course_id and line.split(",")[1] == student_id:
                        f.write(f"{course_id},{student_id},{date},{grade}\n")
                    else:
                        f.write(line)
    else:
        with open("./passed.txt", "a") as f:
            f.write(f"{course_id},{student_id},{date},{grade}\n")

    print("Record added!")


def show_student_record():
    studentid = input("Give the student ID:\n")
    if not csv_does_exist("./students.txt", 0, studentid):
        print("Student ID not found.")
        return

    student = None
    for student in csv_parse("./students.txt"):
        if student[0] == studentid:
            break

    print(f"Student ID: {student[0]}\nName: {student[2]}, {student[1]}\nStarting year: {student[3]}\nMajor: {student[4]}\nEmail: {student[5]}")

    print("Passed courses:\n")

    c_dict = courses_dict()
    credits, grade, count = 0, 0, 0
    for completion in csv_parse("./passed.txt"):
        if completion[1] == studentid:
            credits += int(c_dict[completion[0]][2])
            grade += int(completion[3])
            count += 1

            print(f"Course ID: {completion[0]}, Name: {c_dict[completion[0]][1]}, Credits: {c_dict[completion[0]][2]}\nDate: {completion[2]}, Teacher(s): {', '.join(c_dict[completion[0]][3:]).strip()}, grade: {completion[3]}")

    print(f"Total credits: {credits}, average grade: {grade / count}")


menu_funcs = {
    "1": add_student,
    "2": search_student,
    "3": search_course,
    "4": add_course_completion,
    "5": show_student_record,
    "0": lambda: exit(0),
}


def menu():
    print("You may select one of the following:\n\t1) Add student\n\t2) Search student\n\t3) Search course\n\t4) Add course completion\n\t5) Show student's record\n\t0) Exit\nWhat is your selection?")
    if (selection := input()) in menu_funcs:
        menu_funcs[selection]()


if __name__ == "__main__":
    while True:
        menu()
