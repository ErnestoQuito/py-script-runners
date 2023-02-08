import os
from modules.commons import finder_files
from modules.commons import copy_files

source_ = r"D:\runners_source_files\notificaciones\2023\02\01"
target = r"D:\runners_target_files"
for i in finder_files(source_):
    a = copy_files(i, os.path.join(target, os.path.basename(i)))
    print(a)
