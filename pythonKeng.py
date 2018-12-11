def myFunc(working_list=[]):
    if working_list is None:
        working_list = []
    working_list.append("a")
    print(working_list)

myFunc()
myFunc()
myFunc()