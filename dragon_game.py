#importing random
import random
#importing time
import  time

#defining functions
def prompt():
    print ("You are in a Kingdom of Dragons")
    time.sleep(1)
    print ("In front of you, you see two caves.")
    time.sleep(1)
    print ("In one cave, the dragon is friendly and will share his treasure with you.")
    time.sleep(1)
    print ("The other dragon is hungry and will eat you on sight.\n")    
    time.sleep(1)
def cave():
    while True:
        cave = int(input("Cave 1 or 2 : "))
        if cave > 2  :
            print("Enter valid cave number")
        else:
            break
def decision():
    rand = random.randrange(10)
    num = rand

    if num > 5:
        print("You approach the cave...")
        print("A large dragon jumps out in front of you!")
        print("he opens his jaw and...\n")
        print("Gobbles you down!")
    else:
        print("You approach the cave...")
        print("A large dragon jumps out in front of you!")
        print("he opens his jaw and...\n")
        print("Greets you before share his treasure!")
    
#calling function
prompt ()


#taking user input
ans = cave()

decision()



