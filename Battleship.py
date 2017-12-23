
def user():
    while(True):
        display()
        try:
            changeX = int(input("Set X:"))
            changeY = int(input("Set Y:")) 
            coordinate[changeY][changeX] = 1
            if(changeX == -1 or changeY == -1):
               break
        except IndexError:
            print("\033[0;31;40mInvalid value!\033[0m")
        except ValueError:
            print("\033[0;31;40mInsert any value!\033[0m")
def AI():
    pass

def display():
    print("  ",end="")
    for i in range(10):
        print(str(i)+"  ",end="")
    print("")
    for y in range(10):
        print(y,end="")
        for x in range(10):
            if(not coordinate[y][x] == 0):
                print("[\033[0;31;40mX\033[0m]",end="")
                        #print("[\033[0;31 X \033[0;37 ]",end="")
            else:
                print("[ ]",end="")
            if(x == 9):
                print(" ")
coordinate = [[0 for x in range(10)] for y in range(10)]
display();
user();


