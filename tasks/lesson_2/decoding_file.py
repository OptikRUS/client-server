from chardet import detect


def decoding_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        decoded_data = data.decode(detect(data)['encoding'])

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(decoded_data)
