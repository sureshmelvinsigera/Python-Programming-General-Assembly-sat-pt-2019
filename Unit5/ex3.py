def read_data(file_name):
    try:
        file = open(file_name, 'r')
        for line in file:
            print(line)
        file.close()
    except FileNotFoundError:
        print(file_name, 'is not exists')


if __name__ == '__main__':
    read_data('data1.txt')
