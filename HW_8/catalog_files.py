# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
# с учётом всех вложенных файлов и директорий.


import os
import json
import csv
import pickle
from pathlib import Path


def catalog_files(path, parent_dir=''):
    result = []
    for p in Path(path).iterdir():
        if p.is_dir():
            result += catalog_files(p, parent_dir=p)
        else:
            result.append({
                'parent_dir': parent_dir,
                'path': str(p),
                'type': 'file',
                'size': p.stat().st_size
            })
    return result


def save_catalog(path, out_dir):
    result = catalog_files(path)

    with open(os.path.join(out_dir, 'result.json'), 'w', encoding='UTF-8') as f:
        json_data = []
        for row in result:
            row['parent_dir'] = str(row['parent_dir'])
            row['path'] = str(row['path'])
            json_data.append(row)

        json.dump(json_data, f, ensure_ascii=False, indent=2)

    with open(os.path.join(out_dir, 'result.csv'), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['parent_dir', 'path', 'type', 'size'])
        for row in result:
            writer.writerow([row['parent_dir'], row['path'], row['type'], row['size']])

    with open(os.path.join(out_dir, 'result.pickle'), 'wb') as f:
        pickle.dump(result, f)


if __name__ == '__main__':
    save_catalog('../HW_8', 'files')
