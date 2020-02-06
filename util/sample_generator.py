# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.
from random import randrange, uniform
import random, copy

class Room:
    def __init__(self, id, name, description, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __repr__(self):
        if self.e_to is not None:
            return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        return f"({self.x}, {self.y})"
    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)
    def get_room_in_direction(self, direction):
        return getattr(self, f"{direction}_to")

class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
        self.startingRoom = None
        self.rooms = {}
        self.occupied = set()

    def getRandomDirection(self, room, coords):
        """
        Select a random direction from all valid connections.
        This checks if the connection is unnoccupied and if the
        adjacent grid is also unoccupied.
        """
        dirs = []
        if room.n_to is None and self._checkCoordinates(coords, "n"):
            dirs.append("n")
        if room.s_to is None and self._checkCoordinates(coords, "s"):
            dirs.append("s")
        if room.w_to is None and self._checkCoordinates(coords, "w"):
            dirs.append("w")
        if room.e_to is None and self._checkCoordinates(coords, "e"):
            dirs.append("e")
        random.shuffle(dirs)
        if len(dirs) > 0:
            return dirs[0]
        else:
            return None

    def _updateCoordinates(self, coords, direction):
        """
        Increment xy coordinates in one direction
        """
        new_coords = list(coords)
        if direction == "n":
            new_coords[1] += 1
        if direction == "s":
            new_coords[1] -= 1
        if direction == "e":
            new_coords[0] += 1
        if direction == "w":
            new_coords[0] -= 1
        return new_coords

    def _checkCoordinates(self, coords, direction):
        # """
        # Check if the grid in an adjoining direction is unoccupied
        # """
        return str(self._updateCoordinates(coords, direction)) not in self.occupied

    ####
    # MODIFY THIS CODE
    ####
    def generate_rooms(self, size_x, size_y, numRooms):
        """
        Generate a random graph of rooms
        """
        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range( len(self.grid) ):
            self.grid[i] = [None] * size_x

        self.rooms = {}

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        # The coordinates of our room. We start from middle of display
        x = (self.width // 2)-1
        y = (self.height // 2)
        print(x,y)
  
        # Create a list that will hold the IDs of rooms with valid connections available
        validRooms = []

        # Create n rooms
        for i in range(0, numRooms):
            
            if i == 0:
                # Create the starting room
                validRooms.append(i)
                new_room = Room(i, "The starting Room", "This is the starting room.", x, y)
                self.rooms[i] = new_room
                self.grid[y][x] = new_room
                self.occupied.add(str([x,y]))
                # print("self.occupied: ",self.occupied)
                # print("validRooms: ", validRooms)
            else:
                # If it's not the first room....
                # ...connect to the previous room in a random direction
                random_dir = None
               
                # In case we run into a room with no valid connections, keep looping
                # until we find a room with valid connections.
                # Note that there will ALWAYS be a valid room available
                while random_dir is None:
                    print("valideRooms: ",validRooms)
                    # Get a room that we think is valid
                    connectingRoom = validRooms[0]
                    del validRooms[0]
                    # Get the coordinates of that room
                    x = self.rooms[connectingRoom].x
                    y = self.rooms[connectingRoom].y
                    # See if we can get a random direction from that room
                    random_dir = self.getRandomDirection(self.rooms[connectingRoom], [x,y])
                    print("random_dir: ",random_dir)
                    # If our room is valid (i.e. not None) then we put it back in our
                    # set of valid rooms.
                    if random_dir is not None:
                        validRooms.append(connectingRoom)
                        print("validRooms after appending: ", validRooms)
                    # If it's NOT valid, then we don't put it back into validRooms
                    # and we try again with a different room.


                # We have a valid direction, so update the room and make the connection
                xy = self._updateCoordinates([x,y], random_dir)
                x,y = xy[0], xy[1]

                # Create a room
                new_room = Room(i, "Another room", "This is another room.", x, y)
                self.rooms[i] = new_room
                self.grid[y][x] = new_room

                self.rooms[connectingRoom].connect_rooms(new_room, random_dir)
                print(self.rooms[connectingRoom].get_room_in_direction(random_dir))
                validRooms.append(i)
                self.occupied.add(str([x,y]))
                new_room.x, new_room.y = x,y
            

            random.shuffle(validRooms)
            


        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        if len(self.occupied) == numRooms:
            print("World successfully created!")
        elif len(self.occupied) < numRooms:
            print(len(self.occupied))
        else:
            print("Something is wrong....")

        return self.rooms

# class World:
#     def __init__(self):
#         self.grid = None
#         self.width = 0
#         self.height = 0
#         self.rooms = dict()
#         self.rooms_w_avail_dir = set()
#         self.startingRoom = None

#     def _new_room_coords(self, coords, direction):
#         """
#         Increment xy coordinates in one direction
#         """
#         new_coords = list(coords)
#         if direction == "n":
#             new_coords[1] += 1
#         if direction == "s":
#             new_coords[1] -= 1
#         if direction == "e":
#             new_coords[0] += 1
#         if direction == "w":
#             new_coords[0] -= 1
#         return new_coords

#     def _checkCoordinates(self, coords, direction):
#         """
#         Check in the grid if an adjoining direction is unoccupied
#         """
#         return str(self._new_room_coords(coords, direction)) not in self.occupied


#     def generate_rooms(self, size_x, size_y, num_rooms):
#         '''
#         Fill up the grid, bottom to top, in a zig-zag pattern
#         '''

#         # Initialize the grid
#         self.grid = [None] * size_y
#         self.width = size_x
#         self.height = size_y
#         for i in range( len(self.grid) ):
#             self.grid[i] = [None] * size_x

#         # declare coordinates dictionary: key: coordinate tuple, value: room objects
#         current_coords = dict()
#         # declare rooms dictionary: key: room pk value, value: room objects
#         current_rooms = dict()

#         # Start from the coordinates for the center of map
#         x_coord = (self.width // 2)-1 
#         y_coord = (self.height // 2)-1
#         current_room_coords = (x_coord, y_coord)
#         current_room_count = 1

#         # add starting room to current_rooms and current_coords dictionaries
#         current_rooms[current_room_count] = Room(current_room_count, "The starting Room", "This is the starting room.", x_coord, y_coord)    
#         current_coords[ (x_coord,y_coord) ] = current_rooms[current_room_count]

#         # While there are rooms to be created...
#         while current_room_count < num_rooms:
            
#             avail_rooms = copy.deepcopy(current_rooms)
#             chosen_room = None
#             chosen_room_found = False
#             chosen_dir = ''
#             # choose from one of the rooms that had been created.  Find the available directions of the chosen room, put them in a list then shuffle it, and pick the first element of the shuffled list to determine the direction in which to add the room with. If no avilable direction in chosen room, look for another chosen room randomly
#             while chosen_room_found is False:
#                 chosen_room_id = randrange(0, len(avail_rooms))  
#                 avail_dirs = []
#                 if avail_rooms[chosen_room_id].n_to is None and self._checkCoordinates(coords, "n"):
#                 avail_dirs.append("n")
#                 if avail_rooms[chosen_room_id].s_to is None and self._checkCoordinates(coords, "s"):
#                     avail_dirs.append("s")
#                 if avail_rooms[chosen_room_id].w_to is None and self._checkCoordinates(coords, "w"):
#                     avail_dirs.append("w")
#                 if avail_rooms[chosen_room_id].e_to is None and self._checkCoordinates(coords, "e"):
#                     avail_dirs.append("e")
#                 random.shuffle(avail_dirs)
#                 if len(avail_dirs) > 0:
#                     chosen_dir = avail_dirs[0]
#                     if self._new_room_coords(current_room_coords, chosen_dir)
#                         chosen_room = avail_rooms[chosen_room_id]
#                         chosen_room_found = True
#                 del avail_rooms[chosen_room_id]

#             new_room = Room(current_room_count, "A Generic Room", "This is a generic room.", x_coord, y_coord)

#             current_room_count +=1

    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid) # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)


w = World()
# rm = Room(1, "The starting Room", "This is the starting room.", 2, 2)
# w.grid

num_rooms =100
width = 15
height = 15
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
