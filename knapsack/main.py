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


def main():
    filename = "problem16.7test.txt"
    capacity, depth, itemList = read_file(filename)


if __name__ == '__main__':
    main()
