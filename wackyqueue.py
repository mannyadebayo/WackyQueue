"""
# Copyright Nick Cheng, Emmanuel Adebayo 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from wackynode import WackyNode

# Do not add import statements or change the one above.
# Write your WackyQueue class code below.


# Create a function that helps you to flip lists backwards
def flip(head):
    '''(WackyNode) -> WackyNode
    This function given a head of a 'Linked list' it flips the list
    backwards, making the last item the top and the top item the last item
    and returns the pointer to the head back
    '''
    # First you want to keep a constant Node as you mutate the Linked list
    # You want to do this because you want to make sure that the pointer to the
    # dummy node points to the new top item
    constant = head.get_next()
    if constant is not None:
        current_node = constant.get_next()
    if current_node is not None:
        next_current_node = current_node.get_next()
    last_node = constant
    # Now you want to loop until you reach the end of the list
    while current_node is not None:
        # You want to re-arrange the list as you go through the list
        # whilst keeping the same constant
        constant.set_next(next_current_node)
        current_node.set_next(constant)
        # Make head point to the current node
        head.set_next(current_node)
        # Then make current point to the last node
        current_node.set_next(last_node)
        # Now update the current node and the last node
        last_node = current_node
        current_node = constant.get_next()
        if current_node is not None:
            next_current_node = current_node.get_next()
    return head


class WackyQueue():
    '''This class represents a WackyQueue
    A WackyQUeue is queue that operates with WackyNodes
    It stores its data in two linked lists. Every odd object
    is in a list. And the other holds every even object
    '''
    def __init__(self):
        '''(WackyQueue) -> None
        This method instanciates a WackyQueue
        '''
        # Representation Invariant
        # _size is how many objects the Queue contains
        # _head is the head of the one of the WackyQueues
        # _head2 is the second head of the WackyWueues
        # The hgher the number, the greater its priority
        # Which ever head holds 0 as its priority is the head of the odd
        # list
        # if self._head.get_priority is 0, it is the head of the odd list
        # if self._head2.get_priority is 0, it is the head of the odd list
        # END OF REPRESENTATION INVARIANT
        # Now cretaed the WackyHeads holding no information and
        # pointing to nothing
        # Make self._head's priotiry 0 by defualt to be the head of the odd
        # list, you will see why later.
        self._head = WackyNode(None, 0)
        self._head2 = WackyNode(None, 1)

    def insert(self, obj, pri):
        '''(WackyQueue, object, int) -> None
        This method puts an object in the Wacky Queue depending on its
        priority
        '''
        # Create the new node
        new_node = WackyNode(obj, pri)
        # First you want to find the spot where the new node will go. 'in-head'
        # means the operation is currently in self._head and is loking for
        # where to insert the item
        # We also want to start comparing items from the top of the list
        if self._head.get_priority() is 0:
            current_check = 'in-head'
            current_node = self._head.get_next()
        elif self._head2.get_priority() is 0:
            current_check = 'in-head2'
            current_node = self._head2.get_next()
        # Next you want to make sure that the current node is not None
        if current_node is not None:
            current_pri = current_node.get_priority()
        # You want to keep track of what node was visited last in each list
        last_head_node = self._head
        last_head2_node = self._head2
        # Loop through BOTH lists, by alternating until you find the spot
        while (current_node is not None) and (pri <= current_pri):
            # create a condition that does alternate checking
            if current_check == 'in-head':
                # Keep track of both current and LAST Nodes
                last_head_node = current_node
                current_node = last_head2_node.get_next()
                # Next you want to make sure that the current node is not None
                if current_node is not None:
                    current_pri = current_node.get_priority()
                # Now to alternate make the current check to point to head2
                current_check = 'in-head2'
            elif current_check == 'in-head2':
                # Keep track of both current and LAST Nodes
                last_head2_node = current_node
                current_node = last_head_node.get_next()
                if current_node is not None:
                    current_pri = current_node.get_priority()
                # Now to alternate make the current check to point to head2
                current_check = 'in-head'
        # When the spot is found, depending on the obj of the head, that is
        # where you inserting it
        # Do not forget to push all the other items down the list
        # If the current_check is 'in-head', then you want to PUT the new node
        # in head
        if current_check == 'in-head':
            # Get the next node of the last node you visited in head2
            # Make the new node point to that
            new_node.set_next(last_head2_node.get_next())
            # Make the last node you visited in head2 point to the current node
            last_head2_node.set_next(current_node)
            # Make the last node you visited in head point to the new node
            last_head_node.set_next(new_node)
        # If the current_check is 'in-head2', then you want to PUT the new node
        # in head2
        elif current_check == 'in-head2':
            # Then get the next node of the last node you visited in head
            # Point the new node to the next node of the last node you visited
            # in head
            new_node.set_next(last_head_node.get_next())
            # Now point the last node you visited in head and point it to the
            # current node
            last_head_node.set_next(current_node)
            # Also, get the last node you visited before the current node,
            # then point that node to the new node.
            last_head2_node.set_next(new_node)

    def extracthigh(self):
        '''(WackyQueue) -> object
        This method removes and returns the first item in the WackyQueue.
        The object with the largest priority and inputed first amognst its
        equal priority is removed first
        REQ: The Queue is not empty
        '''
        # You want to extract from the top of the head that has the highest
        # priority in the queue
        if self._head.get_priority() is 0:
            top_item = self._head.get_next()
            new_top_item = top_item.get_next()
            # Now make head point to the new top item
            self._head.set_next(new_top_item)
            # Remember to change the priority of the head, because the new top
            # item is now in the other head
            self._head.set_priority(1)
            self._head2.set_priority(0)
        elif self._head2.get_priority() is 0:
            top_item = self._head2.get_next()
            new_top_item = top_item.get_next()
            # Now make head2 point to the new top item
            self._head2.set_next(new_top_item)
            # Now remember to change the priority of both heads
            self._head.set_priority(0)
            self._head2.set_priority(1)
        return top_item.get_item()

    def is_empty(self):
        '''(WackyQueue) -> bool
        This method returns True if the WackyQueue is empty and False if it is
        not
        '''
        # This part is simple, just get the next item to the dummy node
        # and check if it is None or a Node
        check_odd = self._head.get_next()
        check_even = self._head2.get_next()
        return check_odd is check_even is None

    def changepriority(self, obj, pri):
        '''(WackyQueue) -> None
        This method finds the first object of this priority and changes it to
        the priority that is given. Nothing is done if the object is not found
        '''
        # Now you want to find the first apperance of that object
        # start with the top of the list
        if self._head.get_priority() is 0:
            current_check = 'in-head'
            current_node = self._head.get_next()
        elif self._head2.get_priority() is 0:
            current_check = 'in-head2'
            current_node = self._head2.get_next()
        current_item = current_node.get_item()
        last_head_node = self._head
        last_head2_node = self._head2
        # Now you want to loop until you have found the object you are looking
        # for
        while (current_item is not obj) and (current_node is not None):
            # Again just like in insert, you want to start with the top of the
            # Queue
            if current_check == 'in-head':
                last_head_node = current_node
                current_node = last_head2_node.get_next()
                if current_node is not None:
                    current_item = current_node.get_item()
                current_check = 'in-head2'
            elif current_check == 'in-head2':
                last_head2_node = current_node
                current_node = last_head_node.get_next()
                if current_node is not None:
                    current_item = current_node.get_item()
                current_check = 'in-head'
        # Check if the current node is None first
        if ((current_node is not None) and
           (current_node.get_priority is not pri)):
            # After you have found the node that contains the object you need
            # to re-arrange the list
            if current_check == 'in-head':
                # So first if you left off at head, that is where you are
                # removing the node from
                # Get the previous head item you visited and point it to the
                # next item of the last head2 item you visited
                last_head_node.set_next(last_head2_node.get_next())
                # Now get the previous head2 item you visited and point it to
                # the next node of the current node
                last_head2_node.set_next(current_node.get_next())
                self.insert(obj, pri)
            # If you left off at head2, this is where you are removing the
            # item from
            elif current_check == 'in-head2':
                # get the previos head2 node and point it to the next item of
                # the previous head node you visited
                last_head2_node.set_next(last_head_node.get_next())
                # Then get the previous head node you visited to point it the
                # next item of the current node
                last_head_node.set_next(current_node.get_next())
                # Now you need to put back the new node into the list
                # use the insert method
                self.insert(obj, pri)

    def negate_all(self):
        '''(WackyQueue) -> None
        This method reveres the entry time of all the objects
        '''
        # Since your methods should be independent of the items in the list
        # when retrieving them, You want to 'just' flip both the odd and even
        # lists, luckily you have a helper function for this
        self._head = flip(self._head)
        self._head2 = flip(self._head2)
        # Now to get to the purpose of the function you have to negate all
        # the priorities in the Queue
        current_node = self._head.get_next()
        while current_node is not None:
            pri = current_node.get_priority()
            pri = pri * -1
            current_node.set_priority(pri)
            if current_node is not None:
                current_node = current_node.get_next()
        # Repeat the same steps for head2
        current_node = self._head2.get_next()
        while current_node is not None:
            pri = current_node.get_priority()
            pri = pri * -1
            current_node.set_priority(pri)
            if current_node is not None:
                current_node = current_node.get_next()
        # For the final step, since you do not remember what the last object
        # in the queue is. You need to check for the highest
        if (self._head.get_next() and self._head2.get_next() is not None):
            head_top_pri = self._head.get_next().get_priority()
            head2_top_pri = self._head2.get_next().get_priority()
            # Now you need see if you need a new top Node
            if head_top_pri > head2_top_pri:
                self._head.set_priority(0)
                self._head2.set_priority(1)
            elif head2_top_pri > head_top_pri:
                self._head2.set_priority(0)
                self._head.set_priority(1)

    def getoddlist(self):
        '''(WackyQueue) -> WackyNode
        This function returns a node that points to all the odd items in the
        queue
        '''
        # You know the first item on the list is the list is the one that has
        # priority 0
        if self._head.get_priority() is 0:
            odd_list = self._head.get_next()
        elif self._head2.get_priority() is 0:
            odd_list = self._head2.get_next()
        return odd_list

    def getevenlist(self):
        '''(WackyQueue) -> WackyNode
        This function returns a node that points to all the even items in the
        list
        '''
        # You know that which ever head whose priority is 1 has all the even
        # items
        if self._head.get_priority() is 1:
            even_list = self._head.get_next()
        elif self._head2.get_priority() is 1:
            even_list = self._head2.get_next()
        return even_list

    def __str__(self):
        '''(WackyQueue) -> str
        This method prints the contents of the WackyQueue
        '''
        current_node = self._head.get_next()
        current_node2 = self._head2.get_next()
        head_str = ''
        head2_str = ''
        top_head_str = ''
        top_head2_str = ''
        while current_node is not None:
            current_obj = current_node.get_item()
            head_str = head_str + str(current_obj) + ', '
            current_node = current_node.get_next()
        while current_node2 is not None:
            current_obj2 = current_node2.get_item()
            head2_str = head2_str + str(current_obj2) + ', '
            current_node2 = current_node2.get_next()
        # Check which head has the higher priority
        if self._head.get_priority() is 0:
            top_head_str = 'ODD-LIST -> '
            top_head2_str = 'EVEN-LIST -> '
        elif self._head2.get_priority() is 0:
            top_head2_str = 'ODD-LIST -> '
            top_head_str = 'EVEN-LIST -> '
        #return (top_head_str + head_str[:-2] + ', ' + top_head2_str +)
