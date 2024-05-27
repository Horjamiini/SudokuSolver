def ListTester(x,list,xpos,ypos):
    counter = 0
    saveList = []
    for i in list:
        if i[1] == xpos and i[2] == ypos:
            counter -= 1
            saveList = i
            print('Position already in list, Counter: ', counter)
        else:
            print('Position not in list adding number')

    if counter < 0:
        saveList[0] = x
        print('replace number in list')
    else:
        print('add to list')

    print(list)
    print(saveList)
    

x = 9
list1 = [[3,4,4],[1,2,3]]
list2 = [[3,3,3],[4,2,1]]
xpos = 2
ypos = 1


ListTester(x,list1,xpos,ypos)
ListTester(x,list2,xpos,ypos)