#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    index = 0
    for weight in weights:
        # weight > limit, ignore it
        if weight > limit:
            pass
        # otherwise
        else:
            # check if limit - weight in hashtable
            if hash_table_retrieve(ht, (limit - weight)) is None:
                # if no insert to hashtable as (weight, index)
                hash_table_insert(ht, weight, index)
            else:
                # return tuple if yes
                other_weight = hash_table_retrieve(ht, (limit - weight))
                if index > other_weight:
                    answer = (index, other_weight)
                    return answer
                else:
                    answer = (other_weight, index)
                    print(answer)
                    return answer

        index += 1
    # base case returns None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
