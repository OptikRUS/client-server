import re
from decoding_file import decoding_file


def get_data(files_list):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for file in files_list:
        decoding_file(file)
        with open(file, 'r') as f:
            file = f.read()
            os_prod_list.append(re.findall(r'\Изготовитель системы:\s+(.+)\b', file)[0])
            os_name_list.append(re.findall(r'\Название ОС:\s+(.+)\b', file)[0])
            os_code_list.append(re.findall(r'\Код продукта:\s+(.+)\b', file)[0])
            os_type_list.append(re.findall(r'\Тип системы:\s+(.+)\b', file)[0])

    main_data.append(os_prod_list)
    main_data.append(os_name_list)
    main_data.append(os_code_list)
    main_data.append(os_type_list)

    return main_data
