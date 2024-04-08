negative_rules_set = set()


def negative_rules(rules: object) -> set:
    for r in rules.copy():
        con = r.getRuleConclusions()
        if 'alert' in con:
            rules.remove(r)
            negative_rules_set.add(r)
    return negative_rules_set
