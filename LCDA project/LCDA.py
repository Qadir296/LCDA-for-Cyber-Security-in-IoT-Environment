import copy, time
from derivation import *
from facts import *
from rule import *
from context import *
from dataset import *

def anomaly_Detection(rules, facts, context, negative_rule):
  k = 0           ## number of derivation
  start = time.perf_counter()
  previous_result = []
  current_result = []
  while True:
    k+=1
    matching_context = []
    negative_predicates = []
    #print(len(facts))
    partition_context = fact_Partition(facts, context)
    #print("the partition is", [obj.getFacts() for obj in partition_context])
    #print(partition_context)
    if len(negative_rule) != 0:
      partition_negative = partition(facts, negative_rule)
      combined_facts = generate_combinations(facts, len(facts))
     # print("combined facts", combined_facts)
      for rule in negative_rule:
          for fact_partition in combined_facts:
              result = derive_method(rule, fact_partition)
              #print(result)
              if result is not None:
                  for item in result:
                      if 'alert' in item.keys():
                          print("Alert!!!!! Anomaly Detected.")
                          print("Anomaly caused due to Rule ID:", rule.getRuleID())
                          print("Rule Body Predicates:", rule.getRuleBodyPredicates())
                          end = time.perf_counter()
                          process_time = end - start
                          print("Processing time:", process_time)
                          return
              else:
                  negative_predicates.append(rule.getRuleBodyPredicates())
    else:
        print("No negative rules found.")
        end = time.perf_counter()
        process_time = end - start
        print("Processing time:", process_time)
        return
    for c in context:
      list_context_conclusion = context_conclusion(c)
      # putting the values in one list
      flattened_list = [item for sublist in list_context_conclusion for item in sublist]
      # print("list of conclusions", list_context_conclusion)
      for p in negative_predicates:
          # print("negative Predicate is", p)
          common_elements = set(flattened_list).intersection(p)
          if len(common_elements) == 0:
              continue
          else:
             #print("here inside context loop")
             com = generate_combinations(facts, len(facts))
             #print("com is", com)
             for val in com:
                #print("here inside fact loop")
                derivation = context_make_derivation(c, val)
                # print("new fact derived", derivation)
                if derivation is not None:
                    if len(derivation) == 0:
                        continue
                    else:
                        current_result.append(derivation)
                else:
                   print("nothing derived")
                   return
    #print("current derivation list is", [inner_obj.getFacts() for outer_list in current_result for inner_obj in outer_list])
    #print("previous derivation list is", [inner_obj.getFacts() for outer_list in previous_result for inner_obj in outer_list])
    if previous_result is not None and previous_result == current_result:
      print("No new facts derived")
      end = time.perf_counter()
      process_time = end - start
      print("Processing time:", process_time)
      return
    else:
        previous_result = copy.deepcopy(current_result)
        for result in current_result:
            for item in result:
                facts.add(item)  
  end = time.perf_counter()
  process_time = end - start
  print("Processing time:", process_time)
  return facts