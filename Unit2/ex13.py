choice = ''

while True:
    # print the menu
    print("========== Welcome to Captial One ==========")
    print("Please select from the following menu options")
    print("To check account balance, press C")
    print("To deposit a cheque, press D")
    print("To withdraw, press W")
    print("To exit, press X")

    # get the user selected menu option
    choice = input("Please enter the choice : ")

    if choice == 'B':
        print('Check balance')
    elif choice == 'D':
        print('Deposit cheque')
    elif choice == 'X' or choice == 'x':
        print("Good bye")
        exit()
    else:
        print('Wrong choice')
