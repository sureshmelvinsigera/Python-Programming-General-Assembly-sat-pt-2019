def foo(debug=0):
    """

    :param debug: By default set to zero
    :return:
    """
    if debug:
        print('In debug mode')
    else:
        print("Not in debug mode")
    print("part of the foo")


foo()
