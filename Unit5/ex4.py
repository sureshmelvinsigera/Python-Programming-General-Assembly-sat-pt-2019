def read_data(file_name):
    data = {}
    counter = 1
    try:
        file = open(file_name, 'r')
        for line in file:
            field = line.split(" ")
            data['invoice' + str(counter)] = field[0]
            data['items'] = field[1]
            data['price'] = field[2]
            counter += 1
        file.close()
        return data
    except FileNotFoundError:
        print(file_name, 'is not exists')


if __name__ == '__main__':
    data = read_data('cvs.txt')
    print(data)
