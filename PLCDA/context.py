from classes import *


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


def context_conclusion(context) -> list:
    list_conclusions = []
    if context.getContextExistentialRules() is not None:
        for rule in context.getContextExistentialRules():
            conclusion_rule = rule.getRuleConclusions()
            list_conclusions.append(conclusion_rule)
    else:
        return None
    return list_conclusions
