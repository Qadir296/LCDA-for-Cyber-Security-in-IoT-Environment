def fact_partition1(fact: dict, context: set) -> dict:
    """

    :param fact:
    :param context:
    :return: partitioned fact
    """
    new_dict = {}
    for c in context:
        con_dict = {}
        label = c.getContextLabel()
        # print("label of c", c.getContextLabel())
        for i in label:
            for f in fact:
                if i in f.keys():
                    con_dict[i] = f[i]
                    new_dict[c.getContextID()] = con_dict
    return new_dict
