"""
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
"""
import os

folder = {'--my_project': ['--settings', '--mainapp', '--adminapp', '--authapp']}
for folders in folder.keys():
    for check in folder[folders]:
        if not os.path.exists(f'{folders}\\{check}'):
            os.makedirs(f'{folders}\\{check}')
