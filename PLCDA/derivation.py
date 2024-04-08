import random
from homomorphism import find_homomorphism
from facts import Fact, set_facts


def derive_method(rule: object, fact: dict) -> object:
    """

    :param rule:
    :param fact:
    :return: derived result
    """
    derived_result = []
    random_dict = {}
    fresh_variables = ['X', 'Y', 'Z']
    mapping = find_homomorphism(rule, fact)
    # print("rule has id", rule.getRuleID())
    # print("mapping", mapping)
    if mapping is not None:
        if len(mapping) != 0:
            for key, val in rule.getRuleConclusionVariables().items():
                if isinstance(val, tuple):
                    new_list = []
                    for i in val:
                        if i in mapping.keys():
                            if isinstance(mapping[i], list):
                                for const in mapping[i]:
                                    new_list.append(const)
                            else:
                                new_list.append(mapping[i])
                        else:
                            if len(random_dict) == 0:
                                random_val = random.choice(fresh_variables)
                                random_dict[i] = random_val
                                new_list.append(random_val)
                            else:
                                if i in random_dict.keys():
                                    new_list.append(random_dict[i])
                                else:
                                    random_val = random.choice(fresh_variables)
                                    random_dict[i] = random_val
                                    new_list.append(random_val)
                    derived_result.append({key: new_list})
                else:
                    if val in mapping.keys():
                        if isinstance(mapping[val], list):
                            for con in mapping[val]:
                                derived_result.append({key: mapping[con]})
                        else:
                            derived_result.append({key: mapping[val]})
                    else:
                        if len(random_dict) == 0:
                            random_val = random.choice(fresh_variables)
                            random_dict[val] = random_val
                            derived_result.append({key: random_val})
                        else:
                            if val in random_dict.keys():
                                derived_result.append({key: random_dict[val]})
                            else:
                                random_val = random.choice(fresh_variables)
                                random_dict[val] = random_val
                                derived_result.append({key: random_val})
    else:
        return None

    return derived_result


# context derive method for anomaly detection


def context_make_derivation(context: object, fact: dict) -> object:
    """
    :param context:
    :param fact:
    :return: new facts derived
    """
    result = []
    new_fact_list = []
    rules = context.getContextExistentialRules()
    if rules is not None:
        for rule in rules.copy():
            res = derive_method(rule, fact)
            # print("facts are", fact)
            # print("res", res)
            if res is not None:
                rules.remove(rule)
                if res in result:
                    break
                else:
                    result.append(res)
                    new_fact = Fact(len(set_facts) + 1)
                    # print("res", res)
                    for item in res:
                        for key, val in item.items():
                            new_fact.addFacts(key, val)
                            new_fact.addFactTerms(key)
                            new_fact.addFactConstant(val)
                        new_fact_list.append(new_fact)
    else:
        print("nothing can be derived as no rules left in context")
    return new_fact_list
