import winapps, json
from datetime import datetime as dt

def check_dir(path, directions):#Проверка на нахождения в исключающейся директории
    for dir in directions:
        if dir not in str(path):
            continue
        else:
            return False
    return True

def get_all_app():
    #Список приложений
    list_of_app = winapps.search_installed()
    publisher, publisher_apps = [], []

    #Загружаем config.json
    with open('config.json','r') as configuration_file:
        all_line = json.load(configuration_file)

    blacklist_publisher = all_line['blacklistpublisher']#Не показывать publisher-ы из списка
    blacklist_dir = all_line['blacklistdir']#Не показывать publisher-ы находящиеся в dir

    #Из всех полей сохраняем publisher и name
    for app in list_of_app:
        if app.publisher not in blacklist_publisher and check_dir(app.install_location,blacklist_dir):
            if app.publisher in publisher:
                publisher_apps[publisher.index(app.publisher)].append(app.name)
            else:
                if app.publisher is None:
                    publisher.append(str(app.publisher))
                else:
                    publisher.append(app.publisher)
            publisher_apps.append([app.name])
    
    #Создание словаря и его сортировка
    publisher_with_apps = dict(zip(publisher, publisher_apps))
    sorted_publisher_with_apps = dict(sorted(publisher_with_apps.items(), key= lambda x : -len(x[1])))

    #Вывод в .json
    filename = dt.now().strftime("%d%m%Y_%H%M%S")+'.json'
    with open(filename, 'w', encoding = 'utf-8') as date:
        json.dump(sorted_publisher_with_apps, date, indent = 4, ensure_ascii = False, separators = (',', ': '))    

    #Вывод на экран
    for pub, apps in sorted_publisher_with_apps.items():
        print('Publisher: {} \nApps:'.format(pub))
        for app in apps:
            print('\t-'+app) 

get_all_app()
