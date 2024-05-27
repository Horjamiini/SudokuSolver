


sudoku_listlist = [[2,33,66],[5,33,133],[6,33,33],[9,33,33],[7,66,233],[1,166,266],[4,200,166],[5,200,133]]
list_c1 = []
list_c2 = []
list_c3 = []
list_c4 = []
list_c5 = []
list_c6 = []
list_c7 = []
list_c8 = []
list_c9 = []
list_r1 = []
list_r2 = []
list_r3 = []
list_r4 = []
list_r5 = []
list_r6 = []
list_r7 = []
list_r8 = []
list_r9 = []
def CreateColumnLists(list):
    for i in list:
        match i[1]:
            # First column
            case 0:
                print("1 column")
            # Second column
            case 33:
                print("2 column") 
            # Third column 
            case 66:
                print("3 column")
            # Fourth column
            case 100:
                print("4 column")
            # Fifth column
            case 133:
                print("5 column")
            # Sixth column
            case 166:
                print("6 column")
            # Seventh column
            case 200:
                print("7 column")
            # Eight column
            case 233:
                print("8 column")
            # Ninth column
            case 266:
                print("9 column")

            case _:
                print("eipä ollu")

def CreateRowLists(list):
    for i in list:
        match i[2]:
            # First row
            case 0:
                print("1 row")
            # Second row
            case 33:
                print("2 row") 
            # Third row 
            case 66:
                print("3 row")
            # Fourth row
            case 100:
                print("4 row")
            # Fifth row
            case 133:
                print("5 row")
            # Sixth row
            case 166:
                print("6 row")
            # Seventh row
            case 200:
                print("7 row")
            # Eight row
            case 233:
                print("8 row")
            # Ninth row
            case 266:
                print("9 row")

            case _:
                print("eipä ollu")



def CreateSquareLists(list):
    for i in list:
        match i[1]:
            case 0 | 33 | 66:
                match i[2]:
                    case 0 | 33 | 66:
                        print ("up left square")
                    case 100 | 133 | 166:
                        print("middle left square")
                    case 200 | 233 | 266:
                        print("down left square")

            case 100 | 133 | 166:
                 match i[2]:
                    case 0 | 33 | 66:
                        print ("up middle square")
                    case 100 | 133 | 166:
                        print("middle middle square")
                    case 200 | 233 | 266:
                        print("down middle square")

            case 200 | 233 | 266:
                match i[2]:
                    case 0 | 33 | 66:
                        print ("up right square")
                    case 100 | 133 | 166:
                        print("middle right square")
                    case 200 | 233 | 266:
                        print("down right square")

            case _:
                print("eipä ollu")
            
CreateSquareLists(sudoku_listlist)