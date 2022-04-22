# Написать скрипт, который выводит статистику для заданной папки в виде
# словаря, в котором ключи — верхняя граница размера файла (пусть будет
# кратна 10),
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]),
# например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке,
# где запустили скрипт.

import os
import json
from pprint import pprint

root_dir = 'c:\Python310'

l_100 =  [0, set()]
l_1000 =  [0, set()]
l_10000 =  [0, set()]
l_100000 =  [0, set()]
l_1000000 =  [0, set()]
l_10000000 =  [0, set()]

# Обход папок и подпапок в поисках всех файлов
for root, dirs, files in os.walk(root_dir):
    for file in files:
        f_ext = file.split('.')[-1].lower()
        f_path = os.path.join(root, file)
        f_size = os.stat(f_path).st_size
        # В зависимости от размера файла вносим изменения
        # в соответствующую категорию.
        # Найденные расширения файлов добавляем в позицию set(),
        # чтобы получить сразу уникальные значения.
        if f_size <= 100:
            l_100[0] += 1
            l_100[1].add(f_ext)
        if 100 < f_size <= 1000:
            l_1000[0] += 1
            l_1000[1].add(f_ext)
        if 1000 < f_size <= 10000:
            l_10000[0] += 1
            l_10000[1].add(f_ext)
        if 10000 < f_size <= 100000:
            l_100000[0] += 1
            l_100000[1].add(f_ext)
        if 100000 < f_size <= 1000000:
            l_1000000[0] += 1
            l_1000000[1].add(f_ext)
        if 1000000 < f_size <= 10000000:
            l_100[0] += 1
            l_100[1].add(f_ext)
        if 1000000 < f_size <= 10000000:
            l_10000000[0] += 1
            l_10000000[1].add(f_ext)

# Преобразуем множество с расширениями в заданный по условию список
l_100[1] = list(l_100[1])
l_1000[1] = list(l_1000[1])
l_10000[1] = list(l_10000[1])
l_100000[1] = list(l_100000[1])
l_1000000[1] = list(l_1000000[1])
l_10000000[1] = list(l_10000000[1])

# Создаём словарь с значениями в виде кортежей
res_dict = {100:tuple(l_100),
            1000:tuple(l_1000),
            10000:tuple(l_10000),
            100000:tuple(l_100000),
            1000000:tuple(l_1000000),
            10000000:tuple(l_10000000)
           }

#pprint(res_dict)
# {100: (241,
#        ['voc',
#         'typed',
#         'rst',
#     ...
# 10000000: (11, ['chm', 'txt', 'pyd', 'dll', 'whl'])}

out_file_name = os.path.basename(root_dir) + '_summary.json'
with open(out_file_name, 'w', encoding='utf-8') as f:
    json.dump(res_dict, f, sort_keys=True)
if out_file_name:
    print("Результат сохранён в файл {}".format(out_file_name))

# Условие получить ключи в виде кортежа с списком внутри вынуждает
# проводить разные необязательные преобразования.
