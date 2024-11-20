

def optimism(node):
    '''Calculate the optimistic estimate of the value of a node's subtree.'''

    # The items that have not yet been considered (i.e. the items that are below the current node in the tree)
    # item_list is a global variable that contains a sorted list of all item objects
    avalaible_items = item_list[node.level:]
    capacity = node.capacity
    current_value = node.item.value

    for item in avalaible_items:
        if item.weight <= capacity:
            capacity -= item.weight
            current_value += item.value
        else:
            # If the item does not fit in the knapsack, add the fraction of the item that does fit
            current_value += item.value * (capacity / item.weight)
            break

    return current_value
