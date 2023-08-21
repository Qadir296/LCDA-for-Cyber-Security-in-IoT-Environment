from LCDA.dataset import *

class Context:
    def __init__(self, contextID: int):
        self.contextID = contextID      # Context Id
        self.contextExistentialRules = set()        # provide a set of rules that are inside the context
        self.contextLabel = None      # provide the body predicates of the rules inside the context
        self.ruleSize = []            # size of the body of the rules in context
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


def contextMaking(rules):
    C = set()

    for i in rules:
        result = []
        if len(C) == 0:
            cont = Context(0)
            cont.addContextExistentialRule(i)
            cont.addRuleBodySize(i.getRuleBodyPredicatesSize())
            cont.addContextConclusions(i.getRuleConclusions())
            for j in i.getRuleBodyPredicates():
                cont.addContextLabel(j)
            C.add(cont)
        else:
            for c in C:
                label = set(c.getContextLabel())
                res = label.intersection(set(i.getRuleBodyPredicates()))
                if len(res) != 0:
                    result.append(res)
                    cxt = c
            if len(result) == 0:
                cont = Context(len(C))
                cont.addContextExistentialRule(i)
                cont.addRuleBodySize(i.getRuleBodyPredicatesSize())
                cont.addContextConclusions(i.getRuleConclusions())
                for j in i.getRuleBodyPredicates():
                    cont.addContextLabel(j)
                C.add(cont)
            else:
                cxt.addContextExistentialRule(i)
                for j in i.getRuleBodyPredicates():
                    cxt.addContextLabel(j)
    return C

contexts = contextMaking(set_rules)