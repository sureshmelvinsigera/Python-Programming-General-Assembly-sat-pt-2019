def foo1():
    print("This is foo one")
    print("Calling the foo two")
    foo2()
    print("Done calling the foo2, back to foo one")


def foo2():
    print("This is foo two")


foo1()
