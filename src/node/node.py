class node:
    """The node class holds a collection of values using nodes. It includes
    methods that allow the nodes to be manipulated and modified.
    """
    def __init__(self, data, link):
        """Constructs a node using the specified data value and link.

        :ivar __data: data value of node
        :ivar __link: link portion of node

        Args:
            data: specified data value
            link: specified link
        """        
        self.__data = data
        self.__link = link

    def getData(self):
        """Returns the data value stored in the calling node.

        Returns:
            _type_: data value stored in the calling node.
        """        
        return self.__data
    
    def setData(self, data):
        """Sets the data value stored in the calling node to the 
        specified data value.

        Args:
            data (_type_): specified data value
        """        
        self.__data = data

    def getLink(self):
        """Returns the link stored in the calling node.

        Returns:
            node: link storedn in the calling node
        """        
        return self.__link
    
    def setLink(self, link):
        """Sets the link stored in the calling node to the specified link.

        Args:
            link (node): specified link
        """        
        self.__link = link 

    def addNodeAfter(self, element):
        """Adds a new node containing a specified element value 
        at a selected position in the calling node.

        Args:
            element (_type_): specified element value
        """        
        self.__link = node(element, self.__link)

    def removeNodeAfter(self):
        """Removes a node from a selected position in the calling node.
        """        
        self.__link = self.__link.__link

    @staticmethod 
    def listLength(head):
        """Computes and returns the number of nodes in a specified node.

        Args:
            head (head): specified node

        Returns:
            int: number of nodes
        """  
        cursor = head # cursor used to step through the specified node
        length = 0 # used to count the nodes

        # step through the nodes in the specified node as long as the 
        # cursor isn't None
        while (cursor != None):
            # increment length
            length += 1
    
            # move cursor to next node 
            cursor = cursor.getLink()

        # return length
        return length
    
    @staticmethod
    def listSearch(head, target):
        """Search for a specified target in a specified node. 

        Args:
            head (node): specified node
            target: specified target

        Returns:
            node: reference to node that contains specified target value
            if specified target value is found, else None
        """        
        cursor = head # cursor used to step through the specified node

        # step through the nodes in the specified node as long as the 
        # cursor isn't None
        while (cursor != None):
            # check if the data value in the node cursor refers to is equal
            # to the target
            if (cursor.getData() == target):
                # return cursor
                return cursor
    
            # move cursor to next node 
            cursor = cursor.getLink()

        # return None
        return None
    
    @staticmethod
    def listPosition(head, position: int):
        """Searches for a node in a specified node based on a specified position.

        Args:
            head (node): specified node
            position (int): specified position

        Raise:
            ValueError: indicates position is less than to one

        Returns:
            node: reference to node at specified position if specified position
            is found, else None
        """        