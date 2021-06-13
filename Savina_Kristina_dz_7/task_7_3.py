"""
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
"""
import os
import shutil

if not os.path.exists('--my_project\\--templates'):
    os.mkdir('--my_project\\--templates')

for root, dir, files in os.walk('--my_project'):
    for file in files:
        if file.lower().endswith('.html'):
            file_way = os.path.join(root, file)
            folder_way = os.path.dirname(file_way)
            folder_name = os.path.split(folder_way)[-1]
            if not os.path.exists(f'--my_project\\--templates\\{folder_name}'):
                os.mkdir(f'--my_project\\--templates\\{folder_name}')
            if not os.path.exists(f'--my_project\\--templates\\{folder_name}\\{file}'):
                shutil.copy(file_way, f'--my_project\\--templates\\{folder_name}')
