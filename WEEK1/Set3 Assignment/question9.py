#SEATING CHART VALIDATOR

def seating_report(chart):
    
    report = {
        "total_seats": 0,
        "occupied": 0,
        "empty_rows": []
    }

    for i in range(len(chart)):

        empty = True

        for seat in chart[i]:

            report["total_seats"] = report["total_seats"] + 1

            if seat != None:
                report["occupied"] = report["occupied"] + 1
                empty = False

        if empty:
            report["empty_rows"].append(i)

    return report


chart = [
    ["Alice", "Bob"],
    [None, None],
    ["John", None]
]

print(seating_report(chart))