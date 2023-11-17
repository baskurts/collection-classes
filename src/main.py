from node.node import * 
from stack.stack import *
from stack.balancedparens import *
from stack.calculator import *
from stack.serialsearch import*
from stack.insertionsort import *

def main():
    # testInit()
    # testGettersandSetters()
    # testAddNodeAfter()
    # testRemoveNodeAfter()
    # review()
    # testListLength()
    # testListSearch()
    # testListPosition()
    # testListCopy()
    # testListCopyWithTail()
    # testPush()
    # testPop()
    # testIsEmpty()
    # testPeek()
    # print("Parenthesis are balanced?", balancedparens.isBalanced("{X+Y"))   # False
    # print("Parenthesis are balanced?", balancedparens.isBalanced("{X+Y)"))   # False 
    # print("Parenthesis are balanced?", balancedparens.isBalanced("({X+Y}*Z)"))   # True
    # print("Parenthesis are balanced?", balancedparens.isBalanced("[A+B]*({X+Y}*Z)"))    # True
    # print("(((6+9)/3)*(6-4)) = ", calculator.evaluate("(((6+9)/3)*(6-4))"))
    # print("(6+(3*(6-4))) = ", calculator.evaluate("(6+(3*(6-4)))"))
    # print("((5+2)-(3*(6/9))) = ", calculator.evaluate("((5+2)-(3*(6/9)))"))
    # print("((5*2)-(3*(6/2))) = ", calculator.evaluate("((5*2)-(3*(6/2)))"))
    testInsertionSort(1)
    testInsertionSort(4)
    testInsertionSort(6)
    

def testInsertionSort(first):
    # create an empty stack
    stack_to_sort = stack()

    # push elements onto the top of the stack
    stack_to_sort.push(-7)
    stack_to_sort.push(42)
    stack_to_sort.push(70)
    stack_to_sort.push(39)
    stack_to_sort.push(3)
    stack_to_sort.push(63)
    stack_to_sort.push(8)

    # print unsorted stack
    print(f"Unsorted stack: {stack_to_sort}")

    # call insertion sort method
    insertionsort(stack_to_sort, first)

    # print sorted stack
    print(f"Sorted stack: {stack_to_sort}")
    print()

# Test with different values of 'first'
for first in [1, 4, 6]:
    print(f"Output when first={first}")
    testInsertionSort(first)


def testPeek():
    print("Testing Peek method in stack class")

    s = stack()
    print("Stack size is:", s.size())               # 0
    print("Stack contains:", s)                     # []
    s.push('S')
    print("Stack size is:", s.size())               # 1
    print("Stack contains:", s)                     # [S]
    print("Top element in stack is:", s.peek())     # S
    # s.push('B')
    s.push(1)
    print("Stack size is:", s.size())               # 2
    print("Stack contains:", s)                     # [B S]
    print("Top element in stack is:", s.peek())     # B
    # s.push('O')
    s.push((1,2))
    print("Stack size is:", s.size())               # 3
    print("Stack contains:", s)                     # [O B S]
    print("Top element in stack is:", s.peek())     # O         
    # s.push('J')
    s.push([1,2,3])
    print("Stack size is:", s.size())               # 4
    print("Stack contains:", s)                     # [J O B S]
    print("Top element in stack is:", s.peek())     # J

def testIsEmpty():
    print("Testing Is Empty method in stack class")

    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size is:", s.size()) # 4
    print("Stack contains:", s)       # [J O B S]

    while(not s.isEmpty()):
        print("Just popped:", s.pop())

    print("Stack size is:", s.size()) # 0
    print("Stack contains:", s)       # []

def testPop():
    print("Testing Pop method in stack class")
    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size is:", s.size()) # 4
    print("Stack contains:", s)       # [J O B S]
    print("Just popped:", s.pop())    # J

    print("Stack size is:", s.size()) # 3
    print("Stack contains:", s)       # [O B S]
    print("Just popped:", s.pop())    # O

    print("Stack size is:", s.size()) # 2
    print("Stack contains:", s)       # [B S]
    print("Just popped:", s.pop())    # B

    print("Stack size is:", s.size()) # 1
    print("Stack contains:", s)       # [S]
    print("Just popped:", s.pop())    # S

    print("Just popped:", s.pop())

