from node.node import*
from stack.stack import*

def insertionsort(data: stack, first: int):

    # I created temporary stacks
    tempStack = stack()
    bypassStack = stack()

    # It bypasses the first 'first - 1' elements
    for i in range(first - 1):
        if not data.isEmpty():
            bypassStack.push(data.pop())

    # I sorted the remaining elements
    while not data.isEmpty():
        temp = data.pop()
        while not tempStack.isEmpty() and tempStack.peek() > temp:
            data.push(tempStack.pop())
        tempStack.push(temp)

    # I put the sorted elements back
    while not tempStack.isEmpty():
        data.push(tempStack.pop())

    # i put the bypassed elements back on top
    while not bypassStack.isEmpty():
        data.push(bypassStack.pop())

