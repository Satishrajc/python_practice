with open("test.txt", "r") as rf:
    # print(rf.read())
    # print(rf.read(10))
    # print('---')
    # print(rf.read(10))
    #
    # for i in rf:
    #     print(i)
    #     print(i, end="")
    #
    # print(rf.readline())
    # print('---')
    # print(rf.readline())
    #
    # print(rf.readlines())

    print(rf.read(10))
    print(rf.tell())
    rf.seek(-1, 2)
    print(rf.tell())
