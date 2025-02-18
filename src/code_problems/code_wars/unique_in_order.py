from itertools import groupby


# https://www.codewars.com/kata/54e6533c92449cc251001667
def unique_in_order(sequence):
    final_seq = []
    for item in sequence:
        if len(final_seq) == 0:
            final_seq.append(item)
        elif final_seq[len(final_seq) - 1] != item:
            final_seq.append(item)
    return final_seq


def unique_in_order_alternative(sequence):
    return [item for item, _ in groupby(sequence)]
