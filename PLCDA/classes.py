# class for Predicate

class Predicate:
    def __init__(self, ident, nm, deg):
        self.id = ident  # identifier of the predicate
        self.name = nm  # Name of the predicate
        self.degree = deg  # RENAME IT to (degree)
        # self.predicateTerms = [] #
        self.rules = None  # To add a rule to the list that uses the predicate

    def getPredicateID(self):
        return self.id

    def getPredicateName(self):
        return self.name

    # should be getPredicateDegree
    def getPredicateDegree(self):
        return self.degree

    def getPredicateRules(self):
        return self.rules

    # def setPredicateRules(self, rls):
    #   self.rules = rls

    def addPredicateRule(self, rle):
        if self.rules is None:
            self.rules = [rle]
        else:
            if rle not in self.rules:
                self.rules.append(rle)

    def __str__(self):
        return f"[ID, NAME] = [{self.id}, {self.name}]\n"


## class for Rules


class Rule:
    def __init__(self, ruleID: int):
        self.ruleID = ruleID  # rule Id
        self.ruleBodyPredicates = []  # provide list of predicates that are used in the rule
        self.ruleExistentialVariables = {}  # a dictionary of Predicates as key, and variable as value
        self.ruleConclusions = []  # provide the list of the predicates used in the conclusion
        self.ruleConclusionVariables = {}

    def getRuleID(self):
        return self.ruleID

    def addRuleBodyPredicates(self, predicate: str):
        self.ruleBodyPredicates.append(predicate)

    def getRuleBodyPredicatesSize(self):
        return len(self.ruleBodyPredicates)

    def getRuleBodyPredicates(self):
        return self.ruleBodyPredicates

    def addRuleExistentialVariable(self, predi, variable):
        self.ruleExistentialVariables[predi] = variable

    def getRuleExistentialVariables(self):
        if len(self.ruleExistentialVariables) == 0:
            return None
        return self.ruleExistentialVariables

    def addRuleConclusion(self, conclusion: str):
        self.ruleConclusions.append(conclusion)

    def getRuleConclusions(self):
        return self.ruleConclusions

    def addRuleConclusionVariables(self, predi, variable):
        self.ruleConclusionVariables[predi] = variable

    def getRuleConclusionVariables(self):
        if len(self.ruleConclusionVariables) == 0:
            return None
        return self.ruleConclusionVariables


## Context definition

class Context:
    def __init__(self, contextID: int):
        self.contextID = contextID  # Context Id
        self.contextExistentialRules = set()  # provide a set of rules that are inside the context
        self.contextLabel = None  # provide the body predicates of the rules inside the context
        self.ruleSize = []  # size of the body of the rules in context
        self.conclusions = []

    def getContextID(self):
        return self.contextID

    def addContextExistentialRule(self, rule: str):
        self.contextExistentialRules.add(rule)

    def addRuleBodySize(self, i):
        self.ruleSize.append(i)

    def getRuleBodySize(self):
        return self.ruleSize

    def getContextExistentialRules(self):
        if len(self.contextExistentialRules) == 0:
            return None
        return self.contextExistentialRules

    def addContextLabel(self, label):
        if self.contextLabel is None:
            self.contextLabel = [label]
        else:
            if label not in self.contextLabel:
                self.contextLabel.append(label)

    def getContextLabel(self):
        return self.contextLabel

    def addContextConclusions(self, conclusion):
        self.conclusions.append(conclusion)

    def getContextConclusions(self):
        return self.conclusions


# class Facts

class Fact:
    def __init__(self, ident):
        self.id = ident  # fact id
        self.constant = []  # list of constants for fact
        self.terms = []  # list of predicates of fact --> this is not the terms, name it Predicate
        self.facts = {}  # dict providing predicates as key and const as values

    def getFactId(self):
        return self.id

    def addFacts(self, pred, const):
        self.facts[pred] = const

    def getFacts(self):
        return self.facts

    def addFactTerms(self, predicate: str):
        self.terms.append(predicate)

    def addFactConstant(self, const):
        self.constant.append(const)

    def getFactTerms(self):
        return self.terms

    def getFactConstant(self):
        return self.constant

    def __del__(self):
        del self.terms


##Partitioned Facts

class PartitionedFact:
    def __init__(self, id):
        self.id = id  # id for the partitioned fact, normally set as the id of context matched
        self.Facts = []  # list of the facts added

    def getID(self):
        return self.id

    def addFacts(self, fact):
        self.Facts.append(fact)

    def getPartitionedFacts(self):
        return self.Facts
