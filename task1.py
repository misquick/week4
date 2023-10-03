def grade_calculation(score):
    if score >= 90:
        return("A")
    elif score >= 80:
        return("B")
    elif score >= 70:
        return("C")
    elif score >= 60:
        return("D")
    elif score < 0 or score > 100:
        return ("Error, please enter numeric input between 0 and 100")
    else:
        return("F")
try:
    score_input = float(input("Enter score: "))
    grade = grade_calculation(score_input)
    print(f"Grade: {grade}")
except ValueError:
    print("Error: please enter a valid numeric score between 0 and 100")
