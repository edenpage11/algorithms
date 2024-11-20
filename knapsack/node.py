from dataclasses import dataclass, field

# instantiate with Item(value = , weight = )
# update level with itemInstance.level = index
@dataclass
class Item:
    value: int
    weight: int
    level: int = field(default=-1)


class Node():
    def __init__(self, item, is_subtree_worse_function, parent = None, capacity = 0):
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
        self.is_subtree_worse = is_subtree_worse_function

    def visit(self, stack, items):
        global BEST_REAL_VALUE

        self.yes = None

        # leaf node base case
        if self.item.level == len(items) - 1:
            if self.cur_value > BEST_REAL_VALUE:
                BEST_REAL_VALUE = self.cur_value
            return
        
        # If the item's weight exceeds the remaining capacity, skip the "yes" branch
        if self.item.weight <= self.capacity:
            self.yes = Node(items[self.level + 1], self.is_subtree_worse, parent = self)

        self.no = Node(items[self.level + 1], self.is_subtree_worse, parent = self)
        if not self.is_subtree_worse(self.no):
            stack.append(self.no)
        if self.yes:
            if not self.is_subtree_worse(self.yes):
                stack.append(self.yes)
        return


