while True:
    try:
        # Taking input from user
        # To input follow this
        # How many courses? 3
        # Enter your all course credit in one line serially (separated by space). 
        # 3 3 2
        # Enter your all course gpa in one line serially (separated by space). 
        # 3.25 3 3.75
        number_of_course = int(input("How many courses? "))
        credit_list_input = input("Enter your all course credit in one line serially (separated by space). \n").split()
        gpa_list_input = input("Enter your all course gpa in one line serially (separated by space). \n").split()

        total_grade = 0
        total_credit = 0

        for i in range(number_of_course):
            int_credit = int(credit_list_input[i])
            total_credit += int_credit
            float_gpa = float(gpa_list_input[i])
            total_grade += (int_credit * float_gpa)

        result = total_grade / total_credit
        print(f"Your CGPA for this semester is : {round(result, 2)}")
        break
    except IndexError:
        print("...Please recheck again. You forgot something...")
