class loops:
    @staticmethod
    def evens (start: int, end: int):
        """Finds and displays the even numbers between a specified
        starting and ending value.
        
        Args:
            start (int): specified starting value
            end (int): specified ending value
        """

        if (start <= end):
            if (start % 2 == 0):
                print(start, end=" ")
            
            loops.evens(start + 1, end)