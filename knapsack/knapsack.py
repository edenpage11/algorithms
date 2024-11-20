from dataclasses import dataclass, field

# instantiate with Item(value = , weight = )
# update level with itemInstance.level = index
@dataclass
class Item:
    value: int
    weight: int
    level: int = field(default=-1)

class Node():
    def __init__(self, item, parent = None, capacity = 0):
        self.parent = parent
        self.item = item
        if parent:
            self.capacity = parent.capacity
        else:
            self.capacity = capacity
        self.cur_value = 0 if parent is None else parent.cur_value
        if parent and parent.yes == self:  # If this is the "yes" branch
            self.cur_value += parent.item.value
            self.capacity -= parent.item.weight
        self.level = item.level

    def visit(self, stack, items):
        global BEST_REAL_VALUE

        self.yes = None
        
        print("visit", self, BEST_REAL_VALUE)

        # leaf node base case
        if self.item.level == len(items) - 1:
            if self.cur_value > BEST_REAL_VALUE:
                BEST_REAL_VALUE = self.cur_value
            return
        
        # If the item's weight exceeds the remaining capacity, skip the "yes" branch
        if self.item.weight <= self.capacity:
            self.yes = Node(items[self.level + 1], parent = self)

        self.no = Node(items[self.level + 1], parent = self)
        if not is_subtree_worse(self.no):
            stack.append(self.no)
        if self.yes:
            if not is_subtree_worse(self.yes):
                stack.append(self.yes)
        return
    
def read_file(filename):
    with open(filename, 'r') as f:
        firstline = f.readline()
        capacity, depth = firstline.strip().split(" ")
        capacity, depth = int(capacity), int(depth)

        itemList = []
        for line in f:
            value, weight = line.strip().split(" ")
            itemList.append(Item(int(value), int(weight)))
        itemList = sorted(
            itemList, key=lambda item: item.value / item.weight, reverse=True)
        for i in range(len(itemList)):
            itemList[i].level = i
    return capacity, depth, itemList

filename = "problem16.7test.txt"
# Global variables:
CAPACITY, DEPTH, ITEMLIST = read_file(filename)
BEST_REAL_VALUE = 0

def dfs(itemList, capacity, depth):
    rootNode = Node(itemList[0], capacity = capacity)
    stack = [rootNode]
    while stack:
        curNode = stack.pop()
        curNode.visit(stack, itemList)


def optimism(node):
    '''Calculate the optimistic estimate of the value of a node's subtree.'''

    # The items that have not yet been considered (i.e. the items that are below the current node in the tree)
    # itemList is a global variable that contains a sorted list of all item objects
    avalaible_items = ITEMLIST[node.level:]
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
    dfs(ITEMLIST, CAPACITY, DEPTH)


if __name__ == '__main__':
    main()