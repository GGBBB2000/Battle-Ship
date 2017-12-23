
def user():
    while(True):
        display()
        try:
            print("Which ships do you put?")
            ship = int(input("1:Aircraft charrier 2:Battleship 3:Submarrine 4:Destroyer "))
            direction =int(input("Set direction of the ship; 0:column 1:row "))
            if(direction == 1 or direction == 0):
                pass
            else:
                print("Chose only 0 or 1")
                continue
            changeX = int(input("Set X:"))
            changeY = int(input("Set Y:"))
            if(ship ==1):
                if(direction ==0 and changeY+4 < 10):
                    AC(changeX,changeY,direction)
                    #break;
                elif(direction==1 and changeX+4 < 10):
                    AC(changeX,changeY,direction)
                    #break;
                print("Value you set is out of range!")
            elif(ship == 2):
                if(direction == 0 and changeY+3 < 10):
                    BS(changeX,changeY,direction)
                    #break;
                elif(direction == 1 and changeX+3 < 10):
                    BS(changeX,changeY,direction)
                    #break;
                print("Value you set is out of range!")
            elif(ship == 3):
                if(direction == 0 and changeY+2 < 10):
                    SM(changeX,changeY,direction)
                    #break;
                elif(direction == 1 and changeX+2 < 10):
                    SM(changeX,changeY,direction)
                    #break;
                print("Value you set is out of range!")
            elif(ship == 4):
                if(direction == 0 and changeY+1 < 10):
                    DE(changeX,changeY,direction)
                elif(direction == 1 and changeX+1 <10):
                    DE(changeX,changeY,direction)
                    #break;
                print("Value you set is out of range!")
            else:
                print("\033[0;31;40mWrong number!\33[0m")            
            #coordinate[changeY][changeX] = 1
            if(changeX <= -1 or changeY <= -1 or changeX >=10 or changeY >=10):
               continue
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
            else:
                print("[ ]",end="")
            if(x == 9):
                print(" ")
def AC(x,y,direction):
    #This is a aircraft carrier which has 5 space
    if(direction == 0):
        for i in range(5):
            coordinate[y+i][x] = 1
    else:
        for i in range(5):
            coordinate[y][x+i] = 1

def BS(x,y,direction):
    #This is a battleship which has 4 space
    if(n == 0):
        for i in range(4):
            coordinate[y+i][x] = 1
    else:
        for i in range(4):
            coordinate[y][x+i] = 1

def SM(x,y,direction):
    #This is a submarine which has 3 space
    if(direction == 0):
        for i in range(3):
            coordinate[y+i][x] = 1
    else:
        for i in range(3):
            coordinate[y][x+i] = 1

def DE(x,y,direction):
    #This is a destroyer which has 2 space
    if(direction == 0):
        for i in range(2):
            coordinate[y+i][x] = 1
    else:
        for i in range(2):
            coordinate[y][x+i] = 1
coordinate = [[0 for x in range(10)] for y in range(10)]
user()