def testPush():
    print("Testing Push method in stack class")

    s = stack()
    print("Stack size is:", s.size()) # 0
    print("Stack contains:", s)       # []

    s.push('S')
    print(" Stack size is:", s.size()) # 1
    print("Stack contains:", s)        # [S]

    # s.push = stack('B')
    s.push(1)
    print(" Stack size is:", s.size()) # 2
    print("Stack contains:", s)        # [B S]

    # s.push = stack('O')
    s.push((1,2))
    print(" Stack size is:", s.size()) # 3
    print("Stack contains:", s)        # [O B S]

    s.push('J')
    s.push([1,2,3])
    print(" Stack size is:", s.size()) # 4
    print("Stack contains:", s)        # [J O B S]

def testListCopyWithTail():
    print("Testing List Copy With Tail")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to source
    source = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to source 
    source = node('B', source) # B -> S

    # construct a node with data equal to 0 and link equal to head
    # and assign its reference to source
    source = node('O', source) # O -> B -> S

    # construct a node with data equal to S and link equal to head 
    # and assign its reference to source
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopyWithTail(source) # J -> O -> B -> S, but at a different memory location
    # [J -> O -> B -> S, S]

    print("Source contains", node.listPosition(source, 1).getData(),
          node.listPosition(source, 2).getData(),
          node.listPosition(source, 3).getData(),
          node.listPosition(source, 4).getData())
    
    print("Copy head contains", node.listPosition(copy[0], 1).getData(),
          node.listPosition(copy[0], 2).getData(),
          node.listPosition(copy[0], 3).getData(),
          node.listPosition(copy[0], 4).getData())
    
    print("Copy tail contains", node.listPosition(copy[1], 1).getData())

def testListCopy():
    print("Testing List Copy")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to source
    source = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to source 
    source = node('B', source) # B -> S

    # construct a node with data equal to 0 and link equal to head
    # and assign its reference to source
    source = node('O', source) # O -> B -> S

    # construct a node with data equal to S and link equal to head 
    # and assign its reference to source
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopy(source) # J -> O -> B -> S, but at a different memory location

    print("Source contains", node.listPosition(source, 1).getData(),
          node.listPosition(source, 2).getData(),
          node.listPosition(source, 3).getData(),
          node.listPosition(source, 4).getData())
    
    print("Copy contains", node.listPosition(copy, 1).getData(),
          node.listPosition(copy, 2).getData(),
          node.listPosition(copy, 3).getData(),
          node.listPosition(copy, 4).getData())


def testListPosition():
    print("Testing List Position")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to head
    head = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to head 
    head = node('B', head) # B -> S

    # construct a node with data equal to 0 and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # construct a node with data equal to S and link equal to head 
    # and assign its reference to head
    head = node('J', head) # J -> O -> B -> S

    print("First node contains data:", node.listPosition(head, 1).getData()) # J -> O -> B -> S
    print("Second node contains data:", node.listPosition(head, 2).getData()) # O -> B -> S
    print("Third node contains data:", node.listPosition(head, 3).getData()) # B -> S
    print("Fourth node contains data:", node.listPosition(head, 4).getData()) # S

    if (node.listPosition(head, 5) != None):
        print("Fourth node contains data:", node.listPosition(head, 4).getData())
    else:
        print("There is no fifth node")

def testListSearch():
    print("Testing List Search")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to head
    head = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to head 
    head = node('B', head) # B -> S

    # construct a node with data equal to 0 and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # construct a node with data equal to S and link equal to head 
    # and assign its reference to head
    head = node('J', head) # J -> O -> B -> S

    print("Head contains", node.listSearch(head, 'J').getData())
    print("Head contains", node.listSearch(head, 'O').getData())
    print("Head contains", node.listSearch(head, 'B').getData())
    print("Head contains", node.listSearch(head, 'S').getData())

    if (node.listSearch(head, 'Z') != None):
        print("Head contains", node.listSearch(head, 'Z').getData())
    else:
        print("Head doesn't contain Z.")

def testListLength():
    print("Testing The Length")

     # construct a node with data equal to S and link equal to None
    # and assign its reference to head
    head = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to head 
    head = node('B', head) # B -> S

    # construct a node with data equal to 0 and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # construct a node with data equal to S and link equal to head 
    # and assign its reference to head
    head = node('J', head) # J -> O -> B -> S
    
    print("Length of head s:", node.listLength(head))

