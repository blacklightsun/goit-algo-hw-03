import sys
import os
from pathlib import Path


def sort_by_extension(folder_from: str, folder_to: str) -> None:

    access_mode = os.R_OK | os.W_OK  # Дозвіл на читання та запис

    current_path = Path().absolute()
    path_from = Path(folder_from)
    path_to = current_path / folder_to

    for child in path_from.iterdir():
        if child.is_dir():
            sort_by_extension(child, str(path_to))
        elif child.is_file():
            if os.access(child, access_mode):
                path_ext = path_to / str(child.suffix)
                # if not path_ext.exists():
                try:
                    path_ext.mkdir(parents=True, exist_ok=True)
                    print("Папка створена успішно.")
                # except FileExistsError:
                #     print("Папка вже існує.")
                except OSError as e:
                    print(f"Помилка при створенні папки: {e}")
                    return

                dist_file = path_ext / str(child)
                try:
                    child.rename(dist_file)
                    print("Файл успішно переміщено.")
                except OSError as e:
                    print(f"Помилка при переміщенні файлу: {e}")

            else:
                print("Файл недоступний для копіювання.")


try:
    folder_from = sys.argv[1]
except IndexError:
    print('Помилка! Вкажіть коректний шлях до папки з файлами')
else: 
    try:
        folder_to = sys.argv[2]
    except IndexError:
        print("Папка призначення не вказана. За замовчуванням копіювання буде здійснено в папку 'dist'.")
        folder_to = "dist"
    finally:
        sort_by_extension(folder_from, folder_to)
