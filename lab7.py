# Path 1: north, east, north, east, exit
# Path 2: east, north, north, east, exit
from room import Room
from maze import Maze

# Create list of rooms

my_rooms = []
my_rooms.append(Room("This is the entrance, you enter your house"))
my_rooms.append(Room("This room is the Hokage Office"))
my_rooms.append(Room("This room is the Uchiha Shrine"))
my_rooms.append(Room("YOu enter the store, welcome to Ichiraku Ramen"))
my_rooms.append(Room("This room is the Yamanaka flower shop"))
my_rooms.append(Room("This room is the Five Kage Summit"))
my_rooms.append(Room("This room is Orichimaru's secret lab"))
my_rooms.append(Room("This is your house, time to relax after a long day"))
my_rooms.append(Room("This room enters into the Forest of Death"))
my_rooms.append(Room("This room is the exit! You've reached the Final Valley"))
my_rooms.append(Room("This room is a portal to Mount Myoboku"))
my_rooms.append(Room("You've reached the Great Naruto Bridge"))
# Create connections between rooms which becomes the structure of the maze

my_rooms[0].setNorth(my_rooms[1])
my_rooms[0].setEast(my_rooms[3])
my_rooms[0].setSouth(my_rooms[7])

my_rooms[1].setSouth(my_rooms[0])
my_rooms[1].setEast(my_rooms[2])

my_rooms[2].setWest(my_rooms[1])
my_rooms[2].setNorth(my_rooms[8])
my_rooms[2].setEast(my_rooms[4])
my_rooms[2].setSouth(my_rooms[3])

my_rooms[3].setNorth(my_rooms[2])
my_rooms[3].setSouth(my_rooms[6])
my_rooms[3].setWest(my_rooms[0])
my_rooms[3].setEast(my_rooms[5])

my_rooms[4].setWest(my_rooms[2])
my_rooms[4].setSouth(my_rooms[5])

my_rooms[5].setNorth(my_rooms[4])
my_rooms[5].setWest(my_rooms[3])

my_rooms[6].setNorth(my_rooms[3])
my_rooms[6].setWest(my_rooms[7])
my_rooms[6].setSouth(my_rooms[11])

my_rooms[7].setNorth(my_rooms[0])
my_rooms[7].setEast(my_rooms[6])
my_rooms[7].setSouth(my_rooms[10])

my_rooms[8].setSouth(my_rooms[2])
my_rooms[8].setEast(my_rooms[9])

my_rooms[9].setWest(my_rooms[8])

my_rooms[10].setNorth(my_rooms[7])

my_rooms[11].setNorth(my_rooms[6])

# Create maze object, set entrance and exit
my_maze = Maze(my_rooms[0], my_rooms[9])


print(my_rooms[0])
x = True
while x:
    answer = (input('Enter direction to move north west east south restart\n'))
    if answer.lower() == 'north':
        if my_maze.getCurrent().getNorth():
            my_maze.moveNorth()
            print('You went', answer)
            print(my_maze.getCurrent())
        else:
            print('Direction invalid, try again')
            print(my_maze.getCurrent())
    elif answer.lower() == 'west':
        if my_maze.getCurrent().getWest():
            my_maze.moveWest()
            print('You went', answer)
            print(my_maze.getCurrent())
        else:
            print('Direction invalid, try again')
            print(my_maze.getCurrent())
    elif answer.lower() == 'east':
        if my_maze.getCurrent().getEast():
            my_maze.moveEast()
            print('You went', answer)
            print(my_maze.getCurrent())
        else:
            print('Invalid direction, try again')
            print(my_maze.getCurrent())
    elif answer.lower() == 'south':
        if my_maze.getCurrent().getSouth():
            my_maze.moveSouth()
            print('You went', answer)
            print(my_maze.getCurrent())
        else:
            print('Invalid direction, try again')
            print(my_maze.getCurrent())
    elif answer.lower() == 'restart':
        my_maze.reset()
        print(my_rooms[0])
    if my_maze.atExit():
        print('You found the exit!')
        x = False
