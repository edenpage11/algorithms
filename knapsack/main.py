from node import Item, Node


def read_file(filename):
    with open(filename, 'r') as f:
        firstline = f.readline()
        capacity, depth = firstline.strip().split(" ")
        itemList = []
        for line in f:
            value, weight = line.strip().split(" ")
            itemList.append(Item(int(value), int(weight)))
        itemList = sorted(
            itemList, key=lambda item: item.value / item.weight, reverse=True)
        for i in range(len(itemList)):
            itemList[i].level = i
    return capacity, depth, itemList


def optimism(node):
    '''Calculate the optimistic estimate of the value of a node's subtree.'''

    # The items that have not yet been considered (i.e. the items that are below the current node in the tree)
    # itemList is a global variable that contains a sorted list of all item objects
    avalaible_items = itemList[node.level:]
    capacity = node.capacity
    current_value = node.cur_value

    for item in avalaible_items:
        if item.weight <= capacity:
            capacity -= item.weight
            current_value += item.value
        else:
            # If the item does not fit in the knapsack, add the fraction of the item that does fit
            current_value += item.value * (capacity / item.weight)
            break

    return current_value


def is_subtree_worse(node) -> bool:
    '''
    Check if the node's optimistic estimate is better than the best solution found so far.
    return True if the node's subtree is not worth exploring, 

    Return False if you should push the current node's children onto the stack:
        push 'no' child first, then push 'yes' child (so that 'yes' child is popped first)
    '''
    # call this function when visiting a node
    global BEST_REAL_VALUE
    if optimism(node) < BEST_REAL_VALUE:
        return True
    else:
        return False


def main():
    # TODO: put this at very top of file
    filename = "problem16.7test.txt"
    # Global variables:
    CAPACITY, DEPTH, ITEMLIST = read_file(filename)
    BEST_REAL_VALUE = 0


if __name__ == '__main__':
    main()
