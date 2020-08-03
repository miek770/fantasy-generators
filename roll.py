from random import randint

def expand(table):
    """Flatten and expand the table.

    The original table is a list of tuples, of which the 1st element is a
    value and the second a weight. The resulting table is a list of values,
    where each value appears a number of times defined by its weight.

    :param table: Original table
    :type table: List of (Value, Weight).
    :return: Flattened table
    :rtype: List of values
    """
    t = []
    for r in table:
        for _ in range(r[1]):
            t.append(r[0])
    return t


def roll(table):
    """Roll the table.

    Return a random value from the table, with probabilities dependent on each
    value's weigth.

    :param table: [description]
    :type table: [type]
    :return: [description]
    :rtype: [type]
    """
    t = expand(table)
    return t[randint(0, len(t) - 1)]


def roll_exclusive(table1, table2):
    """Roll each table seperately, without yielding the same index from each.

    Return a random value from each table, while ensuring that they don't
    share the same index number from their respective table.

    :param table1: [description]
    :type table1: [type]
    :param table2: [description]
    :type table2: [type]
    :return: [description]
    :rtype: [type]
    """
    t1 = roll(table1)
    for index1, entry in enumerate(table1):
        if entry[0] == t1:
            break
    while(True):
        t2 = roll(table2)
        for index2, entry in enumerate(table2):
            if entry[0] == t2:
                break
        if index1 != index2:
            return (t1, t2)