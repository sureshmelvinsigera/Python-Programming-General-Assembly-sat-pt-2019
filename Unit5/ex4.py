def read_data(file_name):
    file = open(file_name, 'r')
    data = {}
    counter = 1
    try:
        for line in file:
            field = line.split(';')
            # read the data, and adding to the dictionary.
            # print(field[0], ' ', field[1], ' ', field[2])
            data['id_' + str(counter)] = field[0]
            data['item' + str(counter)] = field[1]
            data['price' + str(counter)] = field[2]

            counter += 1
        # closing the file
        file.close()
        # returning the data dictionary
        return data
    except FileNotFoundError:
        print(file_name, 'is not exists')
    finally:
        file.close()


if __name__ == '__main__':
    data = read_data('cvs.txt')
    print(data)
