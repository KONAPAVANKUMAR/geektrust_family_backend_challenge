from data import king

def getParents(name):
    node = king
    if node is None:
        return
    queue = []
    queue.append(node)
    while queue:
        node = queue.pop(0)
        if node.children:
            for child in node.children:
                if child.name == name:
                    if node.wife:
                        return [node,node.wife]
                    elif node.husband:
                        return [node.husband,node]
                    else:
                        return None
                queue.append(child)


def getSiblings(name):
    parents = getParents(name)
    if not parents:
        return None
    mother = None
    father = None
    for parent in parents:
        if parent.gender == "female":
            mother = parent
        else:
            father = parent
    
    if mother.children:
        return [child for child in mother.children if child.name != name]
    return [child for child in father.children if child.name != name]

def getFather(name):
    parents = getParents(name)
    father = None
    if parents:
        father = parents[0]
    return father

def getMother(name):
    parents = getParents(name)
    mother = None
    if parents:
        mother = parents[1]
    return mother

def getPaternalUncle(name):
    father = getFather(name)
    if not father:
        return None
    paternalFathers = []
    fatherSiblings = getSiblings(father.name)
    if not fatherSiblings:
        return None
    for sibling in fatherSiblings:
        if sibling.gender=="male":
            paternalFathers.append(sibling.name)
    return paternalFathers

def getMaternalUncle(name):
    mother = getMother(name)
    if not mother:
        return None
    paternalMothers = []
    motherSiblings = getSiblings(mother.name)
    if not motherSiblings:
        return None
    for sibling in motherSiblings:
        if sibling.gender=="male":
            paternalMothers.append(sibling.name)
    return paternalMothers

def getPaternalAunt(name):
    father = getFather(name)
    if not father:
        return None
    paternalFathers = []
    fatherSiblings = getSiblings(father.name)
    if not fatherSiblings:
        return None
    for sibling in fatherSiblings:
        if sibling.gender=="female":
            paternalFathers.append(sibling.name)
    return paternalFathers

def getMaternalAunt(name):
    mother = getMother(name)
    if not mother:
        return None
    paternalMothers = []
    motherSiblings = getSiblings(mother.name)
    if not motherSiblings:
        return None
    for sibling in motherSiblings:
        if sibling.gender=="female":
            paternalMothers.append(sibling.name)
    return paternalMothers

def getSpouse(name):
    node = king
    if node is None:
        return None
    queue = []
    queue.append(node)
    while queue:
        node = queue.pop(0)
        if node.name == name:
            if node.wife:
                return node.wife
            if node.husband:
                return node.husband
        if node.wife:
            if node.wife.name == name:
                return node
        if node.husband:
            if node.husband.name == name:
                return node
        
        if node.children:
            for child in node.children:
                queue.append(child)
    return None

def getSpouseSister(name):
    spouse = getSpouse(name)
    if not spouse:
        return None
    spouseSiblings = getSiblings(spouse.name)
    if not spouseSiblings:
        return None
    spouseSisters =  [sibling for sibling in spouseSiblings if sibling.gender == "female"]
    return spouseSisters

def getWifeOfSiblings(name):
    siblings = getSiblings(name)
    if not siblings:
        return None
    brothers = [sibling for sibling in siblings if sibling.gender == "male"]
    wifeOfSiblings = []
    for brother in brothers:
        brotherWife = getSpouse(brother.name)

        if brotherWife:
            wifeOfSiblings.append(brotherWife)
    return wifeOfSiblings

def getSisterInLaw(name):
    spouseSisters = getSpouseSister(name)
    wifeOfSiblings = getWifeOfSiblings(name)
    if not spouseSisters and not wifeOfSiblings:
        return None
    if not wifeOfSiblings:
        return spouseSisters
    if not spouseSisters:
        return wifeOfSiblings
    return spouseSisters + wifeOfSiblings


def getSpouseBrother(name):
    spouse = getSpouse(name)
    if not spouse:
        return None
    spouseSiblings = getSiblings(spouse.name)
    if not spouseSiblings:
        return None
    spouseBrothers =  [sibling for sibling in spouseSiblings if sibling.gender == "male"]
    return spouseBrothers

def getHusbandOfSiblings(name):
    siblings = getSiblings(name)
    if not siblings:
        return None
    sisters = [sibling for sibling in siblings if sibling.gender == "female"]
    husbandOfSiblings = []
    for sister in sisters:
        sisterHusband = getSpouse(sister.name)

        if sisterHusband:
            husbandOfSiblings.append(sisterHusband)
    return husbandOfSiblings

def getBrotherInLaw(name):
    spouseBrothers = getSpouseBrother(name)
    husbandOfSiblings = getHusbandOfSiblings(name)
    if not spouseBrothers and not husbandOfSiblings:
        return None
    if not husbandOfSiblings:
        return spouseBrothers
    if not spouseBrothers:
        return husbandOfSiblings
    return spouseBrothers + husbandOfSiblings

def getChildren(name):
    node = king
    if node is None:
        return
    queue = []
    queue.append(node)
    while queue:
        node = queue.pop(0)
        if node.name == name:
            return node.children
        spouse = getSpouse(node.name)
        if spouse:
            if spouse.name == name:
                return node.children
        if node.children:
            for child in node.children:
                queue.append(child)

def getSon(name):
    children = getChildren(name)
    if children:
        return [child for child in children if child.gender == "male"]

def getDaughter(name):
    children = getChildren(name)
    if children:
        return [child for child in children if child.gender == "female"]





        











