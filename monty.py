from random import randint
from random import choice


N = 1000

def simulate(N):
    K = 0
    ###insert your code here###
    for i in range(N):
        doors = [1, 2, 3]
        realDoor = randint(1, 3)
#        print(realDoor)
        pickedDoor = randint(1, 3)
#        print(pickedDoor)

        doors.remove(pickedDoor)
        
        if (pickedDoor == realDoor):
            montyDoor = choice(doors)
            doors.remove(montyDoor)
            newPickDoor = doors[0]
        else:
            newPickDoor = realDoor

 #       print(newPickDoor)
        if (newPickDoor == realDoor):
            K += 1 
    
    return float(K) / float(N)

print(simulate(N))