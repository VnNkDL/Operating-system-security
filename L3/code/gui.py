from tkinter import *
from tkinter import filedialog as fd
import ctypes, os

#Проверка прав
shell32 = ctypes.windll.shell32
if shell32.IsUserAnAdmin() == 1:
    exit()

#Функции для кнопок
def create_zip():
    file_name = fd.askopenfilename()
    os.system('python create_zip.py "{}"'.format(file_name))
    

def calculate_hash():
    file_name = fd.askopenfilename()
    os.system('python calculate_hash.py "{}"'.format(file_name))

def converte_to_png():
    file_name = fd.askopenfilename()
    os.system('python converte_to_png.py "{}"'.format(file_name))

#GUI
window = Tk()
window.title('Choose the operation')
window.geometry('300x200')


button_create_zip = Button(text='Create .zip', command=create_zip)
button_create_zip.place( x= 10, y = 80)
button_calculate_hash = Button(text='Calculate hash', command=calculate_hash)
button_calculate_hash.place( x= 90, y = 80)
button_convert_to_png = Button(text='Converte to png', command=converte_to_png)
button_convert_to_png.place( x= 190, y = 80)
window.mainloop()