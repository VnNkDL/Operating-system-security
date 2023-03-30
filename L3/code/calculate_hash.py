import filehash, sys, elevate, ctypes
try:
    path = sys.argv[1]
except:
    exit()
file_name = path[path.rfind('/')+1:]
path_name = path[:path.rfind('.')]
try:
    file_hash = filehash.FileHash('md5')
    answer = file_hash.hash_file(path)
    save_file = open(path_name+'_hash.txt', 'a')
    save_file.write(answer)
    save_file.close()
except:
    shell32 = ctypes.windll.shell32
    elevate.elevate()
    shell32.ShellExecuteW(None, 'runas', sys.executable, 'create_zip.py' , "{} {}".format(sys.executable,path), 0)
