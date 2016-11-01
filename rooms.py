'''
Use a spreadsheet program to write the room, save as a csv file.
csv is short for Comma Separated File.

This is an example of what one looks like.
Classroom,A well lighted room,chalk
Basement,Dark and musty ,brick
Dungeon,Moans are heard,key

Program reads the file and converts it to a list of lists and
finally a dictionary
'''
room =[]       
roomslist=[]
 
##############  convert to a list of lists ######################
for line in open("rooms.csv"):
    line = line.strip('\n')         # lose the newline characters
    room = line.split(",")          # single room
    roomslist.append(room)          # all the rooms
 
###############  make list into a dictionary ######################
keys = []
number_of_rooms = (len(roomslist))
for i in range(number_of_rooms):
    keys.append(i)
rooms = dict(zip(keys, roomslist)) 

print (rooms)
