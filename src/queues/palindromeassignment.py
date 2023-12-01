from queues.queue import *
from stack.stack import *

class palindromeassignment:
    @staticmethod
    def isPalindrome(expression: str):

        a1 = queue()    # reads the expression forward
        a2 = stack()    # reads the expression backward
        a3 = queue()    # stores the expression processed so far
        a4 = ""         # stores the expression whether the expression is a palindrome or not

        for words in expression:
            if words.isalpha():  
                upper_word = words.upper()
                a1.enqueue(upper_word)
                a2.push(upper_word)
                a3.enqueue(words)

        while not a1.isEmpty():
            next_char = a1.dequeue()
            a4 += a3.dequeue()  
            if next_char != a2.pop():
                return False, a4    
        
        return True, a4


