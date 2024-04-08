import time
from derivation import derive_method, context_make_derivation
from homomorphism import generate_combinations
from context import context_conclusion
import copy



def anomaly_detection(facts, context, negative_rule):
    k = 0
    print("length of facts is", len(facts))
    derived_facts = set()
    fresh_variables = ['X', 'Y', 'Z']
    start = time.perf_counter()
    previous_result = []
    # print("facts are", facts)
    while True:
        current_result = []
        k += 1
        res = derive_method(negative_rule, facts)
        if (res is not None) and (len(res) != 0):
            for item in res:
                if 'alert' in item.keys():
                    print("Alert!!! Anomaly detected")
                    print("Anomaly caused by rule", negative_rule.getRuleID())
                    print("rule body predicates are", negative_rule.getRuleBodyPredicates())
                    end = time.perf_counter()
                    processing_time = end - start
                    print("processing time is for detection of attack is", processing_time)
                    return
        else:
            print("at context level")
            for c in context:
                derivation = context_make_derivation(c, facts)
                if derivation is not None:
                    if len(derivation) == 0:
                        continue
                    else:
                        current_result.append(derivation)
                else:
                    print("Nothing derived")
        if previous_result is not None and previous_result == current_result:
            print("no new facts derived, we are at Comparison level")
            end = time.perf_counter()
            processed_time = end - start
            print("Derivation ends in", processed_time)
            return
        else:
            previous_result = copy.deepcopy(current_result)
            for r in current_result:
                for item in r:
                    derived_facts.add(item)
                    new_facts = item.getFacts()
                    for key, val in new_facts.items():
                        facts[key] = val
    end = time.perf_counter()
    process_time = end - start
    print("Derivation ends in ", process_time)
    return derived_facts
