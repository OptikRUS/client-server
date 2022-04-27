import re
from decoding_file import decoding_file


def get_data(files_list=['info_1.txt', 'info_2.txt', 'info_3.txt']):
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

    for i in range(3):
        data_list = [os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]]
        main_data.append(data_list)

    return main_data
