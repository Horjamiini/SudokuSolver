
## Logic for adding user input to list
def ListLogic(x,list,xpos,ypos):
    counter = 0
    ## Check if clicked poistion already has a number
    if len(list) != 0:
        for i in list:
            if i[1] == xpos and i[2] == ypos:
                counter -= 1
                saveList = i
                print('Position found')

        # If rect already had number replace it with the new input
        if counter < 0:
            saveList[0] = x
            
        # if rect didn't have number, add number 
        else:
            list.append([x,xpos,ypos])

    else:
        list.append([x,xpos,ypos])