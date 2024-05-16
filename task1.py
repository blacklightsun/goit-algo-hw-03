import sys
import shutil
from pathlib import Path


def sort_by_extension(folder_from, folder_to='dist') -> None:

    path_to = Path(folder_to)

    try:
        for child in Path(folder_from).iterdir():
            if child.is_dir():
                sort_by_extension(child, str(path_to))
            elif child.is_file():
                path_ext = path_to / child.suffix[1:]
                path_ext.mkdir(parents=True, exist_ok=True)
                shutil.copy2(child, path_ext)
    except OSError:
        print("Помилка операцій з файлом чи папкою")


try:
    sort_by_extension(*sys.argv[1:3])
except:
    print('\nПомилка! Не вказаний шлях до папки з файлами. Спробуйте ще раз.\n')
