''' A simple start to a text maze game with a single path thru the maze
Players have to choose the correct direction to get out of a room.

This also is an introduction to making objects in Python.  The 2 classes
construct the rooms and keep track of the player or make it easy to make
the game multi player. 
'''

class Room:
    def __init__ (self, name, exit):
        self.name = name
        self.exit = exit

class Player:
    lives = 3  #initial number of lives
    def __init__ (self, name, room):
        self.name = name
        self.room = room
        

# Starting room and the way out
start = Room('Entrance','l')
 
# Player object
name = input ('What is your name ?')
#put the player in the start room
player = Player(name, start)


wayout = input ("Which way out, r or l ?")
if wayout != start.exit:
    print (player.name + ' you can not go that way!')
    player.lives = 2
    print ('You have ' + str(player.lives) + ' lives left')
else:
    print ('Good')
    player.lives = 3
    
    #add code here to move player to the next room and so on
