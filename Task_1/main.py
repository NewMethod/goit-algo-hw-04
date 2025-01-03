from pathlib import Path
from salary import total_salary

def main():
    # build object Path for dir
    relative_path = Path("salary/salary.txt")
    absolute_path = relative_path.absolute()
    # existing control
    try:
        if absolute_path.exists() and absolute_path.is_file():
            #get function for average
            (total, average) = total_salary(absolute_path)
            return print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
        else:
            return print("Не вдалося знайти файл з зарплатами")
    except FileNotFoundError:
        return print("Не вдалося знайти файл з зарплатами")

if __name__ == "__main__":
    main()