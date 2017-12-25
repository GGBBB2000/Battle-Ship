#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def user():
    while True:
        print(count)
        display()
        if not any(iter(count.values())):
            break
        try:
            print("Which ships do you put?")
            ship = int(input("1:Aircraft charrier(5) 2:Battleship(4) 3:Submarrine(3) 4:Cruiser(3) 5:Destroyer(2) "))
            direction = int(input("Set direction of the ship; 0:column 1:row "))
            if direction != 0 and direction != 1:
                print("Chose only 0 or 1")
                continue
            changeX = int(input("Set X:"))
            changeY = int(input("Set Y:"))
            if changeX <= -1 or changeY <= -1 or changeX >= 10 or changeY >= 10:
                continue
            if ship == 1:
                if not count["AC"]:
                    print("You've already used it !")
                    continue
                if direction == 0 and changeY + 4 < 10 :
                    AC(changeX, changeY, direction)
                    #break;
                elif direction == 1 and changeX + 4 < 10:
                    AC(changeX, changeY, direction)
                    #break;
                else:
                    print("Value you set is out of range!")
            elif ship == 2:
                if not count["BS"]:
                    print("You've already used it !")
                    continue
                if direction == 0 and changeY + 3 < 10:
                    BS(changeX, changeY, direction)
                    #break;
                elif direction == 1 and changeX + 3 < 10:
                    BS(changeX, changeY, direction)
                    #break;
                else:
                    print("Value you set is out of range!")
            elif ship == 3:
                if not count["SM"]:
                    print("You've already used it !")
                    continue
                if direction == 0 and changeY + 2 < 10:
                    SM(changeX, changeY, direction)
                    #break;
                elif direction == 1 and changeX + 2 < 10:
                    SM(changeX, changeY, direction)
                    #break;
                else:
                    print("Value you set is out of range!")
            elif ship == 4:
                if not count["CR"]:
                    print("You've already used it !")
                    continue
                if direction == 0 and changeY + 2 < 10:
                    CR(changeX, changeY, direction)
                elif direction == 1 and changeX + 2 < 10:
                    CR(changeX, changeY, direction)
                    #break;
                else:
                    print("Value you set is out of range!")
            elif ship == 5:
                if not count["DE"]:
                    print("You've already used it !")
                    continue
                if direction == 0 and changeY + 1 < 10:
                    DE(changeX, changeY, direction)
                elif direction == 1 and changeX + 1 < 10:
                    DE(changeX, changeY, direction)
                    #break;
                else:
                    print("Value you set is out of range!")
            else:
                print("\033[0;31;40mWrong number!\33[0m")
            #coordinate[changeY][changeX] = 1

        except IndexError:
            print("\033[0;31;40mInvalid value!\033[0m")
        except ValueError:
            print("\033[0;31;40mInsert any value!\033[0m")

def AI():
    pass

def display():
    print("  ", end="")
    for i in range(10):
        print(str(i) + "  ", end="")
    print("")
    for y in range(10):
        print(y, end="")
        for x in range(10):
            if not coordinate[y][x] == 0:
                print("[\033[0;31;40mX\033[0m]", end="")
            else:
                print("[ ]", end="")
            if x == 9:
                print(" ")

def AC(x, y, direction):
    if not check_coordinate(5,x,y,direction):
        print("\033[0;31;40mAny ship already there!\033[0m]")
        return
    else:
        #This is a aircraft carrier which has 5 space
        for i in range(5):
            if direction == 0:
                coordinate[y + i][x] = 1
            else:
                coordinate[y][x + i] = 1
            count["AC"] = False 
def BS(x, y, direction):
    #This is a battleship which has 4 space
    if not check_coordinate(4,x,y,direction):
        print("\033[0;31;40mAny ship already there!\033[0m]")
        return
    else:
        for i in range(4):
            if direction == 0:
                coordinate[y + i][x] = 1
            else:
                coordinate[y][x + i] = 1
        count["BS"] = False
def SM(x, y, direction):
    if not check_coordinate(3,x,y,direction):
        print("\033[0;31;40mAny ship already there!\033[0m]")
        return
    #This is a submarine which has 3 space
    else:
        for i in range(3):
            if direction == 0:
                coordinate[y + i][x] = 1
            else:
                coordinate[y][x + i] = 1
            count["SM"] = False
def CR(x, y, direction):
    if not check_coordinate(3,x,y,direction):
        print("\033[0;31;40mAny ship already there!\033[0m]")
        return
    #This is a submarine which has 3 space
    else:
        for i in range(3):
            if direction == 0:
                coordinate[y + i][x] = 1
            else:
                coordinate[y][x + i] = 1
            count["CR"] = False
def DE(x, y, direction):
    #This is a destroyer which has 2 space
    if not check_coordinate(2,x,y,direction):
        print("\033[0;31;40mAny ship already there!\033[0m]")
        return
    else:
        for i in range(2):
            if direction == 0:
                coordinate[y + i][x] = 1
            else:
                coordinate[y][x + i] = 1
            count["DE"] = False
def check_coordinate(n,x,y,direction):
    if direction == 0:
        for i in range(n):
            if coordinate[y + i][x] == 0:
                pass
            else:
                return False
        return True
    else:
        for i in range(n):
            if coordinate[y][x + i] == 0:
                pass
            else:
                print("False")
                return False
        return True

if __name__ == '__main__':
    coordinate = [[0 for _ in range(10)] for _ in range(10)]
    count = {"AC":True,"BS":True,"SM":True,"DE":True,"CR":True}
    user()
