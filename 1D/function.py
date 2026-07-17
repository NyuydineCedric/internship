def studentResult(name, math, english, science):
    name = name.capitalize()
    total = math + english + science
    average = total/3
    def grade():
        if (average>=70):
            return "A"
        elif(average>=60):
            return "B"
        elif(average>=50):
            return "C"
        elif(average>=40):
            return "D"
        else:
            return "F"
        return grade()
    return f"Name: {name} \n Math: {math} \n English: {english} \n Science {science} \n Total: {total} \n Average: {average} \n Grade: {grade()}"
print(studentResult("cedric",70,80,80))