#EMPLOYEE PAYROLL SYSTEM
def calculate_payroll(employees):
    
    payroll = {}

    for employee in employees:

        hours = employee["hours_worked"]
        rate = employee["hourly_rate"]

        if hours > 40:
            overtime = hours - 40
            pay = (40 * rate) + (overtime * rate * 1.5)
        else:
            pay = hours * rate

        payroll[employee["name"]] = pay

    return payroll


def highest_paid(payroll):

    highest_name = ""
    highest_pay = 0

    for name in payroll:
        if payroll[name] > highest_pay:
            highest_pay = payroll[name]
            highest_name = name

    return highest_name


employees = [
    {"name": "Cedric", "hours_worked": 80, "hourly_rate": 10},
    {"name": "Jerry", "hours_worked": 45, "hourly_rate": 12},
    {"name": "Tom", "hours_worked": 50, "hourly_rate": 15}
]

payroll = calculate_payroll(employees)

print(payroll)
print(highest_paid(payroll))