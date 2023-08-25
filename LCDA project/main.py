from LCDA import anomaly_Detection
from derivation import *
from dataset import *
from context import *


if __name__ == "__main__":
    negative_rules_set = negative_rules(set_rules)
    contexts = contextMaking(set_rules)
    anomaly = anomaly_Detection(set_rules, set_facts, contexts, negative_rules_set)

