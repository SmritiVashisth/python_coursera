"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        index = 0
        while index < len(self._zombie_list):
            yield self._zombie_list[index]
            index = index + 1
        return

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)   
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        index = 0
        while index < len(self._human_list):
            yield self._human_list[index]
            index = index + 1
        return
        
    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        
        height = poc_grid.Grid.get_grid_height(self)
        width = poc_grid.Grid.get_grid_width(self)
        visited = poc_grid.Grid(height,width)
        visited.clear()
                
        distance_field=[]
        for _ in range(0,height):
            temp = []
            for _ in range(0,width):
                temp.append(height*width)
            distance_field.append(temp)
        
        boundary = poc_queue.Queue()
        
        if entity_type == ZOMBIE:
            for item in self._zombie_list:
                boundary.enqueue(item)
            
        elif entity_type == HUMAN:
            for item in self._human_list:
                boundary.enqueue(item)
                
                
        for cell in boundary:
            visited.set_full(cell[0],cell[1])
            distance_field[cell[0]][cell[1]] = 0
            while len(boundary) > 0:
                current_cell = boundary.dequeue()
                neighbours = poc_grid.Grid.four_neighbors(self,current_cell[0],current_cell[1])
                for neighbour_cell in neighbours:
                    if visited.is_empty(neighbour_cell[0],neighbour_cell[1]) and self.is_empty(neighbour_cell[0],neighbour_cell[1]):
                        visited.set_full(neighbour_cell[0],neighbour_cell[1])
                        boundary.enqueue(neighbour_cell)
                        distance_field[neighbour_cell[0]][neighbour_cell[1]] = min(distance_field[neighbour_cell[0]][neighbour_cell[1]],
                        distance_field[current_cell[0]][current_cell[1]]+1)
                
        
        return distance_field
                
        
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        temp = []
        for cell in self._human_list:
            neighbours = poc_grid.Grid.eight_neighbors(self,cell[0],cell[1])
            maxval = zombie_distance[cell[0]][cell[1]]
            maxpos = (cell[0],cell[1])
            for item in neighbours:
                if maxval < zombie_distance[item[0]][item[1]]:
                    maxval = zombie_distance[item[0]][item[1]]
                    maxpos = item
            temp.append(maxpos)
            
        self._human_list = temp
        
    
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        temp = []
        for cell in self._zombie_list:
            neighbours = poc_grid.Grid.four_neighbors(self,cell[0],cell[1])
            minval = human_distance[cell[0]][cell[1]]
            minpos = (cell[0],cell[1])
            for item in neighbours:
                if minval > human_distance[item[0]][item[1]]:
                    minval = human_distance[item[0]][item[1]]
                    minpos = item
            temp.append(minpos)
            
        self._zombie_list = temp

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Zombie(30, 40))
