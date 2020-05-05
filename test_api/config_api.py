import requests
import json


# получение запросов из API
def set_api(*args):
    list_of_json = []

    for arg in args:
        
        if arg[0] == 'sum':
            req = requests.get('https://api.covid19api.com/summary')
            jfile = req.json()
            for i in range(len(jfile['Countries'])):
                if jfile['Countries'][i]['Slug'] == arg[1]:
                    list_of_json.append(jfile['Countries'][i])
        
        elif arg[0] == 'daily':
            params = {'from': arg[3], 'to': arg[4]}
            req = requests.get(
                f'https://api.covid19api.com/country/{arg[1]}/status/{arg[2]}', params=params)
            jfile = req.json()

            for i in range(len(jfile)):
                if arg[5] != None and arg[6] != None:
                    if jfile[i]['Province'] == arg[5] and jfile[i]['City'] == arg[6]:
                        list_of_json.append(jfile[i])
                elif arg[5] != None:
                    if jfile[i]['Province'] == arg[5]:
                        list_of_json.append(jfile[i])
                else:
                    list_of_json.append(jfile[i])

    return list_of_json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# создание файла с расширением .json, в формате ключ:значение ("united-kingdom" : "United Kingdom")
def json_country():
    
    # попытка прочесть файл, если тот существует
    try:
        with open('jso.json') as data_file:
            data = json.load(data_file)
    
    # в случае отсутствия такого файла, выполнится следующий блок кода
    except IOError:
        
        req = requests.get('https://api.covid19api.com/summary')
        jfile = req.json()
        length_of_json = len(jfile['Countries'])
        
        file = open("jso.json", "w")
        file.write('{')
        for i in range(length_of_json):
            key = jfile['Countries'][i]['Slug'] # ключ
            value = jfile['Countries'][i]['Country'] # значение
            if i + 1 == length_of_json:
                file.write(f'"{key}" : "{value}"\n')
            else:
                file.write(f'"{key}" : "{value}",\n')
        file.write('}')
        file.close()

        with open('jso.json') as data_file:
            data = json.load(data_file)
    
    return data


def check_country(slug):
    ctr = json_country()[slug]
    return ctr
