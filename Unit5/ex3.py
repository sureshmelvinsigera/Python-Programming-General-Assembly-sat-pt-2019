def read_data(file_name):
    file = open(file_name, 'r')
    try:
        for line in file:
            print(line)
    except FileNotFoundError:
        print(file_name, 'is not exists')
    finally:
        file.close()


if __name__ == '__main__':
    read_data('data1.txt')
