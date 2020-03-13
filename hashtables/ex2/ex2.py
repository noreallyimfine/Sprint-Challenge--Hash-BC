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
    ## bad answer, quadratic time
    for ticket in tickets:
        hash_table_insert(ht, ticket.source, ticket.destination)

    for i in range(length):
        key = hash_table_retrieve(ht, tickets[i].source)
        if key == "NONE":
            



    for i in range(length):
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)

        # if the ticket has no source, the dest is first in routes
        if tickets[i].source == "NONE":
            routes[0] = tickets[i].destination
        # if ticket has no dest, the source is last in routes
        elif tickets[i].destination == "NONE":
            routes[-1] = tickets[i].source
        
        else:

    
    return route
        
