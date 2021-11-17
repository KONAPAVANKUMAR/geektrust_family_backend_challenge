from data import king
from models import Person

def addChild(motherName,childName,gender):
    node = king
    if node is None:
        return
    queue = [node]
    while queue:
        node = queue.pop(0)
        if node.gender == "female" and node.name == motherName:
            if node.husband:
                node.children.append(Person(name=childName,gender = gender))
                return "CHILD_ADDITION_SUCCEEDED"
            else:
                return "CHILD_ADDITION_FAILED"
        if node.gender == "male" and node.wife:
            if node.wife.name == motherName:
                node.children.append(Person(name=childName,gender = gender))
                return "CHILD_ADDITION_SUCCEEDED"
        if node.gender == "male" and node.name == motherName:
            return "CHILD_ADDITION_FAILED"


        if node.children:
            for child in node.children:
                queue.append(child)
    return "PERSON_NOT_FOUND"

def firstLetterToLower(string):
    return string[0].lower() + string[1:]
    


