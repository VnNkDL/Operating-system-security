import wmi, json
from datetime import datetime as dt
from tkinter import *
from tkinter import messagebox
all_names = [
    'Наличие антивирусов',
    'Активность антивирусов',
    'Сигнатуры антивирусов',
    'Сетевая защита',
    'Центр обновлений',
    'Название процессора', 
    'Количество ядер', 
    'Загруженность процессора',
    'Количество RAM',
    'Загруженность RAM',
    'Общая память дисков',
    'Свободная память дисков'
]

computer = wmi.WMI()

#Антивирус
def antivirus_name_string():
    print('click')
    names = ''
    antiviruses = wmi.GetObject('winmgmts:\\\\.\\root\\SecurityCenter2').InstancesOf('AntiVirusProduct')
    for antivirus in antiviruses:
        names += '\n\t\t\t' + antivirus.displayName
    return names

def antivirus_name_json():
    print('click')
    names = []
    antiviruses = wmi.GetObject('winmgmts:\\\\.\\root\\SecurityCenter2').InstancesOf('AntiVirusProduct')
    for antivirus in antiviruses:
        names.append(antivirus.displayName)
    return names

def antivirus_working_string():
    print('click')
    result = ''
    antiviruses = wmi.GetObject('winmgmts:\\\\.\\root\\SecurityCenter2').InstancesOf('AntiVirusProduct')
    for antivirus in antiviruses:
        result += '\n\t\t\t' + antivirus.displayName
        status = hex(antivirus.productState)
        if(status[3:5] == '10'):
            result += ' включён'
        else:
            result += ' выключен'
    return result

def antivirus_working_json():
    print('click')
    result= []
    antiviruses = wmi.GetObject('winmgmts:\\\\.\\root\\SecurityCenter2').InstancesOf('AntiVirusProduct')
    for antivirus in antiviruses:
        string = antivirus.displayName
        status = hex(antivirus.productState)
        if(status[3:5] == '10'):
            string += ' включён'
        else:
            string += ' выключен'
        result.append(string)
    return result

def antivirus_signature_string():
    print('click')
    result = ''
    antiviruses = wmi.GetObject('winmgmts:\\\\.\\root\\SecurityCenter2').InstancesOf('AntiVirusProduct')
    for antivirus in antiviruses:
        result += '\n\t\t\t' + antivirus.displayName
        status = hex(antivirus.productState)
        if(status[5:7] == '10'):
            result += ' не требует обновление'
        else:
            result += ' требует обновление'
    return result

def antivirus_signature_json():
    print('click')
    result = []
    antiviruses = wmi.GetObject('winmgmts:\\\\.\\root\\SecurityCenter2').InstancesOf('AntiVirusProduct')
    for antivirus in antiviruses:
        string = antivirus.displayName
        status = hex(antivirus.productState)
        if(status[5:7] == '10'):
            string += ' не требует обновление'
        else:
            string += ' требует обновление'
        result.append(string)
    return result

#Сетевая защита
def firewall():
    print('click')
    firewall = computer.Win32_Service(Name='mpssvc')
    return firewall[0].State

#Обновления ОС
def system_version():
    print('click')
    system = computer.Win32_Service(Name='wuauserv')
    return system[0].State

#Остальная информация
def processor_name():
    print('click')
    return computer.Win32_Processor()[0].Name

def processor_number_cores ():
    print('click')
    return str(computer.Win32_Processor()[0].NumberOfCores)

def processor_workload():
    print('click')
    return '{:2.2%}'.format(computer.Win32_Processor()[0].LoadPercentage / 100)

def ram_all():
    print('click')
    all_roam = int(computer.Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576
    return '{:3.3f} Gb'.format(all_roam)

def ram_workload():
    print('click')
    all_roam = int(computer.Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576
    free_roam = int(computer.Win32_OperatingSystem()[0].FreePhysicalMemory) / 1048576
    return '{:2.2%}'.format(free_roam/all_roam)

def disk_all_space_string(): 
    print('click')
    all_space = ''
    disks = computer.Win32_LogicalDisk()
    for dsk in disks:
        space = int(dsk.Size)/1073741824
        all_space += '\n\t\t' + dsk.Name + ' {:4.3f} Gb'.format(space)
    return all_space

def disk_all_space_json(): 
    print('click')
    all_space = []
    disks = computer.Win32_LogicalDisk()
    for dsk in disks:
        space = int(dsk.Size)/1073741824
        all_space.append(dsk.Name + ' {:4.3f} Gb'.format(space))
    return all_space

def disk_free_space_string():
    print('click')
    free_space = ''
    disks = computer.Win32_LogicalDisk()
    for dsk in disks:
        space = int(dsk.FreeSpace)/1073741824
        free_space += '\n\t\t' + dsk.Name + ' {:4.3f} Gb'.format(space)
    return free_space

def disk_free_space_json():
    print('click')
    free_space = []
    disks = computer.Win32_LogicalDisk()
    for dsk in disks:
        space = int(dsk.FreeSpace)/1073741824
        free_space.append(dsk.Name + ' {:4.3f} Gb'.format(space)) 
    return free_space

#Список всех функций
all_functions_string = [
    antivirus_name_string(),
    antivirus_working_string(),
    antivirus_signature_string(),
    firewall(),
    system_version(),
    processor_name(),
    processor_number_cores(),
    processor_workload(),
    ram_all(),
    ram_workload(),
    disk_all_space_string(),
    disk_free_space_string()
]
all_functions_json = [
    antivirus_name_json(),
    antivirus_working_json(),
    antivirus_signature_json(),
    firewall(),
    system_version(),
    processor_name(),
    processor_number_cores(),
    processor_workload(),
    ram_all(),
    ram_workload(),
    disk_all_space_json(),
    disk_free_space_json()
]

#Операции для кнопок
def information_string():
    information = ''
    for position in range(len(all_names)):
        if (checkboxes_state[position].get()):
            information += all_names[position]+' : '+all_functions_string[position]+'\n'
    return information

def information_json():
    request, answer = [], []
    for position in range(len(all_names)):
        if (checkboxes_state[position].get()):
            request.append(all_names[position])
            answer.append(all_functions_json[position])
    return dict(zip(request,answer))

def show_info():
    text_information.set(information_string())

def create_json():
    filename = dt.now().strftime("%d%m%Y_%H%M%S")+'.json'
    with open(filename, 'w', encoding = 'utf-8') as date:
        json.dump(information_json(), date, indent = 4, ensure_ascii = False, separators = (',', ': '))
    messagebox.showinfo('Создание json', filename+' создан')        

#GUI
window = Tk()
window.title('Данные системы')
window.geometry('600x500')

#Checkboxes 
checkboxes, checkboxes_state = [], []
for position in range(len(all_names)):
    checkbox_state = BooleanVar()
    checkbox_state.set(False)
    checkboxes_state.append(checkbox_state)
    checkbox = Checkbutton(window, text = all_names[position], var = checkboxes_state[position])
    checkbox.place(x = 0, y = 20*position)
    checkboxes.append(checkbox)

#Для вывода текста
text_information = StringVar()
area_info = Label(textvariable = text_information, justify = LEFT)
area_info.place(x = 200, y = 1)

#Кнопки
btn_show_info = Button(window, text = 'Вывести', command = show_info)
btn_show_info.place(x = 5, y = 250)
btn_write_json = Button(window, text = 'Создать json', command = create_json)
btn_write_json.place(x = 85, y = 250)

window.mainloop()