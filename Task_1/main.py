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
            try:
                total, average = total_salary(absolute_path)
                if total != 0:
                    return print(f"Загальна сума заробітної плати: {round(total)}, Середня заробітна плата: {round(average)}")
                elif average==2:
                    return print('Не відкривається файл з зарплатами')           
            except:
                return print('Файл з зарплатами пустий')
        else:
            return print("Шлях до файлу невірний")
    except FileNotFoundError:
        return print("Не вдалося знайти файл з зарплатами")

if __name__ == "__main__":
    main()