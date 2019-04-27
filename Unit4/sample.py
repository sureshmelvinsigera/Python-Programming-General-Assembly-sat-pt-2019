foo = 1  # global


def func():
    bar = 2  # local
    print(globals())  # prints variable foo from global scope
    print(locals())  # prints variable bar from local scope


func()
