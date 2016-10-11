''' A simple start to a text maze game with a single path thru the maze
Players have to choose the correct direction to get out of a room.

This also is an introduction to making objects in Python.
'''
class Player:
     
    def __init__ (self, name, room):
        self.lifes = 2
        self.name = name
        self.room = room
        
    def info(self):
        print ('Hi {}.  Your room {}. You have {} lifes left' \
        .format(self.name, self.room, self.lifes))
        print ('*'* 60)
        
    def change_room(self):
         self.room += 1
        # print (self.room)
         return (self.room)
    
    def win(self):
        pass

    def lose(self):
        self.lifes = self.lifes -1
        if self.lifes == 0:
            print ('Sorry Jack, Your dead!')
            
################### SETUP #####################

print('Can you find your way thru the house? \nl for left and r for right \n')
        
rooms = {1:['Entry','l',' You are standing in front of an abandoned house '\
'There is a door on the left and right. It starts to rain.'],
    2:['Hallway','l','You are in the Hallway.'],
    3:['Living Room','l','You are in the living room.']
    }       #add rooms by addding items to the dictionary

room = 0                    #first room is counted from zero!
# First Player object
name = input ('What is your name ? ')
# put the player in the start room
player = Player(name, room)
room_numbers = list (rooms.keys())      #list of room numbers
room_info = list(rooms.values())           #list of room data

################### GAME LOOP goes here ###################
while player.lifes > 0:
    if player.room > 2:
        break
    #   Current room
    player.info()
    room_name = room_info[player.room][0]
    wayout = room_info[player.room][1]
    description = room_info [player.room][2]

    #check for wayout, 
    whichway = input (description + ' Choose the way ')
    if whichway == wayout:
        player.change_room()   #go to next room
        print ('You have chosen well ' + player.name)
    else:
        player.lose()
