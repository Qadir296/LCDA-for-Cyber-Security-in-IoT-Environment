import multiprocessing
from context import contextMaking
from facts import set_facts
from rules import set_rules
from homomorphism import generate_combinations
from anomaly_detection import anomaly_detection
from negative_rule import negative_rules
from facts_partition import fact_partition1
from new import arrange, context_kb
from partition import partition
import time


start = time.perf_counter()

if __name__ == "__main__":
    negative_rules_set = negative_rules(set_rules)
    contexts = contextMaking(set_rules)
    combined_facts = generate_combinations(set_facts, len(set_facts))
    # partition of facts for negative rules
    neg_facts = partition(combined_facts, negative_rules_set)
    # fact partition for context
    fact_context = fact_partition1(combined_facts, contexts)
    # putting the context related to negative rules together in one tuple
    result = arrange(negative_rules_set, contexts)
    # create a tuple for each negative rule, consist context, facts and negative rule
    pro = context_kb(negative_rules_set, fact_context, neg_facts, result)
    processes = []
    for t in pro:
        process = multiprocessing.Process(target=anomaly_detection, args=(t[0], t[1], t[2]))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    total_time = time.perf_counter() - start
    print("Derivation ends here in", total_time)