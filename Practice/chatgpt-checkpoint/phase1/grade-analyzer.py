grades = {
    "Ada": 85,
    "Tunde": 42,
    "Mina": 73,
    "David": 90
}

def analyze_grades(grades):
    
    passed = []
    sum_grade = 0
    first_student = next(iter(grades))
    highest = grades[first_student]
    highest_grade = first_student

    for key in grades:
        sum_grade += grades[key]
        if grades[key] >= 50:
            passed.append(key)
        if grades[key] > highest:
            highest = grades[key]
            highest_grade = key
    
    average_grade = sum_grade/len(grades)
        
    result = {
        "average": average_grade,
        "highest": highest_grade,
        "passed": passed,
    }
     
    return result
    
print(analyze_grades(grades))