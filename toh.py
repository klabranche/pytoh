# https://code.visualstudio.com/docs/python/python-tutorial

def toh(steps,discCount, source_rod, destination_rod, placeholder_rod):           
    if discCount == 1:
        print("Move disc 1 from rod",source_rod,"to rod",destination_rod)
        steps.append((1,source_rod,destination_rod))
        return
    toh(steps,discCount-1, source_rod, placeholder_rod, destination_rod)
    print("Move disc",discCount,"from rod",source_rod,"to rod",destination_rod)
    steps.append((discCount,source_rod,destination_rod))
    toh(steps,discCount-1, placeholder_rod, destination_rod, source_rod)

def main():
    try:
        discCount = int(input("How many disks do you want to move?"))
    except ValueError:
        print()
        print("discCount is not a number... defaulting to 3")
        discCount=3

    print()
    print("Moving",discCount,"discs from rod A to rod C", end="\n\n")
    steps=[]
    toh(steps,discCount, 'A', 'C', 'B')
    print(steps)
