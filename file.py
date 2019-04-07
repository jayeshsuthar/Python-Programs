import os
from datetime import datetime

for dirpath, dirname, filenames in os.walk(os.getcwd()):
    print('Current path: ',dirpath)
    print('Directories: ',dirname)
    print('Files: ',filenames)
    print()
