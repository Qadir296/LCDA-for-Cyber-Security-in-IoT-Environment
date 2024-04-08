
def partition(facts: list, negative_rules: object) -> dict:
    facts_dict = {}
    for neg_r in negative_rules:
        new_dict = {}
        for f in facts:
            for k in f.keys():
                if k in neg_r.getRuleBodyPredicates():
                    new_dict[k] = f[k]
                    facts_dict[neg_r] = new_dict
    return facts_dict
