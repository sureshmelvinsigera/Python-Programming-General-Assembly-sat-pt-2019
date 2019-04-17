def read_data(file_name):
    file = open(file_name, 'r')
    for line in file:
        print(line)


if __name__ == '__main__':
    read_data('data.txt')
