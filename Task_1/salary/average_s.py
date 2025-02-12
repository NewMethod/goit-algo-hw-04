from pathlib import Path

def total_salary(path):
    try:
        with open(path, "r", encoding='utf-8') as file:
            employers = 0
            total = 0
            lines = file.readlines()
            for line in lines:
                salary = line.split(",")
                if len(salary) == 2 and (salary[1].strip()).isnumeric() is True:
                    employers += 1
                    total += float(salary[1])
                else:
                    print('Частково не коректні дані у файлі, потребують окремої перевірки та валідації.')
    except OSError:
        total, employers = 0, 1
        return total, employers
    try:
        average = total/employers
        return total, average
    except ZeroDivisionError:
        total, employers = 0, 2
        return total, employers