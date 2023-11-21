from node.node import *

class queue:
    """queue class that uses linked lists of nodes as its underlying data structure.
    """    
    def __init__(self):
        """Constructs an empty queue.
        """        
        self.__head = None          # reference to the front node in the queue
        self.__tail = self.__head   # reference to the rear node in the queue
        self.__manyNodes = 0        # keeps track of the number of nodes in the queue

    def size(self):
        """Returns the number of nodes in the calling queue.

        Returns:
            int: number of nodes
        """        
        return self.__manyNodes
    
    def getHead(self):
        """Returns a reference to the head (front) of the calling queue.

        Returns:
            node: reference to the head (front) of the calling queue
        """        
        return self.__head
    
    def getTail(self):
        """Returns a reference to the tail (rear) of the calling queue

        Returns:
            node: reference to the tail (rear) of the calling queue
        """        
        return self.__tail
    
    def getData(self):
        """Returns the data values in the calling queue

        Returns:
            str: data values in the calling queue 
        """        
        cursor = self.__head    # used to step through the nodes in the calling queue
        data = ""               # string representation of data values in the calling queue
        i = 1                   # used to count the nodes in the calling queues

        # loop through the calling queue, one node at a time, getting the data values
        # and concatenating them to data
        while(i <= self.__manyNodes):
            data = data + (str(cursor.getData()) + ' ')
            cursor = cursor.getLink()
            i += 1

        # return data 
        return data 
    
    def __str__(self):
        """Returns string representation of the calling queue

        Returns:
            str: string representation of the calling queue 
        """        
        return f"[ {self.getData()} ]"
    
    def enqueue(self, element):
        """Inserts (adds) the specified element to the front of the calling queue
 
        Args:
            element: specified element
        """        
        # if the calling queue is empty
        if (self.__head == None):
            # add node to calling queue
            self.__head = node(element, None)
            # make tail refer to the same node as head
            self.__tail = self.__head
        else:
            # add node to the front of the queue
            self.__tail.addNodeAfter(element)

            # advance to next node in tail
            self.__tail = self.__tail.getLink()

        # get the number of nodes in the callign queue 
        self.__manyNodes = node.listLength(self.__head)

    def isEmpty(self):
        """Checks if the calling queue is empty

        Returns:
            Boolena: True if the calling queue is empty, else False.
        """        
        return self.size() == 0
    
    def dequeue(self):
        """Removes and returns the element at the head (front) of the calling queue

        Raises:
            ValueError: indicates calling queue is empty

        Returns:
            _type_: element at the top of the calling queue
        """        
        try:
            # if the calling queue is empty, raise error
            if (self.isEmpty()):
                raise ValueError("queue is empty")
        except ValueError as e:
            # display value error and exit
            exit(e)
        else:
            # get data in node at the head (front) of the calling queue
            front = self.__head.getData()

            # advance head instance variable to next node
            self.__head = self.__head.getLink()

            # recompute the number of nodes in the calling queue
            self.__manyNodes = node.listLength(self.__head)

            # return data in node at the head (front) of the calling queue
            return front
        
    def peek(self):
        """Returnss the element at the head (front) of the calling queue, without removing it.

        Raises:
            ValueError: indicates calling queue is empty

        Returns:
            _type_: element at the top of the calling queue
        """        
        try:
            # if the calling queue is empty, raise error
            if (self.isEmpty()):
                raise ValueError("queue is empty")
        except ValueError as e:
            # display value error and exit
            exit(e)
        else:
            # return data in node at the head (top) of the calling queue
            return self.__head.getData()
        
    def __len__(self):
        """Return the size of the queue."""
        return self.__manyNodes
