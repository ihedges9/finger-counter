import pandas as pd

def countPositionDict(count = 5, fingers = 5, cycles = 5):
    """
    Function for finding position of a number in a snake count using fingers/positions. 
    Utilizes a dictionary for position and number tracking.
    
    :param count: The number to be counted to.
    :param fingers: The number of positions used for counting.
    :param cycles: The number of times to count `count` on `fingers`
    """
    hand = {}
    countRange = tuple(range(0, count))
    for i in range(0, fingers):
        hand.update({f"finger{i}": None})
    
    cycleCounter = 0
    for i in range(0, cycles):
        while cycleCounter <= cycles-1:
            if cycleCounter == 0:
                print('First Iteration')
                cycleCounter += 1
                for j in countRange:
                    hand.update({f"finger{j}": j})
                    
            else:
                cycleCounter += 1
                print("Test Progression")
                if None in hand.values():
                    print('Start count again')
                    emptyPositions = [key for key, value in hand.items() if value == None]
                    print(emptyPositions[0])
                for j in countRange:
                    'Placeholder'
                    
            
    
    return hand

def countPositionListTuple(count = 5, fingers = 5, cycles = 5):
    """
    Function for finding position of a number in a snake count using fingers/positions. 
    Utilizes lists and tuples for position and number tracking.
    
    :param count: The number to be counted to.
    :param fingers: The number of positions used for counting.
    :param cycles: The number of times to count `count` on `fingers`
    """

print(countPositionDict(5, 7, 6))