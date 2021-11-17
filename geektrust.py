from data import king
from algorithms import addChild, firstLetterToLower
from relations import *

import sys

file = open(sys.argv[1], "r")
lines = file.readlines()

for line in lines:
    line = line.strip()
    inputs = line.split(" ")
    if inputs[0] == "ADD_CHILD":
        print(addChild(inputs[1],inputs[2],firstLetterToLower(inputs[3])))
    elif inputs[0] == "GET_RELATIONSHIP":
        relationship = inputs[2]
        if relationship == "Paternal-Uncle":
            if not getPaternalUncle(inputs[1]):
                print("PERSON_NOT_FOUND")
                continue
            result = " ".join([child.name for child in getPaternalUncle(inputs[1])])
            if result:
                print(result)
            else:
                print("NONE")
        elif relationship == "Maternal-Uncle":
            if not getMaternalUncle(inputs[1]):
                print("PERSON_NOT_FOUND")
                continue
            result = " ".join([child for child in getMaternalUncle(inputs[1])])
            if result:
                print(result)
            else:
                print("NONE")
        elif relationship == "Paternal-Aunt":
            if not getPaternalAunt(inputs[1]):
                print("PERSON_NOT_FOUND")
                continue
            result = " ".join([child for child in getPaternalAunt(inputs[1])])
            if result:
                print(result)
            else:
                print("NONE")
        elif relationship == "Maternal-Aunt":
            if not getMaternalAunt(inputs[1]):
                print("PERSON_NOT_FOUND")
                continue
            result = " ".join([child for child in getMaternalAunt(inputs[1])])
            if result:
                print(result)
            else:
                print("NONE")
        elif relationship == "Siblings":
            result = " ".join([child.name for child in getSiblings(inputs[1])])
            if result:
                print(result)
            else:
                print("NONE")
        elif relationship == "Brother-In-Law":
            if not getBrotherInLaw(inputs[1]):
                print("PERSON_NOT_FOUND")
                continue
            result = " ".join([child.name for child in getBrotherInLaw(inputs[1])])
            if result:
                print(result)
            else:
                print("NONE")
        elif relationship == "Sister-In-Law":
            if not getSisterInLaw(inputs[1]):
                print("PERSON_NOT_FOUND")
                continue
            result = [child.name for child in getSisterInLaw(inputs[1])]
            if result:
                print(" ".join(result))
            else:
                print("NONE")
        elif relationship == "Son":
            if not getSon(inputs[1]):
                print("PERSON_NOT_FOUND")
                continue
            result = [child.name for child in getSon(inputs[1])]
            if result:
                print(" ".join(result))
            else:
                print("NONE")
        elif relationship == "Daughter":
            if not getDaughter(inputs[1]):
                print("PERSON_NOT_FOUND")
                continue
            result = [child.name for child in getDaughter(inputs[1])]
            if result:
                print(" ".join(result))
            else:
                print("NONE")