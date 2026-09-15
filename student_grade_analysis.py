students=[{"name": "Ali", "course1": "Programming Fundamentals","course2": "Database Management Systems", "course3": "Intro to data science ", "course4": "Quantitative Reasoning", "course5": "Distribution theory", "course6": "Probability and Statistics", 
          "marks1": 85, "marks2": 90, "marks3": 70, "marks4": 81, "marks5": 44, "marks6": 80},

          {"name": "Sara", "course1": "Programming Fundamentals","course2": "Database Management Systems", "course3": "Intro to data science ", "course4": "Quantitative Reasoning", "course5": "Distribution theory", "course6": "Probability and Statistics",
           "marks1": 75, "marks2": 70, "marks3": 85, "marks4": 90, "marks5": 95, "marks6": 88},

           {"name": "Hassan", "course1": "Programming Fundamentals","course2": "Database Management Systems", "course3": "Intro to data science ", "course4": "Quantitative Reasoning", "course5": "Distribution theory", "course6": "Probability and Statistics",
          "marks1": 65, "marks2": 66, "marks3": 75, "marks4": 80, "marks5": 75, "marks6": 90},

           {"name": "Eman", "course1": "Programming Fundamentals","course2": "Database Management Systems", "course3": "Intro to data science ", "course4": "Quantitative Reasoning", "course5": "Distribution theory", "course6": "Probability and Statistics",
            "marks1": 35, "marks2": 92, "marks3": 78, "marks4": 90, "marks5": 85, "marks6": 80},

            {"name": "Esha", "course1": "Programming Fundamentals","course2": "Database Management Systems", "course3": "Intro to data science ",'course4': "Quantitative Reasoning", "course5": "Distribution theory", "course6": "Probability and Statistics",
            "marks1": 85, "marks2": 50, "marks3": 75, "marks4": 70, "marks5": 85, "marks6": 60}] 
student_count = len(students)
print('Total number of students:', student_count)

print('    ------------------Student Result Analysis-------------------')
for student in students:
  
    total_courses = len([student['course1'], student['course2'], student['course3'], student['course4'], student['course5'], student['course6']])

    marks1 = student['marks1']
    marks2 = student['marks2']
    marks3 = student['marks3']
    marks4 = student['marks4']
    marks5 = student['marks5']
    marks6 = student['marks6']
    total_marks = total_courses * 100
    obtain_marks = marks1 + marks2 + marks3 + marks4 + marks5 + marks6
    average_marks = obtain_marks / total_courses
    percentage= (obtain_marks / (total_courses * 100)) * 100

    if percentage >= 90:
        grade = "A+"

    elif percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 50:
        grade = "D"

    else:
        grade = "F"
    
    max_marks = marks1
    max_course = student["course1"]

    if marks2 > max_marks:
        max_marks = marks2
        max_course = student["course2"]

    if marks3 > max_marks:
        max_marks = marks3
        max_course = student["course3"]

    if marks4 > max_marks:
        max_marks = marks4
        max_course = student["course4"]

    if marks5 > max_marks:
        max_marks = marks5
        max_course = student["course5"]

    if marks6 > max_marks:
        max_marks = marks6
        max_course = student["course6"]


    # Student Minimum Marks

    min_marks = marks1
    min_course = student["course1"]

    if marks2 < min_marks:
        min_marks = marks2
        min_course = student["course2"]

    if marks3 < min_marks:
        min_marks = marks3
        min_course = student["course3"]

    if marks4 < min_marks:
        min_marks = marks4
        min_course = student["course4"]

    if marks5 < min_marks:
        min_marks = marks5
        min_course = student["course5"]

    if marks6 < min_marks:
        min_marks = marks6
        min_course = student["course6"]


    # Display Student Result
    print('Student Name:', student['name'])
   # total_courses = len([student['course1'], student['course2'], student['course3'], student['course4'], student['course5'], student['course6']])
    print('Total courses:', total_courses)
    print('courses:', student['course1'], 'marks:', student['marks1'],'grade:', grade)
    print('courses:', student['course2'], 'marks:', student['marks2'],'grade:', grade)
    print('courses:', student['course3'], 'marks:', student['marks3'],'grade:', grade)
    print('courses:', student['course4'], 'marks:', student['marks4'],'grade:', grade)
    print('courses:', student['course5'], 'marks:', student['marks5'],'grade:', grade)
    print('courses:', student['course6'], 'marks:', student['marks6'],'grade:', grade)
    
    print("Total Marks:", total_marks)
    print("Obtained Marks:", obtain_marks)
    print("Average:", average_marks)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)

    print("Highest Marks:", max_marks)
    print("Highest Marks Course:", max_course)

    print("Lowest Marks:", min_marks)
    print("Lowest Marks Course:", min_course)



print('----------------------course wise analysis-----------------------')
courses = [
    "Programming Fundamentals",
    "Database Management Systems",
    "Intro to Data Science",
    "Quantitative Reasoning",
    "Distribution Theory",
    "Probability and Statistics"
]

marks_keys = [
    "marks1",
    "marks2",
    "marks3",
    "marks4",
    "marks5",
    "marks6"
]

for i in range(6):
    obtain_marks = 0
    highest = 0
    lowest = 100
    highest_student = ""
    lowest_student = ""

    for student in students:

        marks = student[marks_keys[i]]

        obtain_marks = obtain_marks + marks

        if marks > highest:
            highest = marks
            highest_student = student["name"]

        if marks < lowest:
            lowest = marks
            lowest_student = student["name"]

    average = obtain_marks / student_count
    percentage = (obtain_marks / (student_count * 100)) * 100

    print("\nCourse:", courses[i])
    print('Total Marks:', total_courses * 100)
    print("Obtained Marks:", obtain_marks)
    print("Average:", average)
    print("Percentage:", percentage, "%")
    print("Maximum Marks:", highest)
    print("Maximum Marks Student:", highest_student)
    print("Minimum Marks:", lowest)
    print("Minimum Marks Student:", lowest_student)












    
