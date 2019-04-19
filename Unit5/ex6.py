def append_data(line, fname='insertdata.txt'):
    f = open(fname, 'a')
    f.write(line)


if __name__ == '__main__':
    append_data('This is another line\n')
