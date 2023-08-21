class Predicate:
    def __init__(self, ident, nm, deg):
        self.id = ident # identifier of the predicate
        self.name = nm  # Name of the predicate
        self.degree = deg  # RENAME IT to (degree)
        #self.predicateTerms = [] #
        self.rules = None   # To add a rule to the list that uses the predicate

    def getPredicateID(self):
        return self.id

    def getPredicateName(self):
        return self.name
    # should be getPredicateDegree
    def getPredicateDegree(self):
        return self.degree
    
    def getPredicateRules(self):
        return self.rules

    #def setPredicateRules(self, rls):
     #   self.rules = rls

    def addPredicateRule(self, rle):
        if self.rules is None:
            self.rules = [rle]
        else:
            if rle not in self.rules:
                self.rules.append(rle)

    def __str__(self):
        return f"[ID, NAME] = [{self.id}, {self.name}]\n"
    


