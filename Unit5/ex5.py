def write_data(file_name, text):
    file = open(file_name, 'w')
    try:
        file.write(text)
    except IOError:
        print('Unable to create file on disk.')
    finally:
        file.close()


if __name__ == '__main__':
    write_data('insertdata.txt', "This is my sample text")
