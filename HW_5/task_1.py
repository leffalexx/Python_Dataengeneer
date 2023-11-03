# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def get_file_info(file_path):
    name_and_ext = file_path.rsplit('/', 1)[-1]
    name, extension = name_and_ext.rsplit('.')
    path = file_path[:-(len(name_and_ext) + 1)]
    return path, name, extension


file_info = get_file_info('C:/Program Files/7-Zip/7Zip.dll')
print(file_info[0])
print(file_info[1])
print(file_info[2])
