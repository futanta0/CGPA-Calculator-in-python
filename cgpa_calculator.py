print("""
______________________________________
-----GPA CALCULATOR OF 1 SEMESTER-----
--------------------------------------
---Based on Bangladesh's GPA system---
______________________________________
""")

def cgpaCalculate():
    courses = int(input("How many courses are in the semester?\n ->"))
    total_grade_point = []
    total_course_credit = []

    #Loop for obtained grade and course credit
    for i in range(courses):
        print("--------------------------------")
        course_code = input("What is the course code? ->")
        obtained_grade = float(input(f"Enter your grade for {course_code}: "))
        course_credit = int(input(f"Enter your credit {course_code}: "))
        total_course_credit.append(course_credit)
        total = obtained_grade * course_credit
        total_grade_point.append(total)
    gpa = sum(total_grade_point) / sum(total_course_credit)
    
    # Letter grade based on GPA
    letter_grade = ""
    if gpa >= 2.0:
        if gpa == 4:
            letter_grade = "A+"
        elif gpa >= 3.75:
            letter_grade = "A"
        elif gpa >= 3.50:
            letter_grade = "A-"
        elif gpa >= 3.25:
            letter_grade = "B+"
        elif gpa >= 3:
            letter_grade = "B"
        elif gpa >= 2.75:
            letter_grade = "B-"
        elif gpa >= 2.5:
            letter_grade = "C+"
        elif gpa >= 2.25:
            letter_grade = "C"
        elif gpa >= 2:
            letter_grade = "D"
    else:
        letter_grade ="F"

    #Final Result    
    print("-------**********--------")
    print(f"Your GPA is: {round(gpa, 2)} & Letter grade: {letter_grade}")


cgpaCalculate()
