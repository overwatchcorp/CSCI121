def cheapest(numBoxes):
    aliceCap = 11
    bobCap = 14
    divAlice = numBoxes // aliceCap 
    divBob = numBoxes // bobCap 
    modAlice = numBoxes % aliceCap
    modBob = numBoxes % bobCap
    
    aliceTrips = divAlice
    if modAlice > 0:
        aliceTrips += 1
    bobTrips = divBob
    if modBob > 0:
        bobTrips += 1

    aliceCost = aliceTrips * 200
    bobCost = bobTrips * 250

    if aliceCost < bobCost:
        return 'Alice'
    return 'Bob'
