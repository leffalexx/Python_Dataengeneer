# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать
# только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


import os


def batch_rename(path, new_name, counter_digits, ext='', new_ext='', name_range=None):
    files = os.listdir(path)

    for i, f in enumerate(files):
        if not f.endswith(ext):
            continue

        num = str(i + 1).zfill(counter_digits)

        if name_range:
            name = f[name_range[0] - 1:name_range[1]]
        else:
            name = ''

        new_filename = f'{new_name}{name}{num}.{new_ext}'
        os.rename(os.path.join(path, f), os.path.join(path, new_filename))


if __name__ == '__main__':
    batch_rename('files', 'doc', 3, 'txt', 'doc', [1, 5])
