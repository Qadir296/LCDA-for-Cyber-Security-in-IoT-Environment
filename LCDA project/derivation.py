from itertools import combinations
import random
from facts import *
from rule import *
from context import *
from dataset import *

def generate_combinations(data, size):
    combinations_list = []
    terms = []
    for i in data:
        terms.append(i.getFacts())
    keys = terms[0].keys()  # Assuming all dictionaries in the list have the same keys
    for comb in combinations(terms, size):
        combined_dict = {k: v for d in comb for k, v in d.items()}
        combinations_list.append(combined_dict)
    return combinations_list


def find_homomorphism(rule, fact):
    substitution_dict = {}
    rule_values = rule.getRuleExistentialVariables()
    rule_body = rule.getRuleBodyPredicates()
    if fact is not None:
        for predicate in rule_body:
            try:
                value = fact[predicate]
                substitution_dict[rule_values[predicate]] = value
            except KeyError:
                return None
    return substitution_dict


def derive_method(rule, fact):
    derived_result = []
    random_dict = {}
    fresh_variables = ['X', 'Y', 'Z']
    mapping = find_homomorphism(rule, fact)
    #print("rule has id", rule.getRuleID())
    conclusion_predicates = rule.getRuleExistentialVariables().keys()
    #print("mapping", mapping)
    if mapping is not None:
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


def context_conclusion(context) -> list:
    list_conclusions = []
    for rule in context.getContextExistentialRules():
        conclusion_rule = rule.getRuleConclusions()
        list_conclusions.append(conclusion_rule)
    return list_conclusions


### context derive methond for anomaly detection



def context_make_derivation(context, fact):
    result = []
    new_fact_list = []
    for rule in context.getContextExistentialRules():
        res = derive_method(rule, fact)
        # print("res", res)
        if res is not None:
            if res in result:
                break
            else:
                result.append(res)
                new_fact = Fact(len(set_facts) + 1)
                for item in res:
                    for key, val in item.items():
                        new_fact.addFacts(key, val)
                        new_fact.addFactTerms(key)
                        new_fact.addFactConstant(val)
                    new_fact_list.append(new_fact)
    return new_fact_list

