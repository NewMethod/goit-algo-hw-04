from pathlib import Path
from Cat import get_cats_info

def main():
    # build object Path for dir 
    path = Path('Cat/cats.txt')
    absolute_path = path.absolute()
    try:
        if Path(absolute_path).exists() and Path(absolute_path).is_file():
            cats_info = get_cats_info(absolute_path)
            return print(cats_info)
        else:
            return print("Не вдалося знайти файл з котами")
    except FileNotFoundError:
        return print("Не вдалося знайти файл з котами")

if __name__ == "__main__":
    main()