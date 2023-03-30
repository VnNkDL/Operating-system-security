import wmi, json
from elevate import elevate
from datetime import datetime as dt

elevate()
computer = wmi.WMI()
with open('config.json','r') as configuration_file:
    all_line = json.load(configuration_file)

blacklist_way = all_line['blacklistedapps']
blacklist_name = []
for way in blacklist_way:
    blacklist_name.append(way[way.rfind('\\')+1:])

process_watcher = computer.Win32_Process.watch_for('creation')

file_name = 'log'+dt.now().strftime("%d%m%Y_%H%M%S")+'.txt'

while True:
    process = process_watcher()
    information = 'Process Name: {} | ID: {} | Way: {} '.format(process.Name,process.ProcessId,process.ExecutablePath)
    str = dt.now().strftime("%d-%m-%Y %H:%M:%S ")
    if (process.ExecutablePath in blacklist_way or process.Name in blacklist_name):
        str += '[BANNED] '
    str += information
    log_file = open(file = file_name,mode = 'a+')
    log_file.write(str+'\n')
    if(process.ExecutablePath in blacklist_way or process.Name in blacklist_name):
        if(process.Terminate()):
            str = dt.now().strftime("%d-%m-%Y %H:%M:%S")
            str += ' [BANNED] '+information+' Stoped'
            log_file.write(str+'\n')
        else:
            str = dt.now().strftime("%d-%m-%Y %H:%M:%S")
            str += ' [BANNED] '+information+' Not stoped'
            log_file.write(str+'\n')
    log_file.close()
            
