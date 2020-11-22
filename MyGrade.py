def main():

    lab_grades = []

    for i in range(0, 5):

        lab = int(input("Enter Lab Grades: "))
        lab_grades.append(lab)

    mid_grade = int(input("Enter Midterm Grade: "))
    final_grade = int(input("Enter Final Grade: "))

    course_grade = calc_course_grade(lab_grades, mid_grade, final_grade)
    print("Your Course Grade is: ", course_grade)


def calc_course_grade(labs, mid, fin):
    lab_weight = .34
    midterm = .33
    final = .33
    lab_grade = 0
    for i in range(len(labs)):
        lab_grade += labs[i]

    lab_grade = lab_grade/len(labs) * lab_weight

    return lab_grade + mid * midterm + fin * final


main()