def review():
    print("Review")

    # Question 1
    head = node('X', None)
    head = node('X', head)
    head = node('X', head)
    head = node('X', head)

    # Question 2 
    selection1 = head

    # Question3
    selection1.addNodeAfter('O')

    # Question 4
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    # Question 5
    selection1.addNodeAfter('O')

    # Question 6
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    # Question 7
    selection1.addNodeAfter('O')

    # Question 8
    tail = head

    # Question 9
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    # Question 10
    selection2 = head

    # Question 11
    selection2 = selection2.getLink()
    selection2 = selection2.getLink()

    # Question 12
    head.setData('A')
    selection2.setData('A')
    selection1.setData('A')
    tail.setData('A')

    # Question 13
    head.removeNodeAfter()
    selection1.removeNodeAfter()
    selection2.removeNodeAfter()

def testRemoveNodeAfter():
    print("Testing Remove Node After")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to head
    head = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to head 
    head = node('B', head) # B -> S

    # construct a node with data equal to 0 and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # construct a node with data equal to S and link equal to head 
    # and assign its reference to head
    head = node('J', head) # J -> O -> B -> S

    print("The head node contains data: ", head.getData())

    # remove the node after the node head refers to (node that has data equal to 0)
    head.removeNodeAfter() # J -> B -> S

    head = head.getLink() # B -> S

    print("The head node contains data: ", head.getData())

    # remove the node after the node head refers to (node that has data equal to S)
    head.removeNodeAfter() # B

    print("The head node contains data: ", head.getData())

    """ # remove the node after the node head refers to (node that has data equal to S)
    head.removeNodeAfter() # this line of code will generate an AttributeError"""

def testAddNodeAfter():
    print("Testing Getters and Setters")

    # construct a node with data equal to J and link equal to None
    # and assign its reference to head
    head = node('J', None) # J

    print("The head node contains data:", head.getData())

    # declare a new node named selection and make it refer 
    # to the same node as head
    selection = head 

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # add a node with data equal to O after the node selection
    # refers to 
    selection.addNodeAfter('O') # J -> O

    # get selection's link and assign its reference back to 
    # selection
    selection = selection.getLink() # O

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # add a node with data equal to B after the node selection
    # refers to 
    selection.addNodeAfter('B') # O -> B

    # get selection's link and assign its reference back to 
    # selection
    selection = selection.getLink() # B

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # add a node with data equal to B after the node selection
    # refers to 
    selection.addNodeAfter('S') # B -> S

    # get selection's link and assign its reference back to 
    # selection
    selection = selection.getLink() # S

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # declare a new node named tail and make it refer to the same
    # node as head
    tail =  head

    # get tail's link and assign its reference to tail
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    # add a new node with data equal to Z after the node tail
    # refers to
    tail.addNodeAfter('Z')

    # get tail's link and assign its reference to tail
    tail = tail.getLink()

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())
    print("The tail node contains data:", selection.getData())

def testGettersandSetters():
    print("Testing Getters and Setters")

    # construct a node with data equal to R and link equal to None
    # and assign its reference to head
    head = node('R', None) # R

    print("The head node contains data:", head.getData())

    head.setData('S') # S
    print("The head node contains data:", head.getData())

    head = node('B', head) # B -> S
    print("The head node contains data:", head.getData())

    head = node('O', head) # O -> B -> S
    print("The head node contains data:", head.getData())

    head = node('J', head) # J -> O -> B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    head = head.getLink() # O -> B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    head = head.getLink() # B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    head = head.getLink() # S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    """ head = head.getLink() # None
    print("The head node contains data:", head.getData()) """

    print("The head node contains link:", head.getLink())

    # set head's link to a new node
    head.setLink(node('O', None)) # S -> O

def testInit():
    print("Testing Node Init")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to head
    head = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to head 
    head = node('B', head) # B -> S

    # construct a node with data equal to 0 and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # construct a node with data equal to S and link equal to head 
    # and assign its reference to head
    head = node('J', head) # J -> O -> B -> S

    head = node(1, head) # 1 -> J -> O -> B -> S
    head = node(1.5, head) # 1.5 -> 1 -> J -> O -> B -> S
    head = node([1,2], head) # [1,2] -> 1.5 -> 1 -> J -> O -> B -> S
    head = node(('A','B'), head) # ('A', 'B') -> [1,2] -> 1.5 -> 1 -> J -> O -> B -> S

    print()

if __name__ == "__main__": 
    main()