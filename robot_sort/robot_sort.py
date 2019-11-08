class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None      # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1
        # Check if at end of array or not
        # False = at end of array

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0
        #Check if at beginning of array or not
        # False = at beginning of array

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False
        # If check passes, moves over 1

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False
        #If check passes, moves back 1

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item
        # Swap X for Y

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        
        If the held item's value is greater, return 1.
        
        If the held item's value is less, return -1.
        
        If the held item's value is equal, return 0.
        
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """

        self.swap_item()
        for i in range(len(l)):
            #print("position at *i* is: ", self._position)
            #print("Initially holding: ", self._item)
            for j in range(i+1, len(l)):
                if l[i] > l[j]:
                    
                    print("yes")
                    print(l[i]
        return l
"""" Pseudo-code:
        Selective Sort:
            Set initial value to first item in array
            Compare to next item in array - if item one index position up is greater, swap, if not, continue

        Bubble Sort:
            Move thru items in array and compare i to i+1.  If item is smaller, swap, if not, move on.
            
            The problem I keep running into and can't get around is two-fold:

            1) Someone had something specific in mind with this code, but never bothered to 
            write down what they were trying to get at, so I'm left to play psychic 
            mindreader detective for most of the sprint while time ticks away instead of coding

            2) The robot is already holding an item - "None" is not "nothing" - it's 
            something, essentially an item of infinitely small value.  Trying to order 
            a list from least to greatest will always leave "None" at the beginnging, 
            and the robot holding the greatest value.

    """"
            
            #self._item = i
            # 
            #     self.move_right()
            #     if self.compare_item() == 1:
            #         self.swap_item()
            #         print("state of array is: ", l)
               # print("held item is: ", self._item)
                #print("position -J- is: ", self._position)
                
                #print("looking at: ", l[j])
                #print("Hello")
                    #self.swap_item()
                #if l[j] < l[i]:
                    #self._item = j
                    #l[i], l[self._item] = l[self._item], l[i]


#   def sort(self):
#         """
#         Sort the robot's list.
#         """
#         for i in range(len(l)):
#             #min_index = i
#             self._item = i
#             for j in range(i+1, len(l)):
#                 #if self.compare_item() == -1:
#                     #self.swap_item()
#                 if l[j] < l[i]:
#                     self._item = j
#                     l[i], l[self._item] = l[self._item], l[i]
#         return l

    # for i in range(len(array)):
    #     min_index = i
    #     for j in range(i+1, len(array)):
    #         if array[j] < array[i]:
    #     array[i], array[self._item] = array[self._item], array[i]
    # return array

#  * You may use any pre-defined robot methods.
#   * You may NOT modify any pre-defined robot methods.
#   * You may use logical operators. (`if`, `and`, `or`, `not`, etc.)
#   * You may use comparison operators. (`>`, `>=`, `<`, `<=`, `==`, `is`, etc.)
#   * You may use iterators. (`while`, `for`, `break`, `continue`)

#   * You may NOT store any variables. (`=`)
#   * You may NOT access any instance variables directly. (`self._anything`)
#   * You may NOT use any Python libraries or class methods. (`sorted()`, etc.)
#   * You may define robot helper methods, as long as they follow all the rules.



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`
    l = [5, 4, 3, 2, 1]
    #l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)