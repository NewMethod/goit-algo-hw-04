from pathlib import Path

def get_cats_info(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        cats = []
        for line in lines:
            cat_info = line.split(',')
            error_file = 'Зміст та формат файлу не відповідає умовам завдання'
            if len(cat_info) > 3 or len(cat_info) < 3:
                return error_file
            else:
                cats.append({'id': cat_info[0], 'name': cat_info[1], 'age': cat_info[2].strip()})
        if cats != None:
            return cats
        else:
            return error_file