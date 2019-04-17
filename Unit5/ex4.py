def read_data(file_name):
    file = open(file_name, 'r')
    data = {}
    counter = 1
    try:
        for line in file:
            field = line.split(" ")
            # read the data, and adding to the dictionary.
            data['invoice' + str(counter)] = field[0]
            data['items'] = field[1]
            data['price'] = field[2]
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
