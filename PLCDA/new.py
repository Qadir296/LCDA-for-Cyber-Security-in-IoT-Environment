from facts_partition import fact_partition1
from context import context_conclusion


def arrange(negative_rules: object, context: object) -> list:
    matched_res = []
    for negative_rule in negative_rules:
        matched_context = []
        t = tuple()
        neg_predicate = [negative_rule.getRuleBodyPredicates()]
        neg_predicate_list = [item for sublist in neg_predicate for item in sublist]
        neg_pred_set = set(neg_predicate_list)
        for c in context:
            context_conclusions = context_conclusion(c)
            if context_conclusions is None:
                break
            else:
                conclusions_list = [item for sublist in context_conclusions for item in sublist]
                res = set(conclusions_list).intersection(neg_pred_set)
                if len(res) != 0:
                    matched_context.append(c)
        t = (negative_rule, matched_context)
        matched_res.append(t)
        # matching facts

    return matched_res


def context_kb(negative_rule: object, context_facts: dict, negative_facts: object, res: list) -> list:
    ckb = []
    for i in negative_rule:
        n = negative_facts.get(i)
        for t in res:
            if i == t[0]:
                for j in t[1]:
                    f = context_facts.get(j.getContextID())
                    if f is not None:
                        n.update(f)
                tup = (n, t[1], t[0])
                ckb.append(tup)

    return ckb
