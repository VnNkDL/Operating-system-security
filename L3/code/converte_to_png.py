import sys, elevate, ctypes
from PIL import Image
try:
    path = sys.argv[1]
except:
    exit()
file_name = path[path.rfind('/')+1:]
path_name = path[:path.rfind('.')]
try:
    img = Image.open(path)
    img.save(path_name+'.png')
except:
    shell32 = ctypes.windll.shell32
    elevate.elevate()
    shell32.ShellExecuteW(None, 'runas', sys.executable, 'create_zip.py' , "{} {}".format(sys.executable,path), 0)
