peopleList = input("Введите через пробел имена лайкнувших:\n").split(" ")

pC = len(peopleList)
pOC = pC - 2
if pC == 0:
    print("no one likes this")
elif pC == 1:
    print(peopleList[0], "likes this")
elif pC == 2:
    print(f"{peopleList[0]} and {peopleList[1]} like this")
elif pC > 2:
    print(f"{peopleList[0]}, {peopleList[1]} and {pOC} more like this")