from itertools import combinations


def generate_combinations(data: object, size: int) -> list:
    """

    :param data:
    :param size:
    :return: list of dictionaries
    """
    combinations_list = []
    terms = []
    for i in data:
        terms.append(i.getFacts())
    keys = terms[0].keys() 
    for comb in combinations(terms, size):
        combined_dict = {k: v for d in comb for k, v in d.items()}
        combinations_list.append(combined_dict)
    return combinations_list


def find_homomorphism(rule: object, fact: dict) -> dict:
    substitution_dict = {}
    l_pred = list(fact.keys())
    comb_list = list(combinations(l_pred, rule.getRuleBodyPredicatesSize()))
    # print("this is the combination list", comb_list)
    rule_values = rule.getRuleExistentialVariables()
    rule_body = rule.getRuleBodyPredicates()
    # print("body of rule", tuple(rule_body))
    for comb in comb_list:
        if set(comb) == set(rule_body):
            # print("test passed")
            for predicate in rule_body:
                try:
                    value = fact[predicate]
                    substitution_dict[rule_values[predicate]] = value
                except KeyError:
                    return None
    return substitution_dict
