# for random creation of predicates and facts
from predicates import predicates_names, set_predicates, Predicate
import random

def random_predicates(range_val, predicates_list):
    for i in range(range_val):
        ident = i + 1
        num = random.choice(predicates_list)
        nm = num + str(ident)
        deg = random.randint(1, 10)
        predicate = Predicate(ident, nm, deg)
        set_predicates.add(predicate)
    return set_predicates


# provide the size of the predicates
random_predicates(1000, predicates_names)
