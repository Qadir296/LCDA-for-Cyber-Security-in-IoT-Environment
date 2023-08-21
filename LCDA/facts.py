class Fact:
    def __init__(self, ident):
        self.id = ident         #fact id
        self.constant = []      # list of constants for fact
        self.terms = []         #list of predicates of fact --> this is not the terms, name it Predicate
        self.facts = {}         # dict providing predicates as key and const as values

    def getFactId(self):
        return self.id

    def addFacts(self, pred, const):
        self.facts[pred] = const

    def getFacts(self):
        return self.facts

    def addFactTerms(self, predicate: str):
        self.terms.append(predicate)

    def addFactConstant(self, const):
        self.constant.append(const)

    def getFactTerms(self):
        return self.terms

    def getFactConstant(self):
        return self.constant

    def __del__(self):
        del self.terms


def partition(facts, negative_rule):
    matched_facts_set = set()
    result = []
    for i in negative_rule:
        matched_facts = []
        predicate = i.getRuleBodyPredicates()
        #print(predicate)
        for j in facts:
            terms = set(j.getFactTerms())
            res = terms.intersection(set(predicate))
            if res:  # If intersection is not empty
                #print("res", res)
                result.append(res)
                matched_facts.append(j)
                #print(matched_facts)
        return matched_facts  # Move the return statement here if you want to return the matched_facts



### Fact Partitions

def fact_Partition(facts, context):
    set_Partition_Fact = set()
    matched_facts = []
    for c in context:
        label = set(c.getContextLabel())
        #print("label", label)
        matched_facts = []
        for j in facts:
            if j is not None:
                terms = j.getFactTerms()
                #print("terms of fact", terms)
                common_terms = set(terms).intersection(label)
                if common_terms:  # Intersection is not empty
                    matched_facts.append(j)
                    #print(matched_facts)
        if matched_facts:
            return matched_facts  # Move the return statement here if matches are found
    return matched_facts  # Move the return statement here if no matches are found