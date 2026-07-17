def get_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
    
scores = [99,78,88,43,60,50]

for score in scores:
    print(f"Score: {score} -> Grade: {get_grade(score)}")