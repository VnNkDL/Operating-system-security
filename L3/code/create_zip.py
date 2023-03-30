from zipfile import ZipFile
import sys, ctypes, time, elevate
try:
    path = sys.argv[1]
except:
    exit()
#print(sys.argv)
#print(shell32.IsUserAnAdmin())
#time.sleep(10)
file_name = path[path.rfind('/')+1:]
path_name = path[:path.rfind('.')]
try:    
    zp = ZipFile(path_name+'.zip','w').write(path,file_name)
except:
    shell32 = ctypes.windll.shell32
    elevate.elevate()
    shell32.ShellExecuteW(None, 'runas', sys.executable, 'create_zip.py' , "{} {}".format(sys.executable,path), 0)