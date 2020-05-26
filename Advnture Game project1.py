import random
import time

def printlate(message1):
    print(message1)
    time.sleep(2.1)


def bluedoor(option,weapon):
    printlate("you have chosen first door\n\n")
    printlate("You chose to go through the blue door.There is a dark, long floor. \n\nSuddenly, you hear a sound from a room at the end of it.\n\n")
    printlate("There is  "+option+"  in the room.\n\nPress 1 to take it or press2 to leave it")
    while True:
        chosen=input("Enter any of the abovne")
        if chosen=="1":
            printlate("now you have internet connection in it ")
            printlate("You opned the google maps and searched where you are and you made a phonecall to your friend and pollice and he came to you to help and you got saved\n\n")
        elif chosen=="2":
            printlate('you refused to take it and you have no chance to escape\n\n')
            printlate("you hav waited there and there is no food.You starved for 30days and you died\n\n")
        playagain()


def reddoor(weapon,option):
    printlate("you have chosen reddoor\n\n")
    printlate("You chose to go through the blue door.There are criminals in that door who kidnaped you\n\n")
    printlate("There is  "+weapon+"  in the room.Press 1 to take it or press2 to leave it\n\n")
    while True:
        life=input(" Choose any of the above\n\n")
        if life=="1":
            printlate("you have"+weapon+"in your hand now\n\n")
            printlate("now you can save yourlife by killing them all\n\n")
            printlate("you shot them with"+weapon+"you saved your life\n\n")
        elif life=="2":
            printlate("You refused to taake it since you dont know how to fire\n\n")
            printlate("criminals have seen you and you have now weapon in your hand\n\n")
            printlate("slowly they came to you and killed you\n\n")
    playagain()


def playagain():
    printlate("do you want to play again\n\n")
    while True:
        agg=input("press1 to play again or press 2 to leave\n\n")
        if agg=="1":
            introduction()
        elif agg=="2":
            printlate("thankyou for playing\n\n")
        else:
            playagain()




def introduction():
    printlate("What did just happen?\n\n")

    printlate("Somehow, your memory of the last few hours seems to be a little blurry, and you can\'t remember how you ended up here. You take a look around, but don\'t recognize anything. You seem to be inside some form of patio, with nowhere to go.\n\n")

    printlate("But wait.In front of you, there are two doors, the left one is blue, the right one is red. You seem to feel like you're hearing a sound from inside the red door. What should you do?You can either go through the blue door, or the red door.There coud be anything in the doors. What do you want to do?\n\n")

    option=random.choice(["mobile","laptop",'iPHONE'"satellite mobile"])
    weapon=random.choice(["shotgun","pistol","m67"])

    while True:
            its_time=input("press 1 to chose blue door or press 2 to chose reddoor\n\n")
            if its_time=="1":
                bluedoor(option,weapon)
                break
            elif its_time=="2":
                reddoor(option,weapon)
                break

introduction()
