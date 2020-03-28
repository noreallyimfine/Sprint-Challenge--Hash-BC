#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    current = hash_table_retrieve(hashtable, "NONE")
    route[0] = current
    for i in range(1, length):
        next_stop = hash_table_retrieve(hashtable, current)
        route[i] = next_stop
        current = next_stop
    
    return route[:-1]
        
