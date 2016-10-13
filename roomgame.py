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
     
    def __init__ (self, name, room):
        self.name = name
        self.room = room
        self.lifes = 3
        

# Starting room and the way out
start = Room('Entrance','l')
 
# Player object
name = input ('What is your name ?')
#put the player in the start room
player = Player(name, start)


wayout = input ("Which way out, r or l ?")
if wayout != start.exit:
    print (player.name + ' you can not go that way!')
    player.lifes = 2
    print ('You have ' + str(player.lifes) + ' lifes left')
    # same line as above, but using the print.format method
    # It saves the call to str() is easier than stringing the
    # text and variables together with + 
    print('You have {} lifes left'.format(player.lifes))
else:
    print ('Good')
    player.lifes = 3
    
    #add code here to move player to the next room and so on
