import os
import time

if __name__ == "__main__":
    print('Текущая дериктория', os.getcwd())
    directory = '.'
    for root, dirs, files in os.walk(directory):
        if root == directory:
            for file in files:
                filepath = os.path.join(root, file)
                filetime = os.path.getmtime(filepath)
                formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
                filesize = os.path.getsize(file)
                parent_dir = os.path.dirname(filepath)
                print(
                    f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
        else:
            break