from pathlib import Path

def total_salary(path):
    with open(path, "r", encoding='utf-8') as file:
        employers = 0
        total = 0
        lines = file.readlines()
        for line in lines:
            salary = line.split(",")
            employers += 1
            total += float(salary[1])
    average = total/employers
    return (total, average)