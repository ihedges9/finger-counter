import pandas as pd


def countPosition(count = 5, fingers = 5, cycles = 5):
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



print(countPosition(5, 7, 6))