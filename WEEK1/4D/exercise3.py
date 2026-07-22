#TEMPERATURE REPORT

def classify_temp(temp):
    if temp <10:
        return "Cold"
    elif temp <25:
        return "Mild"
    else:
        return "Hot"

def temperature_report(temps):
    counts = {"Cold":0,
              "Mild":0,
              "Hot":0,
            }
    for t in temps:
        category = classify_temp(t)
        counts[category] += 1
    return counts
temps =[1,70,20,15,18]
print (temperature_report(temps))