from queues.queue import *
from stack.stack import *

class palindrome:
    @staticmethod 
    def isPalindrome(expression:str):
        

        a1 = queue()
        a2 = queue() 
    
        mismatches = 0
        expression = expression.upper()

        for e in expression:
                
                if e.isalpha():
                    a1.enqueue(e)
        
        for e in reversed(expression):

            if e.isalpha():
                a2.enqueue(e)

        while(not a1.isEmpty()):

            if (a1.dequeue() != a2.dequeue()):
                mismatches += 1

        return (mismatches == 0)