import time #For wait times between text
import random #Damage, picking from item tables, etc


#I might add player HP here but it might add to the general text adventure vibe if you just die to everything
mp = 5 #How many spells you can cast right now
deaths = 0 #Hee hee hee
level1Beat = 0 #Switches on when you beat level 1

def level1():
    choice = 0 #Avoiding syntax errors
    chance = 0 #Hah hah hah
    event1 = random.randint(1,10) #Add more later
    if event1 == 1:
        print("You continue through the twisty passages of the dark, dank dungeon.")
    elif event1 == 2:
        print("Your footsteps echo off the cold walls. It is quiet...very quiet.")
    elif event1 == 3:
        while choice > 2 or choice == 0:
            chance = random.randint(1,3)
            print("You hit a sharp corner. Will you...")
            time.sleep(0.5)
            print("1. Take the turn, or...")
            time.sleep(0.5)
            choice = int(input("2. Carefully peek around the corner? "))
            if choice == 1:
                print("You keep on going. Just a corner, after all.")
                if chance == 2:
                    print("You get shot in the side by a hidden monster!")
                    time.sleep(1)
                    print("Should've seen that coming -- the game'd never include a choice like that if one answer wasn't going to kill you.")
                    while 1 == 1:
                        print(" ")
            elif choice == 2:
                print("You sneak past the corner, sneaky-sneakily.")
                if chance == 2:
                    print("You bump into a monster!")
                    battle(30,5,0,"Kobold Thief")
                    break
            else:
                time.sleep(0.5)
    time.sleep(0.7)
    choice = 0

def battle(hp,pos,speed,mobName): #Fighting engine
        #Note to self: make this more complex. Maybe add enemy attacks?
    poison = 0 #How many times the enemy has been poisoned

    #These are here to make sure that the commands work properly.
    #(if these didn't exist the player would have to type quotation marks around the action)
    fight = "fight"
    recharge = "recharge"
    magic = "magic"
    PUNCH = "punch" #easter egg, does more damage than usual attack and uses "FUNNY" captions
    flee = "flee"
    konami = "up up down down left right left right b a start"

    #begin game
    print("The fight begins.")
    print("An " + mobName + " stands before you...!")

    while 1 == 1: #game loop
        global mp
        result = input("Fight, recharge, flee, or magic?") #this is where you input commands
        pos += speed #enemy gets closer every turn
        if result == fight:
            print("You attack your foe!")
            hp -= random.randint(1,10) + pos #your damage upon attack depends on how close the enemy is to you + a random variable
            print("Enemy HP is now", hp)
            time.sleep(1)
            print("The " + mobName + " advances slowly.")
            hp -= poison
        if result == punch: #once again, easter egg
            print("YOU PUNCH THE BADGUY.")
            time.sleep(1)
            hp -= random.randint(5,15) * pos - 1
            print("NOW HE IS")
            print(hp)
        if result == recharge:
            print("You defend yourself!") #fun fact: this command was originally "defend", but was changed to recharge because there needed to be some way to regain MP
            time.sleep(1)
            print("The " + mobName + " advances slowly.")
            mp += random.randint(0,2)
        if result == magic:
            if mp > 0:
                print("You cast a spell!")
                mp -= 1
                print("Your MP is now ", mp)
                spell = random.randint(1,4) #picks from a random assortment of spells
                if spell == 1:
                    print("FIRE BALL") 
                    time.sleep(1)
                    print("The " + mobName + " is set aflame!")
                    hp -= pos * (mp / random.randint(1,3)) #damages enemy based on current mp
                    hp -= poison
                if spell == 2:
                    print("GUST OF WIND")
                    time.sleep(1)
                    print("The " + mobName + " is knocked back!")
                    pos -= mp #changes pos based on current mp
                    hp -= poison
                if spell == 3:
                    print("Your spell fails.")
                    hp -= poison
                if spell == 4:
                    print("POISON")
                    time.sleep(1)
                    if poison != 1:
                        print("The " + mobName + " begins to lose HP, slowly!")
                    else:
                        print("The " + mobName + " loses HP at an increased speed!!")
                    poison += 1
                    hp -= poison
            else:
                print("You lack the MP required to perform an attack!")
                time.sleep(1)
                print("To regain MP, utilize the 'recharge'command!")
            

        if hp < 1: #hp is below 1
            print("The " + mobName + " has been defeated!")
            print("YOU WON!") #Alakaboom
            time.sleep(2)
            break
        
        if pos == 15:
            print("You've taken too long - the " + mobName + " is too close to escape from now!")
            time.sleep(1)
            print("You are killed.")
            print("GAME OVER.")
            deaths += 1

name = input("Please enter your name: ")
time.sleep(0.5)
print("You are " + name + ", a wizard. Many years you have studied the arcane, the mystical, the magical.")
time.sleep(1)
print("You have decided to test your skills by delving down into the dangerous Dungeon of Deceit.")

while level1Beat == 0:
    level1()
