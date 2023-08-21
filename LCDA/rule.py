from LCDA.predicate import *

class Rule:
    def __init__(self, ruleID: int):
        self.ruleID = ruleID    # rule Id
        self.ruleBodyPredicates = [] # provide list of predicates that are used in the rule
        self.ruleExistentialVariables = {}  # a dictionary of Predicates as key, and variable as value
        self.ruleConclusions = []   # provide the list of the predicates used in the conclusion
        self.ruleConclusionVariables = {}

    def getRuleID(self):
        return self.ruleID

    def addRuleBodyPredicates(self, predicate: str):
        self.ruleBodyPredicates.append(predicate)

    def getRuleBodyPredicatesSize(self):
        return len(self.ruleBodyPredicates)

    def getRuleBodyPredicates(self):
        return self.ruleBodyPredicates

    def addRuleExistentialVariable(self, predi ,variable):
        self.ruleExistentialVariables[predi] = variable

    def getRuleExistentialVariables(self):
        if len(self.ruleExistentialVariables) == 0:
            return None
        return self.ruleExistentialVariables

    def addRuleConclusion(self, conclusion: str):
        self.ruleConclusions.append(conclusion)

    def getRuleConclusions(self):
        return self.ruleConclusions

    def addRuleConclusionVariables(self, predi ,variable):
        self.ruleConclusionVariables[predi] = variable

    def getRuleConclusionVariables(self):
        if len(self.ruleConclusionVariables) == 0:
            return None
        return self.ruleConclusionVariables
    



def negative_rules(rules)->set:
  negative_rules_set = set()
  for r in rules.copy():
    Con = r.getRuleConclusions()
    if 'alert' in Con:
      rules.remove(r)
      negative_rules_set.add(r)
  return negative_rules_set