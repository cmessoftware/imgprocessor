from os import walk
import pathlib

# folder path
dir_path = r'./img'

# list to store files name
res = []
for (dir_path, dir_names, file_names) in walk(dir_path):
     res.extend(file_names)

res = [f for f in walk(dir_path) if pathlib.Path(f).suffix == 'jpg']
print(res)