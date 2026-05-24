import random

def checksorted (list):

    length = len(list)

    if length == 0 or length == 1:
        return True
    
    return list[0] <= list[1] and checksorted(list[1:])
def arraysum (list):

    length = len(list)
    if length == 0:
        return 0
    return list[0] + arraysum(list[1:])

def maxelement (list):
    length = len(list)
    if length == 0:
        return None
    if length == 1:
        return list[0]
    max_of_rest = maxelement(list[1:])
    return max(list[0], max_of_rest)


listnum = random.randint(1, 10)
list = [random.randint(1, 100) for i in range(listnum)]
randomchance = random.random()
if randomchance < 0.5:
    list.sort()
else:
    random.shuffle(list)
print ("The list is:", list)
print ("The maximum element in the list is:", maxelement(list))
print("The sum of the list is:", arraysum(list))

if checksorted(list):
    print("The list is sorted.")
else:
    print("The list is not sorted.")



