_author_ = 'roman'

import itertools

def powerset(set_, n):
  # note we return an iterator rather than a list
  return itertools.chain.from_iterable( itertools.combinations(set_,k) for k in range(1,n+1) )

# очень плохая функция, некоторые разбиения эквивалентны
def get_all_partitions(set_, q):
    if len(set_) == 1:
        return [[tuple(set_)]]

    res = []
    if len(set_) <= q:
        res.append((tuple(set_),))

    for subset in powerset(set_, min(q, len(set_)-1)):
        for partition_of_another_subset in get_all_partitions(set_ - set(subset), q):
            res.append((subset, *partition_of_another_subset))

    return res